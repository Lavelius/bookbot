def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_letters(book_text):
    letters = {}
    fixedText = book_text.lower()
    for char in fixedText:
        if char not in letters:
            letters[char] = 0
        letters[char] += 1
    return letters
