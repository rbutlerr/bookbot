from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    letter_counts = count_letters(book_text)
    print(f"Found {word_count} total words")
    print(letter_counts)

main()
