print("Number guessing game")
print("guess between 1 - 100")
guess = int(input("enter number:"))
if guess < 63:
    print("kam hai!")
elif guess > 63:
    print("zyada hai")
elif guess == 63:
    print("sahi hai")
