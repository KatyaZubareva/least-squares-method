import numpy as np
import matplotlib.pyplot as plt

# Отклонение между предсказанными значениями и реальными
def deviation_measure(func, x_values, y_values, coefficients=None):
    total_deviation = sum(
        (func(x_values[i], *coefficients) - y_values[i]) ** 2
        for i in range(len(x_values))
    )
    return total_deviation

# Среднеквадратичное отклонение
def rms_deviation(func, x_values, y_values, coefficients=None):
    n = len(x_values)
    total_deviation = deviation_measure(func, x_values, y_values, coefficients)
    return np.sqrt(total_deviation / n)

# Функции
def func1(x, a, b):
    return a * x + b

def func2(x, a, b, c):
    return a * x ** 2 + b * x + c

def func3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

def func4(x, a, b):
    return a * (b ** x)

def func5(x, a, b):
    return a * np.log(x) / np.log(b)

def func6(x, a, b):
    return a * x ** b

# Метод наименьших квадратов
def least_squares(func, x_values, y_values, degree=1):
    x_transformed = x_values.copy()
    y_transformed = y_values.copy()

    if func == func4:
        y_transformed = np.log(y_values)
    elif func == func5:
        x_transformed = np.log(x_values)
    elif func == func6:
        x_transformed = np.log(x_values)
        y_transformed = np.log(y_values)

    # Формируем матрицу X
    X = np.vander(x_transformed, degree + 1)
    Y = y_transformed

    # Решаем задачу наименьших квадратов
    coefficients, _, _, _ = np.linalg.lstsq(X, Y, rcond=None)

    if func == func4:
        coefficients[0] = np.exp(coefficients[0])
    elif func == func6:
        num1 = coefficients[0]
        coefficients[0] = np.exp(coefficients[1])
        coefficients[1] = num1


    return coefficients


# Построение графиков
def plot_function(x_values, y_values, fitted_x, fitted_y, label1, label2):
    plt.scatter(x_values, y_values, color="blue", label=label1)
    plt.plot(fitted_x, fitted_y, color="red", label=label2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()

# Чтение данных
def read_data_from_file(filename):
    x_values, y_values = [], []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split(','))
            x_values.append(x)
            y_values.append(y)
    return np.array(x_values), np.array(y_values)

# Основная функция
def main():
    filename = "data.txt"
    x_values, y_values = read_data_from_file(filename)

    functions = {
        1: ("Линейная функция: ϕ(x) = ax + b", func1, 2),
        2: ("Полиномиальная 2-й степени: ϕ(x) = ax² + bx + c", func2, 3),
        3: ("Полиномиальная 3-й степени: ϕ(x) = ax³ + bx² + cx + d", func3, 4),
        4: ("Экспоненциальная функция: ϕ(x) = a * b^x", func4, 2),
        5: ("Логарифмическая функция: ϕ(x) = a * log_b(x)", func5, 2),
        6: ("Степенная функция: ϕ(x) = a * x^b", func6, 2)
    }

    best_deviation = float('inf')
    best_function = None
    best_coefficients = None
    best_label = None

    results = []

    for _, (label, function, num_coeffs) in functions.items():
        coefficients = least_squares(function, x_values, y_values, degree=num_coeffs - 1)
        total_deviation = deviation_measure(function, x_values, y_values, coefficients)
        rms = rms_deviation(function, x_values, y_values, coefficients)

        results.append((label, coefficients, total_deviation, rms))

        if total_deviation < best_deviation:
            best_deviation = total_deviation
            best_function = function
            best_coefficients = coefficients
            best_label = label

    # Вывод наиболее точной функции в начале
    print(f"Наиболее точная функция: {best_label}")
    print(f"Коэффициенты для {best_label}: {best_coefficients}")
    print(f"Мера отклонения (S): {best_deviation}\n")

    # Вывод всех функций
    print("Результаты для всех функций:")
    for label, coefficients, deviation, rms in results:
        print(f"{label}\nКоэффициенты: {coefficients}\nМера отклонения (S): {deviation}\nСреднеквадратичное отклонение (Δ): {rms}\n")

    # Построение графика для наиболее точной функции
    fitted_y_values = [best_function(x, *best_coefficients) for x in x_values]
    plot_function(x_values, y_values, x_values, fitted_y_values, "Original Data", f"Fitted {best_label}")

if __name__ == "__main__":
    main()
