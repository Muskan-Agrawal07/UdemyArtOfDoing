from collections import Counter
print("Welcome to the Frequency Analysis Program.\n")
non_letters=['1','2','3','4','5','6','7','8','9','0',' ','.','?',',','"',"'",':',';','(',')','@','!','#','$','%','&','*','*','\n','\t']

key_phrase_1=str(input("Enter a word or phrase to count the occurence of each letter.:")).lower().strip()

for non_letter in non_letters:
    key_phrase_1=key_phrase_1.replace(non_letter,'')
total_occurences=len(key_phrase_1)
letter_count=Counter(key_phrase_1)
print("\nHere is the frequency analysis of each letter:\n")
print("\n\tLetter\t\tOccurrence\tPercentage")
for k,v in sorted(letter_count.items()):
    percentage=100*v/total_occurences
    percentage=round(percentage,2)
    print("\t",k,"\t\t",v,"\t\t",percentage,"%")
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters=[]
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])
print("\nLetters in descending orders of occurence are:")
for i in key_phrase_1_ordered_letters:
    print(i,end="")


key_phrase_2=str(input("\n\nEnter a word or phrase to count the occurence of each letter.:")).lower().strip()

for non_letter in non_letters:
    key_phrase_2=key_phrase_2.replace(non_letter,'')
total_occurences_2=len(key_phrase_2)
letter_count_2=Counter(key_phrase_2)
print("\nHere is the frequency analysis of each letter:\n")
print("\n\tLetter\t\tOccurrence\tPercentage")
for k,v in sorted(letter_count_2.items()):
    percentage_2=100*v/total_occurences
    percentage_2=round(percentage_2,2)
    print("\t",k,"\t\t",v,"\t\t",percentage_2,"%")
ordered_letter_count_2 = letter_count_2.most_common()
key_phrase_2_ordered_letters=[]
for pair in ordered_letter_count_2:
    key_phrase_2_ordered_letters.append(pair[0])
print("\nLetters in descending orders of occurence are:")
for i in key_phrase_2_ordered_letters:
    print(i,end="")
