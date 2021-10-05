a = float(input("Input your first number: ")) #input statement
o = str(input("Input your operation: ")) #input statement
b = float(input("Input your first number: ")) #input statement

if o != "+" and o != "-" and o != "*" and o != "*" and o != "/" and o != "%" and o != "^":
    print("Error ", o, " is not a valid operator")
    exit()

thisdict = {
    "+": a + b,
    "-": a - b,
    "*": a * b,
    "/": a * b,
    "%": a % b,
    "^": a ** b,
}

print(thisdict[o])