import os
import pickle

import numpy as np

from flask import Flask
from flask import Response
from flask import jsonify
from flask import request

app = Flask(__name__)

prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')

class ScoringService(object):
    model = None

    @classmethod
    def get_model(cls):
        if cls.model == None:
            model_file = os.path.join(model_path, 'model.pkl')
            cls.model = pickle.load(open(model_file, 'rb'))
        return cls.model

    @classmethod
    def predict(cls, input):
        model = cls.get_model()
        return model.predict(input)


@app.route('/ping', methods=['GET'])
def ping():
    health = ScoringService.get_model() is not None

    status = 200 if health else 404
    return Response(response='\n', status=status, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():
    """Do an inference on a single batch of data."""
    if request.content_type == 'application/json':
        data = np.array(request.json)
    else:
        return Response(response='This model only supports JSON data', status=415, mimetype='text/plain')

    print('Invoked with {} records'.format(data.shape[0]))

    predictions = ScoringService.predict(data)
    return jsonify({'predictions': predictions.tolist()})
