from flask import Flask,redirect

app=Flask(__name__)

@app.route("/about-me")
def index():
    return "Name: Đào Chí Tường. Age: 15. Hobbies: Almost none."
@app.route("/school")
def redirekt():
    return redirect("http://techkids.vn") 

if __name__ == "__main__":
    app.run(debug=True)
