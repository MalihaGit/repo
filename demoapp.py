from flask import Flask
app=Flask(__name__)
@app.route("/")
def greetings():
  return "Hello this is Maliha & i love stranger things"
if __name__=="__main__":
  app.run("0.0.0.0")