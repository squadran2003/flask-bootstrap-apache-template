from flask import Flask,request,render_template,redirect

app = Flask(__name__)


@app.route('/')
def index():
	message = "This is a flask bootstrap apache2 starter template"
	return render_template("home.html",message=message)


if __name__=="__main__":
	app.run(debug=True,host='0.0.0.0',port=8000)