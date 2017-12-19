# CS127 Final Project 

####   Boubacar Diallo and Christopher Longueira

### Set Up
In the directory, preferably after having activated the directory with [virtualenv](https://virtualenv.pypa.io/en/stable/),run this command to download the packages needed.
``` 
pip install -r requirements.txt 
```
Then to launch the app, run 
```
python3 app.py
``` 
The site should be live at [127.0.0.1:5000](127.0.0.1:5000)

## MVP 
A flask web app which uses an inverted index, and allows users to submit simple AND/OR queries on data through a form. 

## Future Extensions
(Aiming for half of these)
- [ ] Allow users to submit files that contain data to be queried
- [ ] Use the python [Natural Language Toolkit](http://www.nltk.org/) on data from file that is submitted.
      Analyze sentiment to show user context of the words they searched in each appearance
- [ ] Implement stemming and allow regex in searches 
- [ ] Experiment with n-grams for the inverted index





