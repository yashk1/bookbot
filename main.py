from stats import *
import sys



if __name__ == "__main__":
    if len(sys.argv) <2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text_content = get_book_text(book_path)
    word_count = count_words(text_content)
    char_count_dic = count_characters(text_content)
    sorted_char_counts = sorted_count_character(char_count_dic)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for c, f in sorted_char_counts:
        print(f'{c}: {f}')

    print("============= END ===============")