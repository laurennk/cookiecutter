"""
A file for executing math functions.
"""

def main():
    print(euler())
    print(euler(100000))

def euler(n=10):
    e = 0

    for i in range(0,n):
        e += 1/fac(i)

    return e

def fac(n):
    x = 1

    for i in range(0,n-1):
        x = x*n

    return x

if __name__ == '__main__' :
    main()
