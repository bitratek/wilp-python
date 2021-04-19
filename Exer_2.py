num = input('Enter the number : ')
ord = input('Enter the order : ')

bsum = 0

for digit in num:
    bsum += int(digit) ** int(ord)
print(bsum)

if bsum == int(num):
    print('Number ', num, 'is Armstrong Number')
else:
    print('Number ', num, 'is not Armstrong Number')
