from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{{
                Background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form action="/hello" method="post">
        <label for="Rotate">Rotate by:</label>
        <input name="Rotate" type="text" value'{0}' />
        <textarea name="text">{0}</textarea>
        <input type="submit" />

    </form>
    </body>
</htm>
"""



@app.route("/")
def index():
    return form.format(...)

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rotate_string = encrypt.form['text']
    return form.format(...)



app.run()
