from flask import Flask, jsonify, request

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://rajuamburu:rajasekharpassword@cluster0.poe1vno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
mongoClientConn = MongoClient(uri, server_api=ServerApi('1'))
mongoDB = mongoClientConn['employee_db'] # Select the database
empIdColl = mongoDB['id_card_coll'] # Id Card Collection
empDetailsColl = mongoDB['emp_details_coll']

app = Flask(__name__)

@app.route("/employee_id_details", methods=["GET","POST"])
def employee_details():
    try:
        if request.method == 'POST':
            employee_id_record = request.json
            insertId = empIdColl.insert_one(employee_id_record).inserted_id
            print("Created Employee ID details. Insert-ID :", insertId)
            resp = jsonify({"msg": "Data Inserted", "db_insert_id": str(insertId)})
            return resp
        if request.method == 'GET':
            all_employees = [x for x in empIdColl.find({})]
            print("Fetching the employee details")
            resp = jsonify({"msg": "Data Fetched", "emp_details": str(all_employees)})
            return resp
    except Exception as exp:
        print("Exception details : ", exp)


if __name__ == "__main__":
    app.run()
