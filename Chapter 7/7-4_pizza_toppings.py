# This program simulates a pizza topping selection process.
# Users can choose toppings, view their current selections, or quit.

# --- IMPORTANT NOTE FOR FUTURE DEVELOPMENT ---
# Currently, this program DOES NOT prevent duplicate toppings.
# This feature will be added in a future update.
# ---------------------------------------------

# --- Topping Definitions & Initialization ---

# Tuple of available pizza toppings (tuple).
pizza_toppings = ('mozzarella', 'mushrooms', 'bacon', 'olives', 'pepperoni', 'cheddar', 'tomato', 'onion')

# List to store toppings selected by the user.
pizza_topping = []

# Control variable for the main selection loop.
active = True

# --- Display Available Toppings ---

print('The available toppings are:')
# Loop and print each available topping.
for pizzas in pizza_toppings:
    print('* ' + pizzas.title() + '.')

# --- Main Topping Selection Loop ---

# Loop continues until 'active' is False.
while active:
    # Get user input and convert to lowercase.
    requested_topping = input('What pizza topping would you like to add to your pizza? ').lower()

    # Check if user wants to quit.
    if requested_topping == 'quit':
        active = False # Exit loop
    # Process user input.
    else:
        # Check if requested topping is available.
        if requested_topping in pizza_toppings:
            print(f'Adding {requested_topping} to your pizza!')
            pizza_topping.append(requested_topping) # Add to user's pizza
        # Check if user wants to list current toppings.
        elif requested_topping == 'list':
            print('Your pizza has the following toppings:')
            # Loop and print each selected topping.
            for topping in pizza_topping:
                print('* ' + topping.title())
        # If topping is not available.
        elif requested_topping not in pizza_toppings:
            print('That topping is not available.')