from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def grade():
    if request.method == "POST":
        name = request.form.get("NAME")
        Class = request.form.get("CLASS")
        mark = request.form.get("MARK")
        grade = request.form.get("GRADE")
        print(name,Class,mark,grade)
    return render_template("grade.html")





if __name__ == '__main__':
    app.run(debug=True,port=5555)