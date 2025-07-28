def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def get_num_words():
    letter_list = get_book_text("./books/frankenstein.txt").split()
    letter_count = len(letter_list)

    print(f"{letter_count} words found in the document")

