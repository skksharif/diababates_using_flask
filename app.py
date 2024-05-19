from flask import Flask,render_template,request
import pickle
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        FS=request.form['FS']
        FU=request.form['FU']
        model=pickle.load(open("my_model","rb"))
        prediction=model.predict([[int(FS),int(FU)]])
        if prediction[0]=="YES":
            return render_template("index.html",data=["Sorry you have diabetes","red"])
        else:
            return render_template("index.html",data=["Congratulations you don't have diabetes","green"])
    else:
        return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html",data=[1,2,3,4])

@app.route("/profile/<int:name>")
def myname(name):
    return str(4+int(name))

if __name__ == "__main__":
    app.run(debug=True)