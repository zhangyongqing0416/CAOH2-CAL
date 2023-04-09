import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import pymysql

conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='feigu',db='feigudb',charest='gbk')
