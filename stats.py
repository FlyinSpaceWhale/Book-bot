def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

filepath = "books/frankenstein.txt"
text = get_book_text(filepath)

def get_num_words():
    letter_list = text.split()
    letter_count = len(letter_list)

    print(f"Found {letter_count} total words")

def get_num_char(string):
    char_counts = {}
    string = string.lower()
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

frank_char = get_num_char(text)


def sort_on(char):
    return char["num"]

list_of_dict = []

def dict_report(dict):
    for i in dict:
        list_of_dict.append({"char":i, "num":dict[i]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

dict_report(frank_char)