import pandas as pd
import numpy as np
import webbrowser
import os

df = pd.read_csv("data/kaggle/crimes_2001-present.csv")
df = df.dropna(axis=0,subset=["Location"])

filename = "htmlstyler.html"
with open(filename, "w") as f:
    df[0:5].style.to_html(f)

abspath = os.path.abspath(filename)
webbrowser.open(f"file:{abspath}", new = 1)
