from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd

def read_data(file_path):
    column_names = ['speed', 'acc_x', 'acc_y', 'acc_z', 'acc_mag', 'gyro_x', 'gyro_y', 'gyro_z',"gyro_mag"]
    data = pd.read_csv(file_path, header=None, names=column_names)
    return data


if __name__ == '__main__':
    dataset = read_data('./data/final.csv')