from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET"])
def add_Get():
    return render_template("add.html")

@app.route("/",methods=["POST"])
def add_post():
    if request.method=="POST":
        one=request.form.get("Number1")
        two=request.form.get("Number2")
        print(one,two)
        if one.isnumeric() and two.isnumeric():
            addition=int(one)+int(two)
            return render_template("add.html",add=addition)
        else:
            alert="invalid user input"
            return render_template("add.html",alert=alert)

if __name__ == "__main__":
    app.run(debug=True,port=5050)


