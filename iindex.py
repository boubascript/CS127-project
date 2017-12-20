import csv

def getHeaders(file):
    reader = csv.reader(open("data/" + file))
    return next(reader)
  
def general_iindex(file):
    csv_reader = csv.reader(open("data/" + file))
    d = {}
    for row in csv_reader:
        for col in row:
            for word in col.split(" "):
                d.setdefault(word.lower(),[])
                if row not in d[word.lower()]:
                    d[word.lower()].append(row)
    return d

def search(term,file):
    return general_iindex(file)[term]

def ANDsearch(term1,term2,file):
    results = []
    for result in general_iindex(file)[term1]:
        for phrase in result:
            if term2 in phrase.split(" "):
                results.append(result)
    return results 

def ORsearch(term1,term2,file):
    results = general_iindex(file)[term1]
    results.extend(general_iindex(file)[term2])
    return results

def build_inverted_index(filename,keyindex,textindex):
    csv_reader = csv.reader(open("data/" + filename))
    d={}
    for line in csv_reader:
        document = line[keyindex]
        textstring = line[textindex]
        print(textstring)
        # cleantext = "".join([x if x.isalpha() else ' ' for x in s ])
        cleantext = ""
        for letter in textstring:
            if letter.isalpha():
                cleantext = cleantext + letter
            else:
                cleantext = cleantext + " "
        wordlist = cleantext.split()
        for word in wordlist:
            d.setdefault(word.lower(),[])
            d[word.lower()].append(document)
    return d

def search_dict(str, filename, keyindex, textindex):
    dict = build_inverted_index(filename, keyindex, textindex)
    l = []
    str = str.lower()
    for x in dict.keys():
        if str in x:
            l += dict[x]
    return l

def count_results(str, filename, keyindex, textindex):
    count = 0
    for x in range(len(search_dict(str, filename, keyindex, textindex))):
        count += 1
    return [str, count]

def searchcount(str, filename, keyindex, textindex):
    count = 0
    for x in range(len(search_dict(str, filename, keyindex, textindex))):
        count += 1
    return [str, search_dict(str, filename, keyindex, textindex), count]

#print(ORsearch("sorry","happy",'offenders.csv'))
#new_iindex('example.csv',0,3)
#print(search_dict('sorry', 'data/offenders-clean.csv', 0 , 8)) #- test case
##print(searchcount('triple', './CSVfiles/awardsplayers.csv', 0, 1))
##print(searchcount('Pitching', './CSVfiles/awardsplayers.csv', 0, 1))
##print(searchcount('Buffalo', './CSVfiles/teamsfranchises.csv', 0, 1))
##print(searchcount('New', './CSVfiles/teamsfranchises.csv', 0, 1))