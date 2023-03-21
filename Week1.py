# Week 1 Viper Check
# Given the variables below, print the following title "Valorant Sucks!"

listOfWords = ['Va', 'lo', 'rant', 'Sucks!']

title = 'Va'
title2 = 'lo'
title3 =  'rant'
title4 = 'Sucks!'



#example using join()
print(' '.join(listOfWords))

#example using + operator
print(title+title2+title3+' '+title4)

#example using f strings
print(f"{title}{title2}{title3} {title4}")

#example using print statement
print(title,title2,title3, title4)

#collin's solution: 
print('{}{}{} {}'.format(title, title2, title3, title4))

#brycer solution:
print(title+title2+title3+' '+title4)