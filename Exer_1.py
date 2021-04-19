# 1. Given a number, find the sum of its digits. Take the number as
# an input from the user.

# number = input('Enter the number :')
print('Sum of Digits : ', sum(list(map(int, input('Enter the number :').strip()))))
