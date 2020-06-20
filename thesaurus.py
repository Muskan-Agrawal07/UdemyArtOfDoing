import random
print("Welcome to the Thesaurus!")
print("\nChoose a word from the thesaurus and I will give you a synonym.\n")
words={"hot":["warm","summery","boiling","scorching"],
       "cold":["chilly","cool","freezing","frigid"],
    "happy":["glad","merry","content","joyous"],
       "sad":["gloomy","unhappy","melancholic","downcast"]}
print("Here are the words in the thesaurus:")
for k in words.keys():
 print("\t",k)
word=str(input("What word would you like a synonym for?")).lower().strip()
if word in words.keys():
 index=random.randint(0,4) 
 print("A synonym for",word,"is",words[word][index])
else:
    print(word ,"is not in the given thesaurus")
choice=str(input("Would you like to see the entire thesaurus?(y/n)")).lower()

if choice=="y":
 for key,values in words.items():
     print("Synonyms of",key,"are:")
     for value in values:
      print("\t",value)

else:
    print("okay!")
