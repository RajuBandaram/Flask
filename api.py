# Requirements:
# pip install flask
# pip install flask_restful

from flask import Flask
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
     "Status": "Alive"
}

help_Details = {   
   "Available REST API's Are: ": ["/ping", "/info"]
}


class Employee(Resource):
    def get(self,ename=None):
        if ename:
            if ename in emp_info.keys():
                return emp_info.get(ename)
            else:
                msg = {"Message": "Employee not listed with name: "+ename}
                return msg
        else:
            return emp_info


class Ping(Resource):
    def get(self):
        return ping_Details


class Help(Resource):
    def get(self):
        return help_Details


# api.add_resource(Employees,"/info")
api.add_resource(Employee,"/info","/info/<string:ename>")
api.add_resource(Help,"/")
api.add_resource(Ping,"/ping")


app.run(host="localhost", port=5000, debug='true')
