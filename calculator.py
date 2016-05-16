
"""def number_ask():
    try:
       answer = float(input())
    except ValueError:
       exit()
    return float(answer)"""



def add():
    summ = float(n_1) + float(n_2)
    print ("Result: ", summ)

def sub():
    diff = float(n_1) - float(n_2)
    print ("Result: ", diff)

def multi():
    prod = float(n_1) * float(n_2)
    print ("Result: ", prod)

def div():
    quot = float(n_1) / float(n_2)
    print ("Result: ", quot)

n_1 = float(input("Enter the first number (or a letter to exit): "))
while n_1 != float():
    operator = input("Enter an operation: ")
    n_2 = float(input("Enter the second number: "))
    if (operator == "+"):
        add()
    if (operator == "-"):
        sub()
    if (operator == "*"):
        multi()
    if (operator == "/"):
        div()
    print ("\n")
    n_1 = float(input("Enter the first number: "))
