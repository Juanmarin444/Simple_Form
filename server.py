from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():

   print("Got Post Info")
   print(request.form)

   first_name = request.form['first_name']

   print(first_name)
   
   return render_template('/index.html', name=first_name)

app.run(debug=True)
