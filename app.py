import os, pyrebase
from flask import Flask, render_template, session, url_for, request, redirect, escape 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'covid_19'

# tengin við firebase realtime database á firebase.google.com ( db hjá danielsimongalvez@gmail.com )
config = {
    # hér kemur tengingin þín við Firebase gagnagrunninn ( realtime database )

    "apiKey": "AIzaSyAoVR0f0cnvG6dfU2lAEhjooCr6TnU808o",
    "authDomain": "test-4d7b9.firebaseapp.com",
    "databaseURL": "https://test-4d7b9.firebaseio.com",
    "projectId": "test-4d7b9",
    "storageBucket": "test-4d7b9.appspot.com",
    "messagingSenderId": "1095693323000",
    "appId": "1:1095693323000:web:516e2d493b1cb977c6090d",
    "measurementId": "G-QF6GBDCX62"
}

fb = pyrebase.initialize_app(config)
db = fb.database()

# Test route til að setja gögn í db
@app.route('/')
def index():
    #db.child("notandi").push({"notendanafn":"htg", "lykilorð":4321}) 
    return render_template("index.html")

# Test route til að sækja öll gögn úr db
@app.route('/login',  methods=['GET','POST'])
def login():
    login = False
    if request.method == 'POST':

        usr = request.form['uname']
        pwd = request.form['psw']

        # sækja alla í gagnagrunninn og athugum hvort tiltekið notendanafn og lykilorð sé til
        u = db.child("user").get().val()
        lst = list(u.items())
        for i in lst:
            if usr == i[1]['usr'] and pwd == i[1]['pwd']:
                login = True
                break

        if login:
            # hefur aðgang
            session['logged_in'] = usr
            return redirect("/topsecret")
        else:
            #hefur ekii aðgang
            return render_template("nologin.html")
    else:
        return render_template("no_method.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/doregister',  methods=['GET','POST'])
def doregister():
    usernames = []
    if request.method == 'POST':

        usr = request.form['uname']
        pwd = request.form['psw']

        # fórum í grúnn og athugum hvort notendanafn sé til í grunni
        u = db.child("user").get().val()
        lst = list(u.items())
        for i in lst:
            usernames.append(i[1]['usr'])

        if usr not in usernames:
            db.child("user").push({"usr":"usr", "pwd":pwd}) #Bætir við nýjum notanda 
            return render_template("registered.html")
        else:
            # ef notendanafn er til í grunninum nú þegar, viljum ekki hafa sama
            return render_template("userexists.html")
    else:
        return render_template("no_method.html")


@app.route('/logout')
def logout():
    session.pop("logged_in", None)
    return render_template("index.html")       


@app.route('/topsecret')
def topsecret():
    if 'logged_in' in session:
        return render_template("topsecret.html")
    else:
        return redirect("/")


@app.errorhandler(404)
def page_not_found(error):
    return "Ekki til"



if __name__ == "__main__":
	app.run(debug=True)

# skrifum nýjan í grunn hnútur sem heitir notandi 
# db.child("notandi").push({"notendanafn":"dsg", "lykilorð":1234}) 

# # förum í grunn og sækjum allar raðir ( öll gögn )
# u = db.child("notandi").get().val()
# lst = list(u.items())