import random

chances = 6
lotteryset = set()
count = 0
while count < 6:
    lottery = random.randint(1,20)
    if lottery not in lotteryset:
        lotteryset.add(lottery)
        count += 1
won = 0
for chance in range(chances):
    num = int(input("Enter your lucky number: "))
    if num in lotteryset:
       won += 1
       print("You won a lottery! Congrats")
    else:
        print("Oops no luck! Try again!")
print(f"You won {won} lotteries totally!")