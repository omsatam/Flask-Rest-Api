from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

engg_employee_data_dict = {
    100 : {
        'emp_id' : 100,
        'name' : 'emgemp1',
        'salary' : '25000',
        'designation' : 'junior'
    },
    200 : {
        'emp_id' : 200,
        'name' : 'emgemp2',
        'salary' : '45000',
        'designation' : 'senior'
    }
}

sales_employee_data_dict = {
    100 : {
        'emp_id' : 100,
        'name' : 'salesemp1',
        'salary' : '20000',
        'designation' : 'junior'
    },
    200 : {
        'emp_id' : 200,
        'name' : 'salesemp2',
        'salary' : '41000',
        'designation' : 'senior'
    }
}
class EngineeringEmployee(Resource):
    def get(self,emp_id):
        return engg_employee_data_dict[emp_id]

class SalesEmployee(Resource):
    def get(self,emp_id):
        return sales_employee_data_dict[emp_id]

api.add_resource(EngineeringEmployee, '/engg/<int:emp_id>', '/engg_employee/<int:emp_id>')

api.add_resource(SalesEmployee, '/sales/<int:emp_id>', '/sales_employee/<int:emp_id>')
if __name__ == '__main__':
    app.run(debug=True)