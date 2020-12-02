"""
FINAL CODE
"""
import math

def approximationCalculator():
    print()
    n = inputErrorHandler("What is the value of n (number of trials)?", float)
    p = inputErrorHandler("What is p (probability of success)?", float)

    if (p > 1):
        print("Sorry, the value of 'p' should not be greater than 1. Please check your values and try again.")
        print()
        approximationCalculator()
    else:
        q = 1 - p
        np = n * p
        npq = n * p * q
        squareRoot = math.sqrt(npq)
        print()
        print(("The best normal approximation for this distribution is N({0:.2f}, {1:.2f}).").format(np, squareRoot))
        print()
    
    shouldContinue = inputErrorHandler("Enter 1 to continue or 0 to return to the main menu:", int)
    if shouldContinue:
        approximationCalculator()
    else:
        print()
        main()

def zScoreCalculator():
    print()
    x = inputErrorHandler("What is the value of x (raw score)?", float)
    u = inputErrorHandler("What is the value of u (mean/mu)?", float)
    o = inputErrorHandler("What is the value of o (sample standard deviation)?", float)

    if (o < 0):
        print("Sorry, the value of 'o' should not be negative. Please check your values and try again")
        zScoreCalculator()
    else:
        z = (x-u)/o
        print()
        print(("The Z-Score for this calculation is {0:.2f}").format(z))
        print()
    
    shouldContinue = inputErrorHandler("Enter 1 to continue or 0 to return to the main menu:", int)
    if shouldContinue:
        zScoreCalculator()
    else:
        print()
        main()

def functionDictionary():
    functionDefinitions = {
        1: 'The normal distribution can be used in certain cases to approximate a binomial distribution.',
        2: 'The Z-score is the number of standard deviations the given raw score is away from the mean of the data set.',
        }
    for key in functionDefinitions:
        print("{0}: {1}".format(key, functionDefinitions[key]))
    print("")
    main()

def inputErrorHandler(promptStatement, dataType):
    inputError = True
    while inputError:
        try:
            inputValue = dataType(input(promptStatement + " "))
            break
        except ValueError:
            print("Sorry, please enter your selection as an integer")
    return inputValue

def main():
    functionOptions = {1: 'Normal Approximation Calculator', 2: 'Z-Score Calculator', 3: 'Function Dictionary', 4: 'Exit'}
    print("Welcome to the EasyStats calculator!")

    for key in functionOptions:
        print("{0}: {1}".format(key, functionOptions[key]))
    
    functionSelect = inputErrorHandler("What would you like to do?", int)
    
    #Selection 'switch'
    if (functionSelect == 1):
        approximationCalculator()
    elif (functionSelect == 2):
        zScoreCalculator()
    elif (functionSelect == 3):
        functionDictionary()
    elif (functionSelect == 4):
        print("Thank you for using the EasyStats Calculator!")
        exit()
    else:
        print("Sorry, that was an invalid input.")
        print()
        main()
main()