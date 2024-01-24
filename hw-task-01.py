import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize number of drinks", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту "Лимонад" 
B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # Кількість продукту "Фруктовий сік"

# Функція цілі (Максимізація кількості напоїв)
model += A + B, "Number of drinks"

# Додавання обмежень
model += 2 * A + B <= 100, "Constraint_water"  # Обмеження для води
# model += A <= 50, "Constraint_sugar"  # Обмеження для цукру !!! цю умову можемо не враховувати, оскільки є більш жорстке обмеження по лим. соку
model += A <= 30, "Constraint_lemon juice"  # Обмеження для лимонного соку
model += 2 * B <= 40, "Constraint_fruit puree"  # Обмеження для фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print ("\nМаксимальна загальна кількість вироблених напоїв 'Лимонад' та 'Фруктовий сік', враховуючи обмеження на кількість ресурсів: ")
print("напій 'Лимонад':", A.varValue, " шт.")
print("напій 'Фруктовий сік':", B.varValue, " шт.")
print(f"Значення цільової функції, яке є результатом оптимізації = {pulp.value(model.objective)}")
print("Статусу розв'язку задачі: ", pulp.LpStatus[model.status])
