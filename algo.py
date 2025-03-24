from collections import defaultdict as df_dict
def unique(array):
    seen = set()
    distincts = []

    for el in array:
        if el not in seen:
            distincts.append(el)
            seen.add(el)
    
    """
    Your unique() function works, 
    but checking if el not in distincts for 
    every element is O(n²) time complexity (slow for large lists).
    Better approach: Use a set (O(1) membership check) 
    to track seen elements.

    Why?
        set() has O(1) lookup time (faster than list’s O(n)).
        Still preserves order (unlike converting the entire list to a set directly).
    """

    return distincts
    

def count_element(table):
    # count_of = {}
    count_of = df_dict(int)

    for elt in table:
        # if elt in count_of:
        if elt in table:
            count_of[elt] += 1
        
        # else :
        #     count_of[elt] = 1

    """
    2. Simplify count_element() with collections.defaultdict
        Your count_element() is correct, but you can avoid the 
        if-else by using defaultdict from the collections module.
    
    
        
    """

    return dict(count_of)
    



# test :
my_array = [
    "beva",
    "gaby",
    "beva"
]

table = [
    "raphael", "bienvenu", "raphael", "apple", "banana",
    "apple", "orange", "bienvenu", "mango", "raphael",
    "grape", "banana", "pineapple", "bienvenu", "apple",
    "kiwi", "orange", "raphael", "mango", "banana",
    "grape", "pineapple", "bienvenu", "apple", "kiwi",
    "orange", "raphael", "mango", "banana", "grape"
]

# r = unique(my_array)
# print(r)
# print(count_element(my_array))

r = unique(table)
print(r)
print(count_element(table))