def ask_input_1():
    number_1 = int(input("Input your first number >>> "))
    return number_1

def ask_input_2():
    number_2 = int(input("Input your second number >>> "))
    return number_2

def ask_operation():
    opt = input("Input your operator >>> ")
    return opt

def calculate():
    calculate.one = ask_input_1()
    calculate.opt = ask_operation()
    calculate.two = ask_input_2()

    if calculate.opt == "+":
        answer = calculate.one + calculate.two
    elif calculate.opt == "-":
        answer = calculate.one - calculate.two
    elif calculate.opt == "*":
        answer = calculate.one * calculate.two
    elif calculate.opt == "/":
        answer = calculate.one / calculate.two

    return answer

def display():
    answer = calculate()
    print(f"{calculate.one} {calculate.opt} {calculate.two}")
    print(answer)


comment = False
while comment != "quit":
    display()