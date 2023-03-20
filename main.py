from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

# to get the data of all the stars
@app.route("/")
def index():
    return jsonify({
        "data" : data,
        "message" : "success"
    }), 200
    
# to get the data of a specific star
@app.route("/star")  
def star():
    name = request.args.get("name")   
    starData = next(item for item in data if item["name"] == name)
    return jsonify({
        "data" : starData,
        "message" : "success"
    }), 200    
    
if __name__ == "__main__":
    app.run()    