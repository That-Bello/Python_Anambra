#
# Python Boot Camp Week 3
# TASK 2.
#
# Create a program that prints the Fibonacci sequence up to n terms.

"""
fib_num(0) = 0
fib_num(1) = 1
fib_num(n) = fib_num(n-1) + fib_num(n-2)
"""

nth = int(input("Enter number: "))

fn1 = 0
fn2 = 1
fib_seq = []

for index in range(nth):
    fib_seq.append(fn1)
    fn1, fn2 = fn2, fn1 + fn2

print(f"Prints the Fibonacci sequence up to {nth} terms")

for fib_num in fib_seq:
    print(fib_num, end=" ")






