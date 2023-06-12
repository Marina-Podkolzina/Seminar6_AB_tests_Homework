#Наша продуктовая команда в ecommerce магазине планирует запустить тест, направленный на ускорение загрузки сайта.
#Одна из основных метрик bounce rate в GA = 40%. Мы предполагаем, что при оптимизации сайта она изменится минимум на 20%.
#Средний трафик 4000 человек в день. Посчитайте сколько нам нужно дней держать эксперимент при alpha = 5% и beta = 20%

#Решение:
#mean1 - текущее значение bounce rate (40%)   
#mean2 - ожидаемое изменение bounce rate после оптимизации сайта (-20%)
#alpha - уровень значимости (0.05)
#beta - мощность теста (0.2)
#baseline - текущее значение bounce rate (40%)


import math
import scipy.stats as stats

def sample_size(mean1, mean2, alpha, beta, power, baseline):      
    std1 = math.sqrt(baseline * (1 - baseline))                 
    z_alpha = stats.norm.ppf(1 - alpha / 2)                     
    z_beta = stats.norm.ppf(power)                              
    std2 = std1 * math.sqrt((baseline - mean2) ** 2 / (mean1 - mean2) ** 2)
    return ((std1 * z_alpha + std2 * z_beta) / (mean1 - mean2)) ** 2


print(round(sample_size(mean1=0.4, mean2=-0.2, alpha=0.05, beta=0.2, power=0.8, 
                  baseline=0.4)))

#Ответ:

#5 дней нам нужно держать эксперимент при alpha = 5% и beta = 20%