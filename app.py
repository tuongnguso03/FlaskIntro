#creatingFlaskApp
from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello there."

@app.route("/about+me+the+bad+guy")
def index_2():
    n={
    "name" : "Đào Chí Tường.",
    "Ing": "TOC N2O. "   ,
    "Playstyle": "Singed main."
    }
    k=""
    for i in n:
        k+=i
        k+=":"
        k+=n[i]
        k+="<br/>"
    return k

@app.route("/hello/<name>")
def hello_tu(name):
    return "Em chào anh (chị) {0}".format(name)    

#running
if __name__ == "__main__":
    app.run()
