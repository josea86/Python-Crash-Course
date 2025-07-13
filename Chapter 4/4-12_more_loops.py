my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods:
    print ("My favorite food is " + food)

for food in friend_foods:
    print ("My friend's favorite food is " + food)