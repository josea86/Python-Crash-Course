fruits = ["kiwi","banana", "watermelon", "apple", "plum"]

favorite_fruits = ["kiwi","watermelon","plum"]

for fruit in fruits:
    if fruit in favorite_fruits:
        print ("You really like " + fruit + "!")
    else:
        print (f"{fruit.title()} not in 'favorite_fruit' list.")