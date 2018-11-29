from functools import wraps

from flask import Flask, jsonify, request
from flask_restful import Api, Resource, abort

import pickle
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd

app = Flask(__name__)
api = Api(app)

api_key = 'secret_key'
f = 'models/iris.model'

def get_model():
    import numpy as np
    from sklearn import datasets
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    model.fit(x,y)
    return model 

model = get_model()

weather_data = {'Budapest': 2, 'Pecs': 5, 'Szeged': 7,
'Eger': -1}

def require_apikey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        if request.headers.get('token') and request.headers.get('token') == api_key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

class PredictResource(Resource):
    def get_predicts(self, x):
        y = list(map(lambda x: int(x), model.predict(x)))
        return y
        
    @require_apikey
    def post(self):
        message = request.json
        preds = self.get_predicts(message['x'])
        return jsonify(y=preds)


class WeatherResource(Resource):
    def get_weather_data(self, cities):
        weather_res = {}
        for c in cities:
            try:
                weather_res[c] = weather_data[c]
            except:
                pass
        return weather_res
        
    @require_apikey
    def post(self):
        message = request.json
        res = self.get_weather_data(message['cities'])
        print(res)
        return jsonify(weather=res)

api.add_resource(WeatherResource, '/weather')
api.add_resource(PredictResource, '/predict')

if __name__ == '__main__':
    app.run(debug=True)
