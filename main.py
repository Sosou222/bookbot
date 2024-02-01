def get_word_count(text):
    out = text.split()
    return len(out)

def get_letter_count(text):
    out = {}
    text = text.lower()
    for w in text:
        if w in out:
            out[w] += 1
        else:
            out[w] = 1
    return out

def main():
    #print("hello world")\
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        count = get_word_count(file_contents)
        print(f"Word  count:{count}")
        print("")
        words = get_letter_count(file_contents)
        #print(f"{words}")
        l = list(words.items())
        sorted_words = sorted(l,key=lambda x:x[1],reverse = True)
        for w in sorted_words:
            if w[0].isalpha():
                print(f"The '{w[0]}' character was found {w[1]} times")
    print("--- End report ---")
main()