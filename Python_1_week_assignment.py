
#FizzBuzz

for i in range(1, 101):
    message = ''

    if i % 3 == 0:
        message += "Fizz"

    if i % 5 == 0:
        message += "Buzz"
    print(i, message)


#GCD

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(15,17))