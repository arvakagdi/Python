#try:
print("Please think of a number between 0 and 100!")
#except:
#   print("That's not a valid number:")

epsilon = 0.01
l =  0.0
h = 100.0
inputu = ''

while( inputu != 'c'):
    ans = (l+h)/2
    print("Is your secret number", ans, '?')
    inputu = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if(inputu == 'h'):
        h = ans
    elif(inputu == 'l'):
        l = ans
    elif(inputu !='h' or inputu != 'l' or inputu != 'c'):
        print("Sorry, I did not understand your input.")


print("Game over. Your secret number was:", ans)



