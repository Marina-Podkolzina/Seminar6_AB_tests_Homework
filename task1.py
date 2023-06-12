#Продакт на главной mail.ru решил протестировать в рекомендательной ленте контента вместо карточек со статьями 
#видеоплеер с короткими видео. 
#Нынешний таймспент на юзера в день в среднем равен 25 минут,
#а стандартная ошибка (SD) равна 156. Мы предполагаем, что в новой версии таймспент на юзера в день изменится на 10%. 
#Средний трафик 20000 человек в день. Посчитайте сколько дней необходимо держать эксперимент при alpha = 5% и beta = 20% .

#Решение:

import numpy as np
from scipy.stats import norm, t

n = 20000  # Средний трафик в день
sd = 156  # SD
alpha = 0.05  # уровень значимости
beta = 0.2  # вероятность ошибки второго рода
prop_diff = 0.1  # относительное изменение таймспента

se = sd / np.sqrt(n)  # стандартная ошибка среднего
m = se * norm.ppf(1 - alpha/2)  # граница для доверительного интервала
delta = prop_diff * n  # абсолютное изменение таймспента

z_alpha = norm.ppf(1 - alpha)  
z_beta = norm.ppf(1 - beta) 

n_1 = (z_alpha*m + z_beta*sd/delta)**2
n_2 = (z_alpha*m - z_beta*sd/delta)**2
n_round = np.ceil(max(n_1, n_2))
days = np.ceil(n_round/n)  # количество дней

print(f"Необходимо собрать данные в течении {int(days)} дней")


#Ответ: Необходимо собрать данные в течении 1 дней