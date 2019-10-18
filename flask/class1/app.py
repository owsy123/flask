from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')



@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/home')
def home1():
    return 'hello user'

@app.route('/page1')
def page1():
    return 'incorrect'

@app.route("/auth",methods=['POST'])
def auth():
    data = request.form
    if data['username'] == 'owais' and data['password'] == '12345':
        return redirect ('/home')
    else:
        return redirect('/page1')











app.run(debug=True, port=8080)

