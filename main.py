def sort_on(dict):
    return dict["num"]

def count_words(s):
    return len(s.split())


def count_chars(s):
    chars = dict()

    for c in s:
        if not c.isalpha():
           continue
        char = c.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    char_list = list()
    for k, v in chars.items():
        char_list.append({"name": k, "num": v})

    return char_list


def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document\n")
        char_count = count_chars(file_contents)
        char_count.sort(reverse=True, key=sort_on)
        for char_info in char_count:
            print(f"The '{char_info["name"]}' character was found {char_info["num"]} times")
        print('--- End report ---')


if __name__ == '__main__':
    main()
