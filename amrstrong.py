armstrong
def factorial(num):
    fact = 1;
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
    print(fact())

num = input("Enter a number..");
result = factorial(num)
print("factorial of the number: %d" % result)
factorial(num)
