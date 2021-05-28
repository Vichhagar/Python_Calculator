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
    try:
        calculate.one = ask_input_1()
        calculate.opt = ask_operation()
        calculate.two = ask_input_2()
    except Exception:
        print("\n")
        print_line(25)
        print("Please Enter a valid input!")
        print_line(25)
    else:
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
    if answer:
        print("\n")
        print_line(25)
        print("Your answer: ")
        print(answer)
        print_line(25)
        print("\n")
    else:
        print_line(25)
        print("No answer to be shown")
        print_line(25)
        print("\n")

def print_line(n):
    print("-" * n)


comment = False
while comment != "quit":
    display()