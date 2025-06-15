from stats import get_num_words
from stats import get_letters
from stats import sort_letters_dict

#this function read the book text from a file and returns it as a string.
def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
        return book_text
    
    #This function runs the program that should count the number of words and letters in a book.
def main():
    text = get_book_text("books/frankenstein.txt")
    amount = get_num_words(text)
    letters = get_letters(text)
    sorted_letters = sort_letters_dict(letters)
    print(f"{amount} words found in the document")
    print(f"Letters found in the document: {sorted_letters}")
    




main()
