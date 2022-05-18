import os
import pandas as pd
import csv

from writer import *
from signal_prosesser import *
from detecter import *

def main():

    x_coord=[]
    y_coord=[]
    z_coord=[]
    columns=[]
    #keypoint detection
    x_coord, y_coord, z_coord, columns = detecter(path)
    #calculate similarity for every point
    df_1=pd.read_csv('vid_1.csv')
    df_2=pd.read_csv('vid_2.csv')
    all_dist=[]
    all_dist.append(calculate_score(df_1, df_2, col_n))

