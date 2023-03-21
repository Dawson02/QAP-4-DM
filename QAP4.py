#Author: Dawson Murray
#Date: March 17 2023

#Import
import datetime

#Read data from the OSICDef.dat file (defaults file) 
f = open("OSICDef.dat", "r")

NEXT_POL_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_COV = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_CAR_COV = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PROCESSING_FEE = float(f.readline())

f.close()

#Define valid provinces
ValidProvences = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

#Define functions for input validation
def IsValidProv(province):
    return province in ValidProvences

def ValidPostalCode(PostalCode):
    return len(PostalCode) == 6 and PostalCode[0].isalpha() and PostalCode[1].isdigit() and PostalCode[2].isalpha() and PostalCode[3].isdigit and PostalCode[4].isalpha() and PostalCode[5].isdigit()

def ValidPhoneNum(PhoneNumber):
    return len(PhoneNumber) == 10 and PhoneNumber.isdigit()

#Loop for entering policies and info    
while True:
    #Get Customer Information
    FirstName = input("First Name: ").title()
    LastName = input("Last Name: ").title()
    Address = input("Address: ")
    City = input("City: ").title()
    Province = input("Province: ").upper()
    while Province not in ValidProvences:
        Province = input("Invalid Province. Please Reenter: ").upper()
    PostalCode = input("Postal Code: ")
    PhoneNumber = input("Phone Number: ")

    #Extra Coverage and Calculation
    NumCars = int(input("Enter the number of cars being insured: "))

    ExtraCoverage = input("Would you like to add extra liability coverage?(Y/N): ")
    ExtraCoverageCost = 0.00
    if ExtraCoverage.upper() == "Y":
        ExtraCoverageCost = NumCars * EXTRA_LIABILITY_COV
    else:
        ExtraCoverageCost = 0.00

    GlassCoverage = input("Would you like glass coverage?(Y/N): ")
    if GlassCoverage.upper() == "Y":
        GlassCoverageCost = NumCars * GLASS_COV
    else:
        GlassCoverageCost = 0.00

    LoanerCar = input("Would you like loaner car coverage? (Y/N): ")
    if LoanerCar.upper() == "Y":
        LoanerCarCost = NumCars * LOANER_CAR_COV
    else:
        LoanerCarCost = 0.00

    #Calculations for total insurance premium
    BasicPrem = 869.00 #Basic rate for first vehicle
    Discount = 0.25 #Discount for eacg additional vehicle

    if NumCars == 1:
        BasicPrem
    else:
        BasicPrem + (NumCars - 1) * (1 - Discount) * BasicPrem

    TotalPrem = BasicPrem * NumCars * Discount + ExtraCoverageCost

    #Calculate the total cost with HST

    HstRate = 0.15
    TotalCost = TotalPrem * (1 + HstRate)

    #Calculate monthly payments
    ProcessingFee = 39.99

    PaymentMethod = input("Monthly or Full? (M/F): ").upper()
    if PaymentMethod == "M":
        MonthlyPayment = (TotalCost + ProcessingFee) / 8

    elif PaymentMethod == "F":
        PayMsg = "Your Total is {TotalCost}"

    else:
        print("Invalid Payment. Monthly or Full? (M/F): ").upper()

    #Display all inputs and calculated values
    print()
    print("---Receipt---")

    # Receipt
    print('---Receipt---')
    print(f'Date: {datetime}')
    print('Policy Number:', NEXT_POL_NUM)
    print('Customer Name:', FirstName, LastName)
    print('Customer Address:', Address)
    print(City + ',', Province, PostalCode)
    print('Customer Phone Number:', PhoneNumber)
    print()
    print('Number of Cars Insured:', NumCars)
    if ExtraCoverage:
        print('Extra Liability Coverage: $1,000.00')
    else:
        print('Extra Liability Coverage: $0.00')
    if GlassCoverage:
        print('Glass Coverage: $200.00')
    else:
        print('Glass Coverage: $0.00')
    if LoanerCar:
        print('Loaner Car Coverage: $500.00')
    else:
        print('Loaner Car Coverage: $0.00')
    print()
    print(f'Total Cost: {TotalCost}')
    print('HST: $300.53')
    if PaymentMethod == 'Monthly':
        print('Monthly Payment: $332.32')
    else:
        print('Full Payment: {PayMsg}')

    Exit = input("Do you wish to Continue? (Y/N): ").upper()
    if Exit == "N":
        exit()
    else:
        break
