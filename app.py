
from flask import Flask, render_template, request
import iindex as ii

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method=="GET":
        return render_template('index.html')

    filename = request.form['file'].strip()
    term = request.form['term'].strip()
    try:
        headers = ii.getHeaders(filename)
        if "(AND)" in term:
            terms = term.split("(AND)")
            results = ii.ANDsearch(terms[0].strip().lower,terms[1].strip().lower(),filename)
            term = terms[0].strip() + " AND " + terms[1].strip()
        elif "(OR)" in term:
            terms = term.split("(OR)")
            results = ii.ORsearch(terms[0].strip().lower(),terms[1].strip().lower(),filename)
            term = terms[0].strip() + " OR " + terms[1].strip()
        else:
            results = ii.search(term.strip().lower(),filename)
        
        resultcount = len(results)
        return render_template('results.html',file = filename, term = term, results = results, headers = headers, count = resultcount)
    except IOError:
        return render_template('index.html', error = True, errorMessage = "Sorry, could not find file '" + filename + "'.")
    except KeyError:
        return render_template('index.html', error = True, errorMessage = "The search term '" + term + "' does not appear in this file.")
    except TypeError:
        return render_template('index.html', error = True, errorMessage = "This search combination yields no results. Try broadening your search.")



app.run(debug=True, host = '127.0.0.1', port = 5000)
