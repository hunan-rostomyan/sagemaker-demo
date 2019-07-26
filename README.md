# SageMaker

## Prepare data
- `./_prepare_data`

This will create train and test data under `data/`.

- `cp -R data/*_data.pkl container/local_test/test_dir/input/data/`

This will copy the files for local testing.

## Local

Suppose the image has been built and has the name `basic`. Change into `local_test`.

### Train
- `./train_local.sh basic`

### Serve
- `./serve_local.sh basic`

### Test
- `./predict.sh payload.json`

```json
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 22
Content-Type: application/json
Date: Thu, 14 Mar 2019 20:18:05 GMT
Server: nginx/1.10.3 (Ubuntu)

{
    "predictions": [
        0,
        2
    ]
}
```


## Lambda invocation

### Handler

```python
# python3.6

import json
import os

import boto3


ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    data = json.loads(json.dumps(event))

    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=json.dumps(data))

    predictions = json.loads(response['Body'].read().decode())['predictions']

    output = []
    for x, y in zip(data, predictions):
        output.append((x, y))

    return {
        'statusCode': 200,
        'body': json.dumps(output)
    }
```

### Environment

- `ENDPOINT_NAME = [ENDPOINT_NAME]` (once it's deployed, the endpoint will be assigned a name)

### Permissions

- Assign or Create a Role and attach this policy: `AmazonSageMakerFullAccess`

### Input

Configure Test Events to so it contains the following list of pairs:

```json
[
  [3.5, 4.5],
  [6.7, 3.1]
]
```

Each of these pairs is an input example that our model will use to predict an integral label. If you press "test" above, the handler will make a request to the SageMaker endpoint, passing that json in and getting a json back; something like this:

```json
[0, 2]
```

### Output

```json
{
  "statusCode": 200,
  "body": "[[[3.5, 4.5], 0], [[6.7, 3.1], 2]]"
}
```
