import string

test_data = """White tigers live mostly in India
               Wild lions live mostly in Africa""".split()
with open('stop_words.txt', 'r') as file:
    stop_words = set(file.read().split(','))

def process_file(fname):
    with open(fname) as file:
        s = file.read()
        # Convert punctuation into spaces
        trans_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        return s.translate(trans_table).split()

def compute_tf(words):
    term_frequency_hash = {}

    def add_tf(word):
        word = word.lower()
        if word in stop_words:
            return
        if word in term_frequency_hash:
            term_frequency_hash[word] += 1
        else:
            term_frequency_hash[word] = 1

    for word in words:
        add_tf(word)
    term_frequency_list = []
    for key, value in term_frequency_hash.items():
        term_frequency_list.append((key, value))
    print(sorted(term_frequency_list, key=lambda t: t[1], reverse=True))
    
compute_tf(test_data)
compute_tf(process_file("pride-and-prejudice.txt"))
