from flask import Flask
from markupsafe import escape #Helps against HTML Injection attacks

app = Flask(__name__) #Required, tells flask where to look for templates and files needed, and creates an instance of the class

@app.route("/<name>") #Tells Flask which URL should trigger our function
def hello_world(name):  #Name catches a value from the URL
    return "<p>Hello, {escape(name)}</p>" #escape helps if a user were to change the name value to a command via inspect element, it will render as a text and not a command
