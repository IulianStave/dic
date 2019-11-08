import mysql.connector
from difflib import get_close_matches

#we create an object that will allows us to connect to the database
con = mysql.connector.connect(
    user = 'ardit700_student',
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
#create a cursor using the cursor() method for the above connector object
cursor = con.cursor()

word = input ('Enter word: ')
word = word.lower()

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'"%word)
results = cursor.fetchall()
#print(results)

queryx = cursor.execute("SELECT * FROM Dictionary")
resultsxtended = cursor.fetchall()
list = [item[0] for item in resultsxtended ]
#print('words ',list)
#print(len(get_close_matches(word,list)))
'''
elif len(get_close_matches(word,list))>0:
 
    print('Did you mean %s '%get_close_matches(word,list)[0])
'''

if results:
    print("{} definitions found in dicitionary".format(len(results)))
    #list comprehension from a list of tuples [(word, def1), (word,def2), ...] to a list of definitions [def1, def2, ...]
    defs = [item[1] for item in results]
    print (defs)
    for result in results:
        print(str(results.index(result)+1)+':',word, '=', result[1])

else:
    dictionary = {key: value for key, value in resultsxtended}
    if len(get_close_matches(word,dictionary))>0:
        matches = get_close_matches(word,dictionary)
        print('Did you mean {} ? if so, please check the definitions below'.format(matches[0]))
        #print (len(matches),matches[0])
        results = dictionary[matches[0]]
        print(type(results))
        print(results)
        #print (dictionary.count('rain'))
    else:
        print("No word found")

#dic = {key: value for key, value in resultsxtended}
#matches = get_close_matches(word,dic)
#print (len(matches),matches[0])
