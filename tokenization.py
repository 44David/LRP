import spacy 

def tokenize_data_entry():
    
    nlp = spacy.load("en_core_web_sm")
    
    data = open("data.txt", "r")
    
    entries = data.readlines()
    
    
    tokenized_data = []
    for entry in entries:
        if entry.strip():
            entry = entry.split('->')
            entry[1] = entry[1].strip("\n")
            
            question = nlp(entry[0])
            answer = nlp(entry[1])
            
                  
            question_tokens = []
            for token in question:
                question_tokens.append(token.idx)
            
            answer_tokens = []
            for token in answer:
                answer_tokens.append(token.idx)

            tokenized_pair = []
            tokenized_pair.append(question_tokens)
            tokenized_pair.append(answer_tokens)
            
            tokenized_data.append(tokenized_pair)
    
    print(tokenized_data)
    return tokenized_data
        
tokenize_data_entry()