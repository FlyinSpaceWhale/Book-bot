import sys
from stats import get_num_words, dict_report, frank_char, filepath, list_of_dict

if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
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