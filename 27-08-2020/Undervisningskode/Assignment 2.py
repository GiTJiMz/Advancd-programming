stack = []
operator = {"+" : (lambda a, b: a + b), "-" : (lambda a, b: a - b)}

while True:
    x = input(f"{stack}")

    if x == "+":
        pass
    elif x == "-":
        pass
    elif x == "*":
        pass
    elif x == "/":
        pass
    elif x == "!":
        y = int(stack.pop())
        res = 1
        for f in range(1, y + 1):
            res *= f
        stack.append(res)
    else:
        stack.append(int(x))
    