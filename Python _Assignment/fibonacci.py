# write a program for fibonnaci series

def FibonacciSeries(num):
    n0 = 0
    n1 = 1
    print(n0)
    print(n1)
    for f in range(num):
        n2 = n0+n1
        print(n2)
        n0 = n1
        n1 = n2 

num = int(input("Enter the number: "))
FibonacciSeries(num)