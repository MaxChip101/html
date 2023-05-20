from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the message from the request
        message = request.form['message']

        # Append the message to the file
        with open('messages.txt', 'a') as file:
            file.write(message + '\n')

    return render_template('index.html')

if __name__ == '__chat__':
    app.run()
