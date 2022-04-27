from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Helloworld(Resource):
    def get(self):
        return {'message':'Hello World'}

    def post(self):
        return {'message':'Hello This is post request'}

    def put(self):
        return {'message':'Hello this is put request'}

    def delete(self):
        return {'message':'Hello this is delete request'}

api.add_resource(Helloworld, '/')

if __name__ == '__main__':
    app.run(debug=True)