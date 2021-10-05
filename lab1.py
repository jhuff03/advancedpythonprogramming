salary = float(input("Please input your salary: ")) #input statement for salary

if salary <= 0: #if the salary is not a positive number, the program exits with a message explaining the error
    print("ERROR: Salary must be positive.")
    exit()

hours = float(input("Please input your hours: ")) #input statement for hours

if hours <= 0: #if the hours is not a positive number, the program exits with a message explaining the error
    print("ERROR: Hours must be positive.")
    exit()

if hours >= 40: #this is the calculation for the overtime
    hours -= 40
    print("You made ", (40 * salary) + hours * (salary * 1.5), " dollars.")
else:
    print("You made", salary * hours, " dollars.") #this returns the pay but without overtime