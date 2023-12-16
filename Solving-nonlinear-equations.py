import math

def simple_iteration(x0, epsilon):
    x = x0
    count = 0
    xn = math.log(10*x0 - math.log(x0))
    while abs(( xn - x ) / xn) >= epsilon:
        x = xn
        xn = math.log(10*x - math.log(x))
        count += 1
    nevyazka = xn - math.log(10*xn - math.log(xn))
    pogeshnost = abs(( xn - x ) / xn)
    return xn, nevyazka, count, pogeshnost

def newton_method(x0, epsilon):
    x = x0
    count = 0
    xn = math.log(10*x0 - math.log(x0))
    while abs((xn - x) / xn) < epsilon:
        xn = x0 - math.log(10*x - math.log(x)) / ((10 - 1/x) / (10*x - math.log(x)))
        x = xn
    count += 1
    pogeshnost = abs((xn - x) / xn)
    return xn, count, pogeshnost

x0 = 3.4
epsilon = 0.0001
root = newton_method(x0, epsilon)


xn, nevyazka, count, pogeshnost = simple_iteration(x0, epsilon)
print("Простая итерация: Приближенное значение корня: ", xn)
print("Невязка: ", nevyazka)
print("Количество итераций: ", count)
print("Погрешность: ", pogeshnost)

xn, count, pogeshnost = newton_method(x0, epsilon)
print('Метод Ньютона: Приближенное значение корня:', xn)
print('Количество итераций:', count)
print('Погрешность:', pogeshnost)