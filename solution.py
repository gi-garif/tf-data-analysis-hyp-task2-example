import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 33217853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы    

    # загрузка выборок
    hist_data = pd.read_csv("/historical_data.csv")
    test_data_1 = pd.read_csv("/modified_data_of_type_1.csv")
    test_data_2 = pd.read_csv("/modified_data_of_type_2.csv")
    test_data_3 = pd.read_csv("/modified_data_of_type_3.csv")

    hist = hist_data.iloc[0].to_list()
    test1 = test_data_1.iloc[0].to_list()
    test2 = test_data_2.iloc[0].to_list()
    test3 = test_data_3.iloc[0].to_list()
    
    # расчет статистики критерия и p-value для каждой пары выборок
    stat_1, pvalue_1 = ks_2samp(hist, test1)
    stat_2, pvalue_2 = ks_2samp(hist, test2)
    stat_3, pvalue_3 = ks_2samp(hist, test3)

    # проверка гипотезы однородности на уровне значимости 0.04
    alpha = 0.04
    if pvalue_1 < alpha or pvalue_2 < alpha or pvalue_3 < alpha:
        result = True
    else:
        result = False
    
    return result # Ваш ответ, True или False
