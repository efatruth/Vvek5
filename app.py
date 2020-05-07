import os,pyrebase
from flask import Flask, render_template, session, url_for, request, redirect, escape 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'covid_19'

# tengin við firebase realtime database á firebase.google.com ( db hjá danielsimongalvez@gmail.com )
config = {
    # hér kemur tengingin þín við Firebase gagnagrunninn ( realtime database )
    "apiKey": "AIzaSyCmra7ssC9AkRKVVgkJ6EF9kf524kXUgDM",
    "authDomain": "verkefni5-6a651.firebaseapp.com",
    "databaseURL": "https://verkefni5-6a651.firebaseio.com",
    "projectId": "verkefni5-6a651",
    "storageBucket": "verkefni5-6a651.appspot.com",
    "messagingSenderId": "678266971689",
    "appId": "1:678266971689:web:3cb07445bd7c52a5899e38",
    "measurementId": "G-H0PT7R8SBT"
}

fb = pyrebase.initialize_app(config)
db = fb.database()
#auth = fb.auth() 

##email = input('Please enter your email\n')
#email = input('Please enter your email\n')
##password = input('Please enter your password\n')
#password = input('Please enter your password\n')

##user = auth.create_user_with_email_and_password(email, password)
#user = auth.sign_in_with_email_and_password(email, password)
#auth.send_email_verification(user['idToken'])
##print(auth.get_account_info(user['idToken']))


# Test route til að setja gögn í db
@app.route('/')
def index():
    #db.child("notandi").push({"notendanafn":"htg", "lykilorð":4321}) 
    return render_template("index.html")
                                                                                                                                                  
# Test route til að sækja öll gögn úr db
@app.route('/login',  methods=['GET','POST'])
def login():
    
    if request.method == 'POST': 

        usr = request.form['uname']
        pwd = request.form['psw']

        db.child("notandi").push({"notendanafn":usr,"lykilord":pwd}) 
        #return "Gögn er komin í gagnagrunn"
        return render_template("topsecret.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/doregister',  methods=['GET','POST'])
def doregister():
    
    if request.method == 'POST':

        usr = request.form['uname']
        pwd = request.form['psw']

<<<<<<< HEAD
        db.child("notandi").push({"notendanafn":usr,"lykilord":pwd}) 
        #return "Gögn er komin í gagnagrunn"
        return render_template("registered.html")
=======
        # fórum í grúnn og athugum hvort notendanafn sé til í grunni
        u = db.child("user").get().val()
        lst = list(u.items())
        for i in lst:
            usernames.append(i[1]['usr'])

        if usr not in usernames:
            db.child("user").push({"usr":usr, "pwd":pwd}) #Bætir við nýjum notanda 
            return render_template("registered.html")
        else:
            # ef notendanafn er til í grunninum nú þegar, viljum ekki hafa sama
            return render_template("userexists.html")
    else:
        return render_template("no_method.html")
>>>>>>> dd2328a7445a001e3b840cb3db72da4c485d15ba

        

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
