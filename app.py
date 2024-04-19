from flask import Flask, render_template, request, redirect, url_for # type: ignore
import base64
import os
from dotenv import load_dotenv # type: ignore

app = Flask(__name__,template_folder='template')
app.data = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secret', methods=['POST'])
def secret():
    if request.method == 'POST':
        decoded_data = base64.b64decode(app.data)
        print(decoded_data)
        secret_key = request.form['secret']
        print(f"Received secret key: {secret_key}")
        if decoded_data.decode('utf-8') == secret_key:
            return render_template("winner.html")
        else:
            return render_template("index.html")
if __name__ == '__main__':
    with open('../static/') as file:
        app.data = file.read()
    app.run(debug=False)
