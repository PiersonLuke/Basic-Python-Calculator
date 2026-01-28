def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def numerator():

    a = (
        input("Enter a number for the numerator: "))
    if is_float(a) == False:
        return None
    else:
        x = float(a)
        operator = input(
            "Enter an operator (+ - * /) or Enter nothing to Exit: ")
        while operator in {"+", "-", "*", "/"}:
            b = (input("Enter another number for the numerator: "))
            match operator:
                case "+":
                    x = float(a) + float(b)
                case "-":
                    x = float(a) - float(b)
                case "*":
                    x = float(a) * float(b)
                case "/":
                    if b in {'0', ""}:
                        UND = "Output: Undefined"
                        return UND
                    else:
                        x = float(a) / float(b)
                case _:
                    return x
            a = x
            operator = input(
                "Enter another operator (+ - * /) or Enter nothing to move to the denominator: ")
        return x


num = numerator()


if num is None:
    print("Output: 0")
elif num == "Output: Undefined":
    print("Output: Undefined")
else:

    def denominator():

        a = (
            input("Enter a number for the Denominator or Nothing for no denominator: "))
        if is_float(a) == False:
            return 1
        else:
            y = float(a)
            operator = input(
                "Enter an operator (+ - * /) or Enter nothing to Exit: ")
            while operator in {"+", "-", "*", "/"}:
                b = (input("Enter another number for the denominator: "))
                match operator:
                    case "+":
                        y = float(a) + float(b)
                    case "-":
                        y = float(a) - float(b)
                    case "*":
                        y = float(a) * float(b)
                    case "/":
                        if b in {'0', ""}:
                            return None
                        else:
                            y = float(a) / float(b)
                    case _:
                        return y
                a = y
                operator = input(
                    "Enter another operator (+ - * /) or Enter nothing to get the answer: ")
            return y
    den = denominator()
    if den is None:
        print("Output: UNDEFINED")
    else:
        print(f"Output: {num / den}")
