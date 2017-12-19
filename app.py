
from flask import Flask, render_template, request
import iindex as ii

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method=="GET":
        return render_template('index.html')
    filename = request.form['file']
    term = request.form['term']
    print(ii.build_inverted_index(filename,0,8))
    return render_template('index.html')


app.run(debug=True, host = '127.0.0.1', port = 5000)
