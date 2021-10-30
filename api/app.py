import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>NLP API</h1><p>Here's your resume.</p>"

app.run()