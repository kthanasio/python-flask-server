import json
from flask import Flask,jsonify,request

demos = [{
        'id': 1,
        'name': 'Demo 1'
    },
    {
        'id': 2,
        'name': 'Demo 2'
    }]

port = 5002

app = Flask (__name__)

# Health Check
@app.route("/demos/health", methods=['GET'])
def server():
    return f"Server running at port: {port}"

# List all Demos
@app.route("/demos", methods=['GET'])
def listDemos():
    return jsonify(results=demos)

# List 1 Demo
@app.route("/demos/<int:id>")
def demoDetail(id):
    for demo in demos:
        if demo['id'] == id:
            return jsonify(results=demo)

# Create 1 Demo
@app.route("/demos", methods=['POST'])
def createDemos():
    body = request.get_json()
    demos.append(body)
    return jsonify(result='OK')

if (__name__ == "__main__"):
    app.run(host= 'localhost', port=port, debug=True)