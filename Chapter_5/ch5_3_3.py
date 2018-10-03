from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello Napier"

#@app.route('/force404')
#def force404():
#	abort(404)

@app.route('/force400')
def force400():
	abort (400)

#@app.errorhandler(404)
#def page_not_found(error):
#	return "Couldn't find the page you requested.", 404

@app.errorhandler(400)
def page_not_found(error):
	return "This is error 400.", 400

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
