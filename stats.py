def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

text = get_book_text("./books/frankenstein.txt")

def get_num_words():
    letter_list = text.split()
    letter_count = len(letter_list)

    print(f"{letter_count} words found in the document")

def get_num_char(string):
    char_counts = {}
    string = string.lower()
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

get_num_char(text)