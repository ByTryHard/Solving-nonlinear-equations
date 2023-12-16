import math

def f(x):
    return x - math.log(10*x - math.log(x))

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

def Delenie_otrezka(x0, epsilon):
    a = 2.9
    b = 3.9
    count = 0
    x_pred = x0
    while True:
        x = (a + b) / 2
        fx = f(x)
        if fx == 0 or abs((x-x_pred) / x) < epsilon:
            break
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x
        x_pred = x
    count +=1
    pog = abs((x-x_pred) / x)
    return x, f(x), count, pog

x0 = 3.4
epsilon = 0.0001
xn, nevyazka, count, pogeshnost = simple_iteration(x0, epsilon)
print("Простая итерация: Приближенное значение корня: ", xn)
print("Невязка: ", nevyazka)
print("Количество итераций: ", count)
print("Погрешность: ", pogeshnost)

xn, count, pogeshnost = newton_method(x0, epsilon)
print('\nМетод Ньютона: Приближенное значение корня:', xn)
print('Количество итераций:', count)
print('Погрешность:', pogeshnost)

root, residue,count,pog = Delenie_otrezka(x0, epsilon)
print("\nДеления отрезка пополам: Приближенное значение корня: ", root)
print("Невязка: ", residue)
print("Количество итераций: ", count)
print("Погрешность: ", pog)
