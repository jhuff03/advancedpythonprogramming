year = int(input("Please input the year (0 is 1990): "))

def calcPopPos(year):#Calculate the population if the year is after or equal to 1990
    output = 89.2
    for i in range (year): #increase the population for each year
        output *= (1.023)
    return output

def calcPopNeg(year): #Calculate the population if the year is before 1990
    output = 89.2
    for i in range (year): #increase the population for each year
        output /= (1.023)
    return output

if year >= 0: #Determine which function to run whether or not the year is over or under 1990
    print("The population in Mexico in ", (1990 + year), " is ", calcPopPos(year), "million")
else:
    print("The population in Mexico in ", (1990 + year), " is ", calcPopNeg(-year), "million")

pop = int(input("Please input the population in millions: "))


def calcYearNeg(pop): #Calculate the Year where the population is equal to the population inputted if that population is less than the population in 1990
    start = 1990
    while 1==1: #run loop infinitely
        if int(calcPopNeg(1990-start)) <= int(pop): #if the population in a given year is close enough...
            return start #return the current year and...
            break #end the loop
        start -= 1 #decrease year

def calcYearPos(pop): #Calculate the Year where the population is equal to the population inputted if that population is greater than the population in 1990
    start = 0
    while 1==1: #run loop infinitely
        if int(calcPopPos(start)) >= int(pop): #if the population in a given year is close enough...
            return 1990 + start #return the current year and...
            break #end the loop
        start += 1 #increase the year



if pop < 89.2: # ensure that the right function is run depending on the population chosen
    print("The population in the year ", calcYearNeg(pop), " is ", calcPopNeg(1990 - calcYearNeg(pop)), " million")
else:
    print("The population in the year ", calcYearPos(pop), " is ", calcPopPos(calcYearPos(pop) - 1990), " million")