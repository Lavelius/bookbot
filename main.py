from stats import get_num_words
from stats import get_letters
from stats import sort_letters_dict
import sys

#this function read the book text from a file and returns it as a string.
def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
        return book_text
    
    #This function runs the program that should count the number of words and letters in a book.
def main():
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(file_path)
    amount = get_num_words(text)
    letters = get_letters(text)
    sorted_letters = sort_letters_dict(letters)
    print(f"Found {amount} total words")
    for letter in sorted_letters:
        print(f"{letter['char']}: {letter['num']}")
    




main()
