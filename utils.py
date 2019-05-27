# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script



def word_count(cl:list):
    """
    counts how often a word exist (add everytime plus 1) and if there ist only one word it sets the count on one.
    """
    cars={}
    for i in cl:
        if i in cars.keys():
            cars[i] += 1
        else:
            cars[i]=1
    return cars



