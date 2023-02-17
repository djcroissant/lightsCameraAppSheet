from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

import board
import neopixel

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

# Define color arguments in body
parser.add_argument('r', type=str, location='json')
parser.add_argument('g', type=str, location='json')
parser.add_argument('b', type=str, location='json')

# Define apikey in header
parser.add_argument('apikey', type=str, location='headers', required=True)

# Initialize neopixel object
pixels = neopixel.NeoPixel(board.D18, 360)

# Check apikey
def check_apikey(apikey):
    if apikey != "lightscameraaction":
        abort(404, message='invalid apikey')

class LightsOn(Resource):
    def post(self):
        args = parser.parse_args()
        check_apikey(args['apikey'])
        red = int(args['r'])
        green = int(args['g'])
        blue = int(args['b'])
        pixels.fill((red, green, blue))
        return 200

class LightsOff(Resource):
    def post(self):
        args = parser.parse_args()
        check_apikey(args['apikey'])
        pixels.fill((0, 0, 0))
        return 200

api.add_resource(LightsOn, '/on')

api.add_resource(LightsOff, '/off')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='33', debug=True)