#SCRATCH PAPER DO NOT USE



#FUNCTION HOLDING AREA

#GET BOOK TEXT FUNCTION

book = "/home/jkarra/Bootdev/bookbot/books/frankenstein.txt"

def get_book_text(book):
    with open(book) as t:
        text = t.read()
    return(text)

#GET WORDCOUNT FUNCTION

def wordcount(text):
    words = text.split()
    return (f"{len(words)} words found in the document")

#COUNT LETTERS FUNCTION

def character_frequency(text):
    final = {}
    l_text = text.lower()
    characters = list(l_text)
    for char in characters:
        if char in final:
            final[char] += 1
        else:
            final[char] = 1

    return final

#COMPLETE REPORT FUNCTION

def s_char_freq(final):

    char_list = []

    for char, num in final.items():
        if char.isalpha():
            char_list.append( {"char":(char), "num":(num)} ) 
    
    def s_method(hold):
        return hold["num"]

    char_list.sort(key=s_method, reverse=True)
    return char_list
