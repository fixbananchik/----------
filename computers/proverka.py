def bar(N, A, B, C):
    if 1 <= N <= 100:
        if 1 <= A <= 100:
            if 1 <= B <= 100:
                if 1 <= C <= 100:
                    return True
    else:
        print("Количество компьютеров или удлинителей должно быть меньше 100 и больше одного!!!")
        return False