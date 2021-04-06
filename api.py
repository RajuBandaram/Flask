# Requirements:
# pip install flask
# pip install flask_restful

from flask import Flask, make_response, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

emp_info = {
    "Raju": {
        "name": "Raju",
        "Sal": "150000",
        "technology": "Pythonista"
    },
    "Ravi": {
        "name": "Ravi",
        "Sal": "150000",
        "technology": "Cyber Security"
    }
}

ping_Details = {
    "Available REST API's Are: ": ["/api/v1/ping", "/api/v1/info/:ename"]
}

help_Details = {
    "Status": "Alive"
}


# class Employees(Resource):
#     def get(self):
#         return emp_info


class Employee(Resource):
    def get(self,ename=None):
        if ename:
            if ename in emp_info.keys():
                return make_response(jsonify(emp_info.get(ename)), 200)
            else:
                msg = {"Message": "Employee not listed with name: "+ename}
                return make_response(jsonify(msg), 404)
        else:
            return make_response(jsonify(emp_info), 200)


class Ping(Resource):
    def get(self):
        return ping_Details


class Help(Resource):
    def get(self):
        return help_Details


# api.add_resource(Employees,"/info")
api.add_resource(Employee,"/api/v1/info","/api/v1/info/<string:ename>")
api.add_resource(Help,"/api/v1/help")
api.add_resource(Ping,"/")


app.run(host="localhost", port=5000, debug='true')
