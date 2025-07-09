#HEADER AND FOOTER

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)

book = sys.argv[1]

from stats import get_book_text, wordcount, character_frequency, s_char_freq
text = get_book_text(book)
print(f'''============ BOOKBOT ============
Analyzing book found at {book}
----------- Word Count ----------''')
print(wordcount(text))
print("--------- Character Count -------")
final = character_frequency(text)
char_list = s_char_freq(final)
for character_dictionary in char_list:
    print(f"{character_dictionary["char"]}: {character_dictionary["num"]}")
print("============= END ===============")
