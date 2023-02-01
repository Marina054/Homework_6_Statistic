# В результате 10 независимых измерений некоторой величины Х, выполненых с одинаковой точностью, получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предпологая, что результаты измерений подченены нормальному закону распределения вероятностей, оценить истинное 
# значеие величины Х при помощи доверительного интервала, покрывающего это значение с доверительной вероятностью 0,95.

import numpy as np
import scipy.stats as stats
a = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]) # Для решения применяем формулу если сигма ген. совок неизестна
x= np.mean(a) # 6.59
D = np.var(a, ddof = 1) # 0.2032222222222223 нашли несмещенную дисперсию
t1 = stats.t.ppf(0.975, 9) # 2.2621571627409915 
otr =  x - t1 * np.sqrt(D / 10) 
pol = x + t1 * np.sqrt(D / 10)
print([otr, pol]) # [6.267515851415713, 6.912484148584288]
