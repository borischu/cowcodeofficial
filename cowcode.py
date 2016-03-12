from flask import Flask, render_template, session, redirect, request, url_for
import os 

app = Flask(__name__)

###ROUTING###
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

    #this is a test