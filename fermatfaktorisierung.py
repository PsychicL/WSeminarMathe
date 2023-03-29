import math
 
n = int(input("Enter a number made of 2 primes pq: "))

a = math.isqrt(n) + 1
print(f" a ist {a}")

r = a*a - n

b = math.isqrt(r)

while b*b != r:
    a += 1
    r = a*a - n
    b = math.isqrt(r)

p = a+b
q = a-b
print(f"found a: {a}")
print(f"found b: {b}")
print(f"found p: {p}")
print(f"found q: {q}")



