def print_string():
    print("code started.")


if __name__ == '__main__':
    print_string()

fibo_n = int(input("enter a number for the Fibonacci series:\n"))

n1, n2 = 0, 1
t = 0

print("The Fibonacci series is:")
while t < fibo_n:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    t += 1
