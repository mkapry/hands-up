import os
import csv

def csv_writer(csv_path,n_frames,x_coord, y_coord, z_coord,columns):
    '''
    Записывает ключевые точки в csv
    На вход:
        csv_path - путь до файла в виде строки, n_frames - количество кадров, 
        x_coord, y_coord, z_coord - координаты (списками),
        columns - названия колонок (список) 
    На выход:
          0 - успех; 1 - ошибка
    '''
    with open(csv_path, mode='w') as csv_file:
        try:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(columns)
                                
            for i in range(n_frames):
                row = [i] + ['' for _ in range(21*3)]
                for point in handsModule.HandLandmark:
                    index = 1+3 * point
                    row[index]=x_coord[point+i]
                    row[index+1]=y_coord[point+i]
                    row[index+2]=z_coord[point+i]
                csv_writer.writerow(row)
            return 0
        except:
            print('Trouble with writing to csv')
            return 1
        
    