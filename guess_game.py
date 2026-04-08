secret_num= 7
guess_num= int(input("guess a number (1 to 10): "))

if guess_num == secret_num:
    print ("Bingo, Correct answer.")
elif secret_num +1 == guess_num or secret_num -1 == guess_num:
    print ("Close enough to the correct answer.")
else:
    print ("Try again.")