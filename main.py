def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

        print("--- Begin report of books/frankenstein.txt ---")

        #print(file_contents)
        words(file_contents)
        
        print()
        
        charcount(file_contents)

        print("--- End report ---")

def words(text):
    word_count = 0

    for word in text.split():
        word_count += 1

    print(f"{word_count} words found in the document")

def charcount(text):
    char_count = {}

    for char in text:
        lchar = char.lower()

        if lchar in char_count:
            char_count[lchar] += 1
        else:
            char_count.setdefault(lchar, 1)

    for key in char_count:
        code = ord(key)

        if code >= 97 and code <= 122:
            print(f"The '{key}' character was found {char_count[key]} times")

main()