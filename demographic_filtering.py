import pandas as pd
import numpy as np
df1=pd.read_csv("articles.csv")
# df1.dropna(['title'],axis=1,inplace=True)
df1=df1.sort_values(['total_events'],ascending=[False])
output = df1[['total_event']].head(20).values.tolist()