
from flask import Flask, render_template, request
import iindex as ii

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method=="GET":
        return render_template('index.html')

    filename = request.form['file']
    term = request.form['term']
    try:
        results = ii.search(term,filename)
        resultcount = len(results)
        headers = ii.getHeaders(filename)
        return render_template('results.html',file = filename, term = term, results = results, headers = headers, count = resultcount)
    except IOError:
        return render_template('index.html', error = True, errorMessage = "Sorry, could not find file '" + filename + "'.")
    except KeyError:
        return render_template('index.html', error = True, errorMessage = "The search term '" + term + "' does not appear in this file.")



app.run(debug=True, host = '127.0.0.1', port = 5000)
