def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
        return book_text

def num_words(book_text):
    words = book_text.split()
    return len(words)
    
def main():
    text = get_book_text("books/frankenstein.txt")
    amount = num_words(text)
    print(f"{amount} words found in the document")


main()
