
from flask import Flask, render_template, request, session
from flask_session import Session
# from data import nem

app = Flask(__name__)
app.config["SESSION_PERMANENT"] == False
app.config["SESSION_TYPE"] == "filesystem"
Session(app)

# names=nem()

@app.route('/', methods=['POST','GET'])
def index():
	if session.get("names") == None:
		session["names"] = []
	if request.method == 'POST':
		name = request.form.get('name')
		if len(name) > 0:
			session["names"].append(name)
		return  render_template('index.html', author="The Department", names=session["names"])
	else:
		return  render_template('index.html', author="The Department", names=session["names"])		

@app.route('/queens')
def queens():
    return  render_template('queens.html')

@app.route('/hello', methods=["POST"])
def hello():
	name = request.form.get('name')
	return  render_template('hullo.html', name=name)
