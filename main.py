import math as m
import random as r
import statistics as s

if __name__ == '__main__':
    sampleSize = 1000

    selection = [3 * r.uniform(0, 1) for i in range(sampleSize)]

    average = s.mean(selection)

    variance = s.variance(selection)

    standardDeviation = m.sqrt(variance)

    delta = 1.96 * standardDeviation / m.sqrt(sampleSize)

    x1 = average - delta
    x2 = average + delta

    print('Оценка математического ожидания\n', round(average, 3))
    print('Оценка дисперсии\n', round(variance, 3))
    print('Оценка среднеквадратического отклонения\n', round(standardDeviation, 3))
    print('Интервальная оценка\n', '(', round(x1, 3), ',', round(x2, 3), ')')
    print('Точечная оценка\n', round((x1 + x2) / 2, 3))
