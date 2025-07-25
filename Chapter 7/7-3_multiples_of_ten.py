number = input ("Enter a number and I'll tell you if that number is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print ('That number is a multiple of 10.')
else:
    print ('That number is not a multiple of 10.')