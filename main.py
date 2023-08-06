import pandas as pd
import numpy as np

data = pd.read_csv("data/kaggle/crimes_2001-present.csv")
data_filtered = data.dropna(axis=0,subset=["Location"])
