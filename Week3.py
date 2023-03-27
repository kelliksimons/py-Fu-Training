# Write a function that prints numbers 1 to 10 
# Then on a new line it prints every other number i.e 1,3,5,7,9
# You should have 2 lines. 1 to 10 and 1,3,5,7,9
# Testing

numbers = [1,2,3,4,5,6,7,8,9,10] # setting a variable for the numbers


def yee():                       # giving a function that prints 1-10 and another line that skips every other number
    print(numbers)
    print(numbers[::2])

yee()                             # executing the function here
    

# Collin's Solution
def one_to_ten():
    num = 10

    print(','.join([str(i) for i in range(1, num + 1)]))
    print(','.join([str(i) for i in range(1, num + 1, 2)]))
    
one_to_ten()

