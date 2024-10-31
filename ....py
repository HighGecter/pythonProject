'''def iterativeFib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a

print(iterativeFib(3))'''
while a%b>biggest
    a=b*a//b+a%b
return a
def Evclid(a:int,b:int):
    dividers = []
    for i in range(1, max(a,b)):
        if a%i == 0 and b%i == 0
            dividers.append(i)
    Biggest=max(dividers)
    if a>b:





def simplify(number):
    multipliers = []
    for i in range(2, number + 1):
        if number % i == 0:
            multipliers.append(i)
            number = number//i
    return multipliers

num = int(input())
print(f"Множители числа {num}:{simplify(num)}")