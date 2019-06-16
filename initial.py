test_data = """White tigers live mostly in India
               Wild lions live mostly in Africa"""
stop_words = set(['in', 'the', 'and', 'for']) # etc etc
term_frequency_hash = {}
def add_tf(word):
    if word in stop_words:
        return
    if word in term_frequency_hash:
        term_frequency_hash[word] += 1
    else:
        term_frequency_hash[word] = 1
        
words = test_data.split()
map(add_tf, words)
term_frequency_list = []
for key, value in term_frequency_hash.items():
    term_frequency_list.append((key, value))

print sorted(term_frequency_list, key=lambda t: t[1], reverse=True)
