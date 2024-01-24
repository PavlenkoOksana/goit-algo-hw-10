# goit-algo-hw-10

# Лінійне програмування та рандомізовані алгоритми

## Опис завдання

Завдання полягає у перевірці правильності розрахунків значення інтеграла функції за допомогою методу Монте-Карло, щоб підтвердити точність методу Монте-Карло, шляхом порівняння отриманого результату та аналітичних розрахунків або результату виконання функції quad. Зробіть висновки. 

## Функція

Для цього завдання була обрана функція, графік якої являє собою коло радіусом 1:

$$x^{2} + y^{2} = 1$$ 

чи іншими словами 

$$y = \sqrt{1-x^{2}}$$

## Графік функції

![graf_func](https://github.com/PavlenkoOksana/goit-algo-hw-10/assets/107678761/64086390-7c82-4f33-9ec5-06e0adb9d868)

## Результати розрахунків значення інтеграла функції за допомогою методу Монте-Карло

Для порівняння результатів розрахунків, були проведені тести, з різними параметрами (кількість проведених експериментів та кількість випадкових точок points). Результати тестування наведені в таблицях:

| кіл-ть експериментів   | 1 | 1 | 1 | 1 | 10 |100|
| ----------------------- |:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| кіл-ть точок   | 10 | 100 | 1000 | 15000 | 15000 |15000|
| площа |0.7|0.86|0.785|0.7868|0.7856|0.7849833333333335|
 
Як можна побачити у результатах тестування, точність розрахунків суттєво залежить від кількості проведених експериментів та від кількості згенерованих випадкових точок.

## Перевірка обчислення визначеного інтеграла:

Перевірку обчислення визначеного інтеграла за допомогою методу Монте-Карло я здійснила двома способами:

   ### з використанням бібліотеки SciPy, зокрема її функцію quad з підмодуля integrate:
   результат розрахунків:
   0.785398163397448, error: 8.833911380179416e-11

   ### шляхом розрахунку площі фігури за формулою
   площа квадранта кола розраховується за формулою: 
   $$\frac{\pi*r^{2}}{4}$$, 
   для нашого конкретного випадку формула виглядає наступним чином:
   $$\frac{\pi}{4}$$
   результат розрахунків: 
   0.7853981633974483

   ### порівняння результатів:
   Якщо порівнювати результати обчислення значення інтеграла функції за допомогою методу Монте-Карло, за умови проведення 100 експериментів та генерації 15 000 випадкових точок, то різниця між отриманими результатами та точними аналітичними або за допомогою функції quad розрахунками становить 0,0528%.

## Висновки

Значення інтеграла функції, отримане за допомогою методу Монте-Карло, близьке до теоретичного або значення, отриманого чисельним методом, це свідчить про ефективність методу Монте-Карло для цього конкретного інтегралу. Також під час проведення тестів ми підтвердили, що точність методу Монте-Карло залежить від кількості випробувань (експериментів), тож збільшення їх може призвести до точніших результатів.

