real_age = 36
age_guessed = int(input("Input the age you guessed: "))

if age_guessed == real_age:
    print("Congratulation! Your guess is right.")
elif age_guessed > real_age:
    print("Sorry, you should try a smaller one.")
else:
    print("Sorry, you should try a bigger one.")
# else:
#     print("Sorry, your guess is wrong.")
