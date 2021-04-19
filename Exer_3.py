# 3. Given a string, write a python function to check if it is
# palindrome or not. A string is said to be palindrome if the reverse
# of the string is the same as string. For example, “malayalam” is a
# palindrome, but “music” is not a palindrome.

pal = True
num = input('Enter the number : ')
for i in range((int((len(num)) / 2)) + 1):
    if num[i] == num[(len(num) - i - 1)]:
        continue
    else:
        pal = False
        break

if pal:
    print('Number ', num, ' is a palindrome')
else:
    print('Number ', num, 'is not a palindrome')
