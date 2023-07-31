from flask import Flask, redirect, url_for, render_template, jsonify, request
import os

app = Flask(__name__)


@app.route("/")
def redirhome():
    return redirect(url_for("home"))


@app.route("/chat/")
def redirchat():
    return redirect("0")


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/chat/<id>")
def room(id):
    if os.path.exists("static/chatrooms/" + id + ".txt"):
        pass
    else:
        with open("static/chatrooms/" + id + ".txt", "w") as f:
            f.write("-- Start of chatroom: " + id + " --")

    return render_template("chat.html", roomid=id)


@app.route('/sendmsg', methods=['POST'])
def send_message():
    data = request.json
    msg = data.get('msg')
    room = data.get('room')
    name = data.get('name')

    # Somehow debugs the entire thing
    print("")

    # puts new text on the top of the file
    with open("static/chatrooms/" + str(room) + ".txt", "r") as f:
        prevmsgs = f.read()
        with open("static/chatrooms/" + str(room) + ".txt", "w") as file:
            file.write("[ @" + name + " ]: " + msg + "\n")

        with open("static/chatrooms/" + str(room) + ".txt", "a") as file:
            file.write(prevmsgs)

    return ''


@app.route('/chatroom', methods=['POST'])
def changeroom():
    roomid = request.form['room']
    return redirect("/chat/" + roomid)

@app.route('/username', methods=['POST'])
def changename():
    roomid = request.form['name']
    return redirect("/chat/" + roomid)


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=False, port=5000)
