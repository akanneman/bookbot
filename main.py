def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
    return text

def word_count(book_text):
    return len(book_text.split())

def count_letters(book_text):
    letter_count = 0
    for char in book_text:
        if char.isalpha():
            letter_count += 1
    return letter_count

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)

    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

    num_letters = count_letters(book_text)
    print(f"{num_letters} letters found in the document")

if __name__ == "__main__":
    main()

    