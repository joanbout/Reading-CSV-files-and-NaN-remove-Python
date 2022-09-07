#Importing the required modules
import glob2
import pandas as pd
import os
import glob
import pathlib
import re
import csv
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
  
#Specifying the path to csv files
path = pathlib.Path().resolve() # use your path
path = str(path)
print(path)
total_path = Path(path).glob('**/*.csv')
  
#Defining an empty list to store content
data_frame = pd.DataFrame()
content = []

#CSV files in the path
files = [str(file) for file in total_path if file.is_file()]
##print(files)

#Loop for reading all the csv files in the specified path
for i, filename in  enumerate(files):
     #Reading content of csv file
      content.append(filename)
      df = pd.read_csv(filename, index_col=None)
      ##print(df)
      content.append(df)
#Printing the columns of the dataframe
      df_columns=df.columns
      ##print(df_columns)
#Replacing NaT values with 0
      df= df.replace('NaT', '0')
#Replacing Not Applicable label with 0
      df= df.replace('NotApplicable', '0')
      ##df1=df.iloc[10:20, 10:13]
      ##print(df1)
#Removing NaN values from columns
      df = df.dropna(axis="columns", how="any")
      ##print(df)
      
