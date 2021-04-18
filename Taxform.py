"""
Program: Taxform.py
Author: Ben Baker 20069810 (C) April 2021
Compute a person’s income tax.
1. Significant constants tax rate standard deduction deduction per dependent
2. The inputs are gross income number of dependents
3. Computations: taxable income = gross income - the standard deduction - a deduction for each dependent income tax = is a fixed percentage of the taxable income
4. The outputs are the income tax
"""

# Initialise the constants
TAX_RATE_SINGLE = 0.15
TAX_RATE_MARRIED = 0.14
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs:
# Request gross income, ensuring it is a positive number value
while True:
    try:
        grossIncome = float(input("Enter the gross income: "))
        if grossIncome < 0:
            print("You can't have a negative income. Please try entering a positive value for gross income.")
        elif grossIncome >= 0:
            break
    except ValueError:
        print("Your income must consist of numbers. Please try again.")

# Request number of dependents, ensuring it is a positive number value
while True:
    try:
        numDependents = int(input("Enter the number of dependents: "))
        if numDependents < 0:
            print("You can't have a negative dependents. Please try entering a positive value.")
        elif numDependents >= 0:
            break
    except ValueError:
        print("You must enter a number. Please try again.")

# Request Tax File Number, ensuring it is a positive number value
while True:
    try:
        taxFileNumber = int(input("Enter your Tax File Number: "))
        if taxFileNumber < 0:
            print("You can't have negative number. Please try entering a positive value.")
        elif taxFileNumber >= 0:
            break
    except ValueError:
        print("You must enter a number. Please try again.")

# Request first name
firstName = str(input("Enter your first name: "))

# Request last name
lastName = str(input("Enter your last name: "))

# Request address
address = str(input("Enter your address: "))

# Request postcode, ensuring it is a positive numeric value
while True:
    try:
        postcode = int(input("Enter your postcode: "))
        if postcode > 0:
            break
        else:
            print("Your postcode can't be a negative number. Please try entering another number.")
    except ValueError:
        print("Your postcode must consist of numbers. Please try again.")

# Compute the taxable income, ensuring it is not less than zero
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
if taxableIncome < 0:
    taxableIncome = 0


# Request whether married
while True:
    try:
        marriedYorN = str(input("Are you married (Y/N)? ")).upper()
        if marriedYorN == "N":
            incomeTax = taxableIncome * TAX_RATE_SINGLE
            # Display the income tax
            print("\nNorth Metro Insurance")
            print("%10s%12s%12s%12s%16s%16s%16s%16s%16s" % ("Tax File Number", "Last name", "First name", "Address", \
                                                        "Postcode", "Number of dependents", "Marital Status", \
                                                        "Annual income", "Income Tax"))
            print("%10s%12s%14s%12s%16s%16s%16s%16s%16s" % (taxFileNumber, lastName, firstName, address, \
                                                        postcode, numDependents, marriedYorN, \
                                                        "$%0.2f" % grossIncome, "$%0.2f" % incomeTax))
            break
        elif marriedYorN == "Y":
            incomeTax = taxableIncome * TAX_RATE_MARRIED
            # Display the income tax
            print("\nNorth Metro Insurance")
            print("%10s%12s%12s%12s%16s%16s%16s%16s%16s" % ("Tax File Number", "Last name", "First name", "Address", \
                                                            "Postcode", "Number of dependents", "Marital Status", \
                                                            "Annual income", "Income Tax"))
            print("%10s%12s%14s%12s%16s%16s%16s%16s%16s" % (taxFileNumber, lastName, firstName, address, \
                                                            postcode, numDependents, marriedYorN, \
                                                            "$%0.2f" % grossIncome, "$%0.2f" % incomeTax))
            break
        else:
            print("There was an error. Make sure you enter Y or N.")
    except ValueError:
        print("You must enter a number. Please try again.")






