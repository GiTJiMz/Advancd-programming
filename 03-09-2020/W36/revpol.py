
from operator import add

stack = []
ops = {
    "+" : add,
    "-": lambda a, b: a - b,
    "/": lambda a, b: a // b,
    "*": lambda a, b: a * b
    } 
while True:
    stackstr = ', '.join(map(str,stack))
    i = input(f'| {stackstr:<40s} | ')
    if i in ops:
        fst = stack.pop()
        try:
            snd = stack.pop()
        except IndexError:
            snd = 0 
        stack.append(ops[i](snd, fst))
    elif i.lower().startswith("q"):
        print("Thank you, next!")
        break
    else:
        try:
            stack.append(int(i))
        except:
            print("Unknown cmd: {i}")
        
        
        