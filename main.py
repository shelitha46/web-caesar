from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True


form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                Background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <form action="/hello" method="post">
        <label for="Rotate">Rotate by:</label>
        <input id="Rotate" type="text" name="rot" />
        <textarea name="text"></textarea>
        <input type="submit" />

    </form>
    </body>
</htm>
"""



@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    form_value = request.form['rot']
    return '<h1>Hello, ' + rot + '</h1>'
app.run()
