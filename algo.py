def unique(array):
    distincts = []

    for el in array:
        if el not in distincts:
            distincts.append(el)
    return distincts

def count_element(table):
    count_of = {}

    for elt in table:
        if elt in count_of:
            count_of[elt] += 1
        
        else :
            count_of[elt] = 1

    return count_of
# test :
my_array = [
    "beva",
    "gaby",
    "beva"
]

r = unique(my_array)
print(r)
print(count_element(my_array))