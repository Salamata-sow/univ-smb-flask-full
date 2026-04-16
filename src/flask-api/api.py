from flask import Flask, jsonify
import json
from flask import request
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!"

@app.route("/config/lb", methods=["GET"])
def get_loadbalancers():
    with open("data/loadbalancer.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/config/lb/<int:id>", methods=["GET"])
def get_lb(id):
    with open("data/loadbalancer.json") as f:
        data = json.load(f)

    for lb in data:
        if lb["id"] == id:
            return jsonify(lb)

    return jsonify({"error": "not found"}), 404

@app.route("/config/lb", methods=["POST"])
def add_lb():
    new_lb = request.json

    file_path = os.path.join(os.path.dirname(__file__), "data", "loadbalancer.json")

    with open(file_path) as f:
        data = json.load(f)

    data.append(new_lb)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify(new_lb), 201

@app.route("/config/lb/<int:id>", methods=["DELETE"])
def delete_lb(id):
    file_path = os.path.join(os.path.dirname(__file__), "data", "loadbalancer.json")

    with open(file_path) as f:
        data = json.load(f)

    data = [lb for lb in data if lb["id"] != id]

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({"message": "deleted"})


@app.route("/config/webserver", methods=["GET"])
def get_webservers():
    file_path = os.path.join(os.path.dirname(__file__), "data", "webserver.json")

    with open(file_path) as f:
        data = json.load(f)

    return jsonify(data)

@app.route("/config/webserver/<int:id>", methods=["GET"])
def get_webserver(id):
    file_path = os.path.join(os.path.dirname(__file__), "data", "webserver.json")

    with open(file_path) as f:
        data = json.load(f)

    for ws in data:
        if ws["id"] == id:
            return jsonify(ws)

    return jsonify({"error": "not found"}), 404


@app.route("/config/webserver", methods=["POST"])
def add_webserver():
    new_ws = request.json

    file_path = os.path.join(os.path.dirname(__file__), "data", "webserver.json")

    with open(file_path) as f:
        data = json.load(f)

    data.append(new_ws)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify(new_ws), 201

@app.route("/config/webserver/<int:id>", methods=["DELETE"])
def delete_webserver(id):
    file_path = os.path.join(os.path.dirname(__file__), "data", "webserver.json")

    with open(file_path) as f:
        data = json.load(f)

    data = [ws for ws in data if ws["id"] != id]

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({"message": "deleted"})


@app.route("/config/reverseproxy")
def get_reverseproxy_list():
    with open("data/reverseproxy.json") as f:
        return jsonify(json.load(f))

@app.route("/config/reverseproxy/<int:id>")
def get_reverseproxy_detail(id):
    with open("data/reverseproxy.json") as f:
        data = json.load(f)

    for rp in data:
        if rp["id"] == id:
            return jsonify(rp)

    return jsonify({"error": "not found"}), 404
@app.route("/config/reverseproxy", methods=["POST"])
def add_reverseproxy():
    file = "data/reverseproxy.json"

    with open(file) as f:
        data = json.load(f)

    new = request.json
    data.append(new)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify(new)

@app.route("/config/reverseproxy/<int:id>", methods=["DELETE"])
def delete_reverseproxy(id):
    file = "data/reverseproxy.json"

    with open(file) as f:
        data = json.load(f)

    data = [rp for rp in data if rp["id"] != id]

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({"message": "deleted"})