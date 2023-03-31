def nine(n):
    v = ""
    while n > 0:
        v = str(n % 9) + v 
        n = n // 9
    return v
n = int(input("Введите число n"))
print(nine(n))