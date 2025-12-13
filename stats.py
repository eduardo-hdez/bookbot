
def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    seen = {}
    for character in text:
        lowered = character.lower()
        if lowered == " ":
            continue
        elif lowered in seen:
            seen[lowered] += 1
        else:
            seen[lowered] = 1
    return seen


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list