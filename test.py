#coding=utf-8

import pandas as pd #数据分析
import numpy as np   #科学计算
from pandas import Series,DataFrame
import os

base_dir =  os.path.dirname(os.path.relpath(__file__))

def test():
    data_train = pd.read_csv(os.path.join(base_dir,'resource','train.csv'))
    print data_train.head()


if __name__ == '__main__':
    test()
