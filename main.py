import pandas as pd
import numpy as np
import webbrowser
import os

df = pd.read_csv("data/kaggle/crimes_2001-present.csv")
df = df.dropna(axis=0,subset=["Location"])
df_prune = df.drop(["Case Number",
                    "Block",
                    "Primary Type",
                    "Description",
                    "FBI Code",
                    "X Coordinate",
                    "Y Coordinate",
                    "Year",
                    "Updated On",
                    "Location"], axis=1)

filename = "htmlstyler.html"
with open(filename, "w") as f:
    df_prune[0:21].style.to_html(f)

abspath = os.path.abspath(filename)
webbrowser.open(f"file:{abspath}", new = 1)
