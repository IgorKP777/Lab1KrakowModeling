import math as m
import random as r
import statistics as s

if __name__ == '__main__':
    n = 1000

    selection = [3 * r.uniform(0, 1) for i in range(n)]

    average = s.mean(selection)

    variance = s.variance(selection)

    standardDeviation = m.sqrt(variance)

    delta = 1.96 * standardDeviation / m.sqrt(n)

    x1, x2 = average - delta, average + delta

    print('Оценка математического ожидания\n', round(average, 3), sep='')
    print('Оценка дисперсии\n', round(variance, 3), sep='')
    print('Оценка среднеквадратического отклонения\n', round(standardDeviation, 3), sep='')
    print('Интервальная оценка\n', '(', round(x1, 3), ', ', round(x2, 3), ')', sep='')
    print('Точечная оценка\n', round((x1 + x2) / 2, 3), sep='')
