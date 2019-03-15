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
