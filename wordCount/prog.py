from collections import defaultdict
from operator import itemgetter

def word_count(lines):
    word_freq = defaultdict(int)
    total_words = 0
    for line in lines:
        words = line.split()
        total_words += len(words)  # Add the number of words in the current line to the total
        for word in words:
            word_freq[word] += 1
    return word_freq, total_words

def sort_word_freq(word_freq):
    sorted_word_freq = sorted(word_freq.items(), key=itemgetter(1), reverse=True)
    return sorted_word_freq

if __name__ == "__main__":
    filename = input("Enter the file name: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            word_freq, total_words = word_count(lines)
            sorted_word_freq = sort_word_freq(word_freq)
            print("Total number of words:", total_words)
            print("Word frequencies:")
            for word, freq in sorted_word_freq:
                print(f"{word}: {freq}")
    except FileNotFoundError:
        print("File not found.")
