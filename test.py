sample = "Here's some sample text. It's got different kinds of punctuation! And also multiple sentences... Seems pretty neat I guess."

print(sample)

sample.translate(None, sample.punctuation)

print(sample)