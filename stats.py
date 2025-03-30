def get_num_words(text):
    return (len(text.split()))

def char_count(text):
    char_dict = {}
    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sorted_char_count(dict_to_sort):
    list_dict = []
    for char, count in dict_to_sort.items():
        char_dict = {"char": char, "count": count}
        list_dict.append(char_dict)

    list_dict.sort(reverse=True,key=lambda d: d["count"])
    return list_dict
