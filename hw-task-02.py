import random
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції 
def f(x):
    return np.sqrt(1 - x**2)


def draw_graph_of_func (a, b):
    # Створення діапазону значень для x
    x = np.linspace(-0.1, 1.21, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = sqrt(1 - x^2) від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


def is_inside(x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині квадранта кола."""
    return y <= np.sqrt(1 - x**2)


def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        # Відбір точок, що знаходяться всередині квадранта кола
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (a * b)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area


def main():
    a = b = 1  # Розміри квадрата
    # визначення межі інтегрування
    c = 0
    d = 1 
    draw_graph_of_func (c, d)
    
    num_experiments = 100  # Кількість експериментів
    
    
    
    # Виконання симуляції
    average_area = monte_carlo_simulation(a, b, num_experiments)
    print(f"Середня площа квадранта кола (значення інтегралу) методом Монте-Карло за {num_experiments} експериментів: {average_area}")

    # Обчислення інтеграла
    result, error = spi.quad(f, c, d)
    print("Інтеграл: ", result, "error:", error)
    
    # Обчислення площі квадранта кола за формулою
    S = math.pi / 4 
    print(f"Теоретична площа квадранта кола: {S}")

    # порівняння результатів обчисленя:
    res = ((result-average_area)/result)*100
    print("Різниця в результатах обчислення = ", res, "%")

if __name__ == "__main__":
    main()








