def main():
    book_path = "books/frankenstein.txt.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count = get_count_characters(text)
    report = get_book_report(count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    print()
    for item in report:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character has been found {item["num"]} times")
    print("--- End Report ---")
    
    

def get_num_words(text):
    words = text.split()
    return len(words)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_characters(text):
    count_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in count_dict:
            count_dict[lowered] += 1
        else:
            count_dict[lowered] = 1
                
    return count_dict


def sort_on(d):
    return d["num"]


def get_book_report(count):
    sorted_list= []
    for ch in count:
        sorted_list.append({"char":ch,"num":count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()