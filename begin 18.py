A = float(input("Введите число A (A < C): "))
B = float(input("Введите число B (C < B): "))
C = float(input("Введите число C (A < C < B): "))
if A < C and C < B:
    print(f"Длина отрезка AC: {abs(C - A)}")
    print(f"Длина отрезка BC: {abs(B - C)}")
    print(f"Произведение длин отрезков AC * BC: {abs(C - A) * abs(B - C)}")
else:
     print("Ошибка, точка C не находится между точками A и B")