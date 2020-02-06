epsilon = 0.00001
step = 0.000001
guess = 0.0
num_guesses = 0
cube = 26

while abs(guess**2 - cube) >= epsilon:
    guess += step
    num_guesses +=1

print('num of guesses:' , num_guesses)
print("Approx cube root", guess)