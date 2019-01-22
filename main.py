from flask import Flask

app = Flas(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "Hello World"


    app.run()