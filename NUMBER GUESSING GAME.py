import random
secret = random.randint(1,100)
attempts = 0
print("Number guessing game!")
print("1-100 ke beech guess karo")

while True:
     guess = int(input("Guess:"))
     attempts +=1
     if guess < 63:
          print("kam hai! Try Again!")
     elif guess > 63:
          print("zyada hai! Try again")
     else:
          print(f"sahi {attempts} attempts mein jeeta!")
