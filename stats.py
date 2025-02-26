def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append((char, count))
    return sorted(char_list, key=lambda x: x[1], reverse=True)