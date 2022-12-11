from flask import Flask, render_template, url_for, request
from markupsafe import escape
app = Flask(__name__)

in_string = " "

@app.route('/') #home url
def root():
    in_string = " "
    message = "Flask server is running"
    # return "hi"
    return render_template("index.html",message=message)
    
    
@app.route("/", methods=['GET', 'POST'])
def index():
    print("In index")
    if request.method == 'POST':
        print("In POST")
        in_string = request.form.get("text_1")
        # print(in_string) 
        l = in_string.split()
        k = []
        for i in l:
            if ((in_string.count(i)>= 1) and (i not in k)):
                k.append(i)
        name = k
        return render_template('index.html', namexx=name)
    elif request.method == 'GET':
        print("In GET")
        return render_template('index.html', form=form)

    return render_template('index.html')

