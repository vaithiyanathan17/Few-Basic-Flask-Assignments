from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def loginPage():
    alert = ""
    if request.method == "POST":
        user = request.form.get("USERNAME")
        psd = request.form.get("PASSWORD")
        if user == "" or psd == "":
            alert = "provide valid credentials"
            return render_template("reg_form.html", alert=alert)
        elif user != "" or psd != "":
            return redirect(url_for("next_page",usr=user))
    return render_template("reg_form.html", alert=alert)


@app.route("/next_page <usr>",methods=["GET"])
def next_page(usr):
        print(usr)
        return render_template("next_page.html",usr=usr)





if __name__== "__main__":
    app.run(debug=True)