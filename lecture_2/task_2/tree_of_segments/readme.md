B. Индекс максимума на отрезке
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	4 секунды	1024 Мб	стандартный ввод	стандартный вывод
Kotlin 2.1.20 (JRE 21)	10 секунд	1024 Мб
Swift 6.1	10 секунд	1024 Мб
Python 3.13.2	10 секунд	1024 Мб
Node.js 22.14.0	10 секунд	1024 Мб
Реализуйте структуру данных для эффективного вычисления номера максимального из нескольких подряд идущих элементов массива.

Формат ввода

В первой строке вводится одно натуральное число N ( 1 ⩽ N ⩽ 100 000 ) — количество чисел в массиве.
Во второй строке вводятся N чисел от 1 до 100 000 — элементы массива.
В третьей строке вводится одно натуральное число K ( 1 ⩽ K ⩽ 300 000 ) — количество запросов на вычисление максимума.
В следующих K строках вводится по два числа — номера левого и правого элементов отрезка массива (считается, что элементы массива нумеруются с единицы).

Формат вывода
Для каждого запроса выведите индекс максимального элемента на указанном отрезке массива. Если максимальных элементов несколько, выведите любой их них.

Числа выводите по одному в строке.

Пример
Ввод
5
2 2 2 1 5
2
2 3
2 5

Вывод
3
5
