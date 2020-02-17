STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

with open('seneca_falls.txt', 'r') as f:
    data = f.read()
    # print(data)

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

no_punct = ""
for char in data:
    if char not in punctuation:
        no_punct = no_punct + char
# print(no_punct)

data_lower = no_punct.lower()
# print(data_lower)

data_split = data_lower.split(" ")
# print(data_split)

no_stop_words = []
for word in data_split:
    if word not in STOP_WORDS:
        no_stop_words.append(word)
print(no_stop_words)



# def print_word_freq(file):
#     """Read in `file` and print out the frequency of words in that file."""
#     pass


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
