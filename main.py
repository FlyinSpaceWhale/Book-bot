from stats import get_book_text, get_num_words, get_num_char, text, dict_report, frank_char, filepath, list_of_dict

def main():
    char_count = get_num_char(text)
    dict_report(frank_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    get_num_words()
    print("--------- Character Count -------")

    for i in list_of_dict:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
   
    print("============= END ===============")
    
# if __name__ is used to avoid accidental calls of main() 
if __name__ == "__main__":
    main()