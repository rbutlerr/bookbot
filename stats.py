def count_words(book_text):
    word_list = book_text.split()
    counter = len(word_list)
    return counter

def count_letters(book_text):
    lowercase = book_text.lower()
    letter_counts = {}
    for letter in lowercase:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else: 
            letter_counts[letter] = 1

    return letter_counts

def sort_dicts(letter_counts):
    letter_dicts = []
    for char in letter_counts:
        one_char = {
            "char": char,
            "num": letter_counts[char]
            }
        letter_dicts.append(one_char)

    def sort_on(items):
        return items["num"]

    letter_dicts.sort(reverse=True, key=sort_on)
    return letter_dicts
