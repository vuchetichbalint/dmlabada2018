from functools import wraps

from flask import Flask, jsonify, request
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

api_key = 'secret_key'

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

if __name__ == '__main__':
    app.run(debug=True)
