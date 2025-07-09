#HEADER AND FOOTER
book = "/home/jkarra/Bootdev/bookbot/books/frankenstein.txt"

from stats import get_book_text, wordcount, character_frequency, s_char_freq
text = get_book_text(book)
print('''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------''')
print(wordcount(text))
print("--------- Character Count -------")
final = character_frequency(text)
char_list = s_char_freq(final)
for character_dictionary in char_list:
    print(f"{character_dictionary["char"]}: {character_dictionary["num"]}")
print("============= END ===============")
