from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Takanolab!"

@app.route("/hello",
  methods=["GET"],
  endpoint="hello-endpoint")
def hello():
    return "Hello, KAIT!"

@app.route("/sentiment",
  methods=["GET"],
  endpoint="sentiment")
def sentimet():
  #return "sentiment"
  return render_template("index_py.html")

@app.route("/sentiment_do",
  methods=["GET"],
  endpoint="sentiment_do")
def sentiment_do():
  # GETのときはrequest.args.getを使う
  message = request.args.get('usermsg')
  # return message
  return render_template("result.html", message=message)