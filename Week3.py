# Write a function that prints numbers 1 to 10 
# Then on a new line it prints every other number i.e 1,3,5,7,9
# You should have 2 lines. 1 to 10 and 1,3,5,7,9
# Testing


# Collin's Solution
def one_to_ten():
    num = 10

    print(','.join([str(i) for i in range(1, num + 1)]))
    print(','.join([str(i) for i in range(1, num + 1, 2)]))
    
one_to_ten()