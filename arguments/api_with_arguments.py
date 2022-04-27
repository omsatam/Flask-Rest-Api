from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Helloworld(Resource):
    def get(self,name):
        return {'message':'Hello ' + name}

class Employee(Resource):
    def get(self,emp_id, name):
        return {'Employee ID': emp_id, 'Name': name}

api.add_resource(Helloworld, '/greeting/<string:name>')

api.add_resource(Employee, '/employee/<int:emp_id>/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)