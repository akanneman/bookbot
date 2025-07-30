from stats import word_count, count_letters, character_count

def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
    return text

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)

    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

    num_letters = count_letters(book_text)
    print(f"{num_letters} letters found in the document")

    char_freq = character_count(book_text)
    for char in sorted(char_freq.keys()):
        print(f"'{char}': {char_freq[char]}")

if __name__ == "__main__":
    main()


    