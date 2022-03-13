import math as m
import random as r
import statistics as s
from prettytable import PrettyTable as pt

if __name__ == '__main__':
    n = 1000

    selection = [3 * r.uniform(0, 1) for i in range(n)]

    average = s.mean(selection)

    variance = s.variance(selection)

    standardDeviation = m.sqrt(variance)

    delta = 1.96 * standardDeviation / m.sqrt(n)

    x1, x2 = average - delta, average + delta

    table_result = pt()
    table_result.title = 'Результаты'
    table_result.field_names = ['Параметры оценки', 'Результат']
    table_result.add_row(['Оценка математического ожидания', round(average, 3)])
    table_result.add_row(['Оценка дисперсии', round(variance, 3)])
    table_result.add_row(['Оценка среднеквадратического отклонения', round(standardDeviation, 3)])
    table_result.add_row(['Интервальная оценка', '(' + str(round(x1, 3)) + ', ' + str(round(x2, 3)) + ')'])
    table_result.add_row(['Точечная оценка', round((x1 + x2) / 2, 3)])

    print(table_result)
