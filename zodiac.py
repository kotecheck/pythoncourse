import random

first = [1,2,3,4,5]
second = ['h','g','j','o','p']
third = ['A','B','C','D','E']
 
zods = [ 'Овен','Козерог']
    
def get_prediction():
    return f'{random.choice(first)} {random.choice(second)} {random.choice(third)}'
