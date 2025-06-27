import math

# takes in a vector of logits
# outputs the predicted probability distribution
def softmax(logits):
    max_logit = max(logits)
    
    sum_logits = 0
    
    normalized_logits = []
    probability_distribution = []
    
    for j in range(len(logits)):
        normalized_logits.append(logits[j]-max_logit)
        sum_logits += math.exp(logits[j]-max_logit)
    
    
    for i in range(len(logits)):
        
        softmax_logit = round(math.exp(normalized_logits[i]) /sum_logits, 3)
        probability_distribution.append(softmax_logit)
    
    return probability_distribution


def loss_function(true_distribution, predicted_distribution):
    cross_entropy = 0
    
    for i in range(len(true_distribution)):
        cross_entropy += ( true_distribution[i] * math.log(predicted_distribution[i]) ) * -1
        
    return cross_entropy    
    
    