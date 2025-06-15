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

def sort_on(dict):
    return dict["num"]

def sort_letters_dict(letters):
    sorted_letters = []
    for char in letters:
        if char.isalpha():
            sorted_letters.append({"char" : char, "num" : letters[char]})
    sorted_letters.sort(key=sort_on, reverse=True)
    return sorted_letters



        
        

