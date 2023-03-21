#Print this list in Reversed
#Print the reversed list sorted.
#Output should be 2 lines.

list = [1,5,3,4,7,8,2]

# Collin's solution
rev_list = list.copy()
rev_list.reverse()

sorted_list = sorted(list, reverse=True)

print(rev_list)
print(sorted_list)

