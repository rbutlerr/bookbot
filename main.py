import sys

from stats import count_words, count_letters, sort_dicts 


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def check_args(sys_argv):
    if len(sys_argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys_argv[1]

def main():

    book_locale = check_args(sys.argv) 
    book_text = get_book_text(book_locale)
    word_count = count_words(book_text)
    letter_counts = count_letters(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_locale}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    chars_indiv = sort_dicts(letter_counts)
    for char in chars_indiv:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")



main()
