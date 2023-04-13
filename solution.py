import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 33217853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы    

    stat, pvalue = ks_2samp(x, y)
    
    alpha = 0.04
    if pvalue < alpha:
        result = True
    else:
        result = False
    
    return result # Ваш ответ, True или False
