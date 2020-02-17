from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as f:
        data = f.read()
    # print(data)

    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    no_punct = ""
    for char in data:
        if char not in punctuation:
            no_punct = no_punct + char
    #print(no_punct)

    data_lower = no_punct.lower()
    # print(data_lower)

    data_split = data_lower.split(" ")
    # print(data_split)

    no_stop_words = []
    for word in data_split:
        if word not in STOP_WORDS:
            no_stop_words.append(word)
    # print(no_stop_words)

    def word_freq(no_stop_words):
        counts = {}

        for word in no_stop_words:
            if word in counts:
                counts[word] += 1
            else: 
                counts[word] = 1
        return counts  
    # print(word_freq(no_stop_words)) 

    my_string = word_freq(no_stop_words)

    for key, value in my_string.items():
        print(key, ' | ', value)      

    # counts = Counter(no_stop_words)
    # print(counts)
  


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
