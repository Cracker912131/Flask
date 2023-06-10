
from flask import Flask
import os,sys

app = Flask(__name__)

@app.route('/')

def hello_world():
	os.system("ls >> h.txt")
    x=open("h.txt","r").read()
    return 'Hello, World!'+x

if __name__ == '__main__':

    app.run()
