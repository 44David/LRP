data = open("data.txt", "r")

entries = data.readlines()
vocabulary = {}
index = 0

for entry in entries:
    entry = entry.replace('->', 'IMPLIES').split()
    for token in entry:
        if token not in vocabulary:
            vocabulary[token] = index
            index += 1


def tokenize_entry(text):
    text = text.replace("->", "IMPLIES")
    tokens = text.split()
    return [vocabulary[token] for token in tokens]

def prepare_training_data(tokens):
    implies = tokens.index(vocabulary["IMPLIES"])
    
    premise = tokens[:implies]
    conclusion = tokens[implies+1:]


    
    return premise, conclusion
    