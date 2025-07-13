current_users = ["Joey", "roSS", "ChAdler", "rachel", "monica", "Phoebe"]

new_users = ["joey", "Ross", "MONICA", "Homer", "bart"]

current_users_low = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_low:
        print (f"{new_user} not available")
    else:
        print (f"{new_user} available")