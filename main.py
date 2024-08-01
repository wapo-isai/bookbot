def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = word_count(file_contents)
        chars_dict = char_count(file_contents)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document")
        print()
        
        for item in chars_sorted_list:
            if not item["char"].isalpha():
                continue
            print(f"The '{item['char']}' character was found {item['num']} times")
        
        print("--- End report ---")

def word_count(file_contents):
    words = file_contents.split()
    words_len = len(words)

    char_count(words)
    return words_len

def char_count(text):
    char_count_dict = {}
    
    for char in text:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] = char_count_dict[char] + 1
        else:
            char_count_dict[char] = 1

    return char_count_dict
    
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main();