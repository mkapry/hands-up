import fastdtw
import numpy as np
import pandas as pd

from scipy.ndimage.filters import gaussian_filter
from scipy.signal import *
from scipy.spatial.distance import euclidean

def process_signal(signal):
    '''Обработка прерд DTW
    На вход:
        сигнал (список)
    На выход:
        сигнал (список)
    '''
    signal = gaussian_filter(signal, sigma=1)
    mean = np.mean(signal)
    return [x - mean for x in signal]

def calculate_score(df_1,df_2,c_names,n_dim=3):
    '''Подсчет меры схожести сигналов DTW
    На вход:
        df_1,df_2 - датафреймы с сигналами,
        c_names - названия столбцов в датафреймах (список)
        n_dim - размерность (дефолтно 3D)
    На выход:
        средняя дистанция между последовательностями (float)
    '''
    distance=0.0
    for i in c_names:
        peaks_1,_ = find_peaks(df_1[i])
        peaks_2,_ = find_peaks(df_2[i])
        sig1 = process_signal(signal=peaks_1)
        sig2 = process_signal(signal=peaks_2)
        temp_distance, _ = fastdtw.fastdtw(sig1, sig2, radius=1, dist=euclidean)
        distance+=temp_distance
    return distance/n_dim