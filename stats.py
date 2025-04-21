def get_book_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        book_text = f.read()
    return book_text

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    count_dic = {}
    for char in text.lower():
        if char.isalpha():
            count_dic[char] = count_dic.get(char, 0) + 1
    return count_dic

def sorted_count_character(dictionary: dict) -> list:
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)