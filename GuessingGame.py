import random

# Main logic

def run():
    
    # Range of numbers AI can guess
    numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    attempts = []
    
    
    # Loops guesses until correct
    while True:
        print('')
        guess = random.choice(numbers)
        print(guess)
        correct = input('\nY/N: ')
        if correct == 'y' or correct == 'Y':
            print("\nWow, I'm good!")
            # Removes guess from list before continuing
            numbers.remove(guess)
            # Prints remaining numbers in list
            print("\nRemaining numbers were: ", numbers)
            # Takes number of list items remaining and subtracts from what is remaining to determine amount of guesses it took
            remaining = 51 - len(numbers)
            print("\nIt took " + str(remaining) + " guesses!")
            print("\nNumbers guessed: ", attempts)
            break
        else:
            # Adds guess to attempts list
            attempts.append(guess)            
            # Removes guess from list before continuing guesses
            numbers.remove(guess)
            
        
    
    
    
    
    


is_ready = input("Do you have a number, between 0 and 50 picked? (y/n): ")

if is_ready == 'y' or is_ready == 'Y':
    print("\n\nOk good. I will begin guessing.")
    run()
else:
    exit()
