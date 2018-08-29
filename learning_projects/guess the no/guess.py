import random
guess_again=1;guess_count=0;guess_less=0;guess_more=0;perfect_guess=0
while guess_again !=0:
    user_guess=int(input("Guess a number between 1-100\n"))
    if user_guess>1 and user_guess<=100:
        random_guess=random.randint(1,100)
        if user_guess>random_guess:
            guess_more+=1
            print(random_guess)
            print("Sorry!!! You went too far from system\'s guess.")
        elif user_guess<random_guess:
            guess_less+=1
            print(random_guess)
            print("Ohh!!! You ain\'t even near to system\'s guess.")
        else:
            perfect_guess+=1
            print("Bingoo!!! Your guess is right.")
        guess_count+=1
    else:
        print('Invalid input. Try again.')
    guess_again=int(input("Want to guess again? 0=NO, 1=YES\n"))
print('You\'ve made',guess_count,'guesses.')
print('Guessed more than system:',guess_more,'times.')
print('Guessed less than system:',guess_less,'times.')
print('Guessed perfectly:',perfect_guess,'times.')