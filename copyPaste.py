from pyperclip import paste,copy
from flask import Flask, request, jsonify
from json import loads


app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def CopyPaste():
	if request.method == 'POST':
		clipboardText = copy(loads(request.data.decode("utf-8"))["1"])
		return jsonify(clipboardText)
	if request.method == 'GET':
		clipboardText = paste()
		return jsonify(clipboardText)

if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)

