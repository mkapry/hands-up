import argparse
import os
import pandas as pd
import csv

from writer import *
from signal_prosesser import *
from detecter import *

parser = argparse.ArgumentParser()
parser.add_argument('--video', type=str, metavar='VIDEO_PATH', help='video path')
parser.add_argument('--csv_path',type=str, metavar='CSV_PATH', help='where to store csv')
parser.add_argument('--keypoints_1', type=str, metavar='KP_1',help='keypoint_1 csv file')
parser.add_argument('--keypoints_2', type=str,metavar='KP_2',help='keypoint_2 csv file')
def main():

    global args
    args = parser.parse_args()
    x_coord=[]
    y_coord=[]
    z_coord=[]
    columns=[]
    #keypoint detection
    video_path=os.path.normpath(args.video)
    csv_path=os.path.normpath(args.csv_path)
    x_coord, y_coord, z_coord, columns, result = detecter(video_path)
    #calculate similarity for every point
    if args.keypoints_1 and args.keypoints_2:
        df_1=pd.read_csv(args.keypoints_1)
        df_2=pd.read_csv(args.keypoints_2)
        all_dist=[]
        all_dist.append(calculate_score(df_1, df_2, col_n))
        print(all_dist)


if __name__ == '__main__':
    main()

