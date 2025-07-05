#FUNCTION HOLDING AREA

#GET BOOK TEXT FUNCTION

book = "/home/jkarra/Bootdev/bookbot/books/frankenstein.txt"

def get_book_text(book):
    with open(book) as t:
        text = t.read()
    return(text)

#GET WORDCOUNT FUNCTION

def wordcount():
    text = get_book_text(book)
    words = text.split()
    print(f"{len(words)} words found in the document")

wordcount()
