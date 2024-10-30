#Given a sentence S, write a program to print the sentence by replacing 
# the first letter of every word with its next letter based on its Unicode value


#First define a function withe an arg sentance.
def replace_first_words(sentance):
    #.split() it splits the sentence into list eg:['East' , 'Best]
    words = sentance.split()
    #used to store the modified word.
    modefied_words = []
    #for loop to reach each wor in list words['east', 'best' , 'note']
    for word in words:
        #if word checks the word is empty or not before modefing 
        if word:
            first_letter = word[0]
            #ord() is used check the unicode value of the specified value
            #chr() convers the unicode to character.
            
            next_word = chr(ord(first_letter)+1) 
            #combines next_word with other letters in the word
            modefied_word = next_word + word[1:]
            #combile modified_words with modefid_words
            modefied_words.append(modefied_word)
    #combine all word to form an sentance
    modefied_sentance = ' '.join(modefied_words)
    
    return modefied_sentance
#take input from user
sentance = input("Enter Sentance: ")
#function call
result  = replace_first_words(sentance)
print(result)
        
        
        