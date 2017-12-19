import csv

def build_inverted_index(filename,keyindex,textindex):
    csv_reader = csv.reader(open("data/" + filename))
    d={}
    for line in csv_reader:
        document = line[keyindex]
        textstring = line[textindex]
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


#print(build_inverted_index('data/example.csv',0,3))
#print(search_dict('sorry', 'data/offenders-clean.csv', 0 , 8)) #- test case
##print(searchcount('triple', './CSVfiles/awardsplayers.csv', 0, 1))
##print(searchcount('Pitching', './CSVfiles/awardsplayers.csv', 0, 1))
##print(searchcount('Buffalo', './CSVfiles/teamsfranchises.csv', 0, 1))
##print(searchcount('New', './CSVfiles/teamsfranchises.csv', 0, 1))