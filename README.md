# CS127 Final Project 

####   Boubacar Diallo and Christopher Longueira

## MVP 
A flask web app which uses an inverted index, and allows users to submit AND/OR/NOT queries on data through a form. The inverted index will also contain number of occurences.

## Extensions
(Aiming for half of these)
- [ ] Allow users to submit files that contain data to be queried
- [ ] Use the python [Natural Language Toolkit](http://www.nltk.org/) on data from file that is submitted.
      Analyze sentiment to show user context of the words they searched in each appearance
- [ ] Implement stemming and allow regex in searches 
- [ ] Experiment with n-grams for the inverted index

## How to use inverted index code
Using the function build_inverted_index, you must use three parameters: 
- [ ] filename - the name of the file you would like to create an index for
- [ ] keyindex - the value of the inverted index
- [ ] textindex - the key of the inverted index

The result is a list of the file names as an inverted index.

Using the function search_dict, you must use four parameters:
- [ ] str - the value you are searching for within the file
- [ ] filename - the name of the file you would like to create an index for
- [ ] keyindex - the value of the inverted index
- [ ] textindex - the key of the inverted index

The result is a list of the file names that include the string that is being searched for.

Using the function count_results, you must use four parameters:
- [ ] str - the value you are searching for within the file
- [ ] filename - the name of the file you would like to create an index for
- [ ] keyindex - the value of the inverted index
- [ ] textindex - the key of the inverted index

The result is a tuple of the given string and the number of occurrences within the files the given string is included in.

Using the function searchcount, you must use four parameters:
- [ ] str - the value you are searching for within the file
- [ ] filename - the name of the file you would like to create an index for
- [ ] keyindex - the value of the inverted index
- [ ] textindex - the key of the inverted index

The result is a tuple of the given string, the list of file names that included the given string, and the number of occurrences of the given string within these files.




