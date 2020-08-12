import math
#we asking the user which calculator they would like to use
invest = str(input("Choose either 'Investment' or 'Bond'\n"
+"Investment\t -To calculate the amount of intrest you will earn on interest\n"+
"Bond\t\t -the amount you will have to pay on your home loan.--->"))
#if they chose investment
if invest.upper() == "INVESTMENT":
    #we asking the user how much money they will be depositing
    p = int(input("Enter amount you will be depositing. "))
    #we asking how much interest they would like
    r = float(input("Enter the interest rate you would prefer (just the number please). "))
    #we asking the user how many years they would like to for
    t = int(input("Enter how many years you would you like to invest for. "))
    #we asking the user which type of interest they would like
    intrest = str(input("Would you prefer (simple/compound) interest. "))
    #if they choose simple interest
    if intrest.upper() == "SIMPLE":
        #formula for calculating simple interest
        A = p*(1+r*t)
        print(f"You will earn R{A} on {r}% of interest.")
    #if they choose compound interest
    elif intrest.upper() == "COMPOUND":
        #formula for calculating compound interest
        A = p*math.pow((1+r),t)
        #we printing the results
        print(f"You will earn R{A} on {r}% of interest.")
#if they chose bond
elif invest.upper() == "BOND":
    #we asking the user what is the present value of the house
    p = int(input("Enter present value of the houes. "))
    #we asking the user whats the annual interest rate
    i = float (input("Enter annual interest rate. "))
    #we are calculating the monthly interest rate by dividing it by 12
    i2 = i/12
    #we asking the user for the amout of months she will repay the bond
    n = int(input("Enter amount of months in which the bond will be repaind. "))
    #formula for calculating amount user has to pay fo the amount of months
    A = (i2 * p)/(1-math.pow((1+i),-n))
    #we printing the output
    print(f"You will have to pay R{A} for {n} months on {i}% intrest")