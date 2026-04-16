from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route("/")
def start():
    lb = requests.get("http://127.0.0.1:5000/config/lb").json()
    ws = requests.get("http://127.0.0.1:5000/config/webserver").json()

    return render_template("start.html", lb=lb, ws=ws)

@app.route("/lb")
def lb_list():
    response = requests.get("http://127.0.0.1:5000/config/lb")
    lbs = response.json()
    return render_template("lb_list.html", lbs=lbs)

@app.route("/lb/<int:id>")
def lb_detail(id):
    response = requests.get(f"http://127.0.0.1:5000/config/lb/{id}")
    lb = response.json()
    return render_template("lb_detail.html", lb=lb)

@app.route("/lb/create", methods=["GET", "POST"])
def lb_create():
    if request.method == "POST":
        data = {
            "id": int(request.form["id"]),
            "name": request.form["name"],
            "ip_bind": request.form["ip_bind"],
            "pass": request.form["pass"]
        }

        requests.post("http://127.0.0.1:5000/config/lb", json=data)


    return render_template("lb_create.html")

@app.route("/lb/delete/<int:id>")
def lb_delete(id):
    requests.delete(f"http://127.0.0.1:5000/config/lb/{id}")
    return "Supprimé  <a href='/lb'>Retour</a>"

@app.route("/webserver")
def webserver_list():
    response = requests.get("http://127.0.0.1:5000/config/webserver")
    servers = response.json()
    return render_template("webserver_list.html", servers=servers)

@app.route("/webserver/<int:id>")
def webserver_detail(id):
    response = requests.get(f"http://127.0.0.1:5000/config/webserver/{id}")
    ws = response.json()
    return render_template("webserver_detail.html", ws=ws)

@app.route("/webserver/create", methods=["GET", "POST"])
def webserver_create():
    if request.method == "POST":
        data = {
            "id": int(request.form["id"]),
            "name": request.form["name"],
            "ip_bind": request.form["ip_bind"],
            "root": request.form["root"]
        }

        requests.post("http://127.0.0.1:5000/config/webserver", json=data)

        return redirect("/webserver")

    return render_template("webserver_create.html")

@app.route("/webserver/delete/<int:id>")
def webserver_delete(id):
    requests.delete(f"http://127.0.0.1:5000/config/webserver/{id}")
    return redirect("/webserver")



@app.route("/reverseproxy")
def rp_list():
    response = requests.get("http://127.0.0.1:5000/config/reverseproxy")
    rps = response.json()
    return render_template("reverseproxy_list.html", rps=rps)


@app.route("/reverseproxy/<int:id>")
def rp_detail(id):
    response = requests.get(f"http://127.0.0.1:5000/config/reverseproxy/{id}")
    rp = response.json()
    return render_template("reverseproxy_detail.html", rp=rp)

@app.route("/reverseproxy/create", methods=["GET", "POST"])
def rp_create():
    if request.method == "POST":
        data = {
            "id": int(request.form["id"]),
            "name": request.form["name"],
            "ip_bind": request.form["ip_bind"],
            "target": request.form["target"]
        }

        requests.post("http://127.0.0.1:5000/config/reverseproxy", json=data)

        return redirect("/reverseproxy")

    return render_template("reverseproxy_create.html")

@app.route("/reverseproxy/delete/<int:id>")
def rp_delete(id):
    requests.delete(f"http://127.0.0.1:5000/config/reverseproxy/{id}")
    return redirect("/reverseproxy")

