print ('Welcome to our fantastic Murcia Kino!')
print ('If you want to leave, please enter "quit".')
active = True

while active:
    age = input('\nPlease, enter your age to know price of the ticket: ')
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print ('The ticket is free!')
        elif age <= 12:
            print ('The ticket costs $10.')
        elif age > 12:
            print ('The ticket costs $15.')