def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
    return text

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(text)

if __name__ == "__main__":
    main()
