from flask import Flask, request 

app = Flask(__name__)

app.secret_key = 'My-secret-key'

@app.route("/")
def home():
    return """

    <html>
        <head>
        
            <title>Home Page </title>
    
        </head>
    
        <body>
        
        <form action = "/greet" method = "POST">
        
            Enter your name : <input type = "text" name = "username">
            <input type = "submit" value = "Submit">

        </body>
    
    </html>

"""

@app.route("/greet", methods = ['POST'])
def greet():
    user_input = request.form['username']
    return f"Hello {user_input}, welcome to our app."


