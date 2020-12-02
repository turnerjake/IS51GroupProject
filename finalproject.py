"""
STRUCTURED ENGLISH

Create a calculator to simplify some common calculations used in statistics

Provide user with 'menu' of options in the calculator
Switch to different functions based off of user input

Normal Approximation:
Take in values for n & p (these are values that are given/found when working out these problems)
check if p > 1, if true throw error
From p, find the value of q (1 - p)
Calculate and print to user (np, sqrt(npq))
Ask user if they want to calculate another or return to main menu

Z-score calculator:
Take in values for x, u, o (these are values that are given/found when working out these problems)
Check if o < 0, if true throw error
Calculate and return z = (x-u)/0
Ask user if they want to calculate another or return to main menu

Function Dictionary:
Initialize a dictionary that defines the functions in the calculator
Iterate through the keys and print values to user when function is called
Return to main menu

Exit:
Exit() from program

END STRUCTURED ENGLISH
"""