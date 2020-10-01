def checkNumber(n):
    for i in range(2, n):
        if n % i == 0:
            return False # ikke primtal
    return True # er primtal


def printPrimeNumbers(n):
    for i in range(2, n):
        if checkNumber(i) == True:
            print(i)

if __name__ == "__main__":
    printPrimeNumbers(20)