app = Flask(__name__)
  
@app.route("/")
def hello():
    return "Hello Geeks!! from Google Colab"
  
if __name__ == '__main__':
    app.run()