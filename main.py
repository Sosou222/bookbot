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
    print("hello world")\

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        count = get_word_count(file_contents)
        print(f"Word  count:{count}")
        words = get_letter_count(file_contents)
        print(f"{words}")
main()