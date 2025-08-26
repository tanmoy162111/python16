import random
print("You got")
for i in range(1,6):
    lower = 1
    higher = 14
    card_no = random.randint(lower, higher)
    card_name = ["spade", "heart", "diamond", "club"]
    shuffled = random.choice(card_name)
    print( card_no, " of ", shuffled)