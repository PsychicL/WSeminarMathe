def isqrt(n):
    x = n
    y = (x + n // x) // 2
    print(f"Schritt 1 y={y}")
    while y < x:
        x = y
        print(f"Schritt 2 x={x}")
        y = (x + n // x) // 2
        print(f"Schritt 3 y={y}")
    print(f"{x}")


print(y)


print("teste mal ne zahl")
n=int(input())
isqrt(n)