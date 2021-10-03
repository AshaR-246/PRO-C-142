import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df1=pd.read_csv("articles.csv")
# df1.dropna("title",axis=1,inplace=True)
def lowercase(x):
  if isinstance(x, str):
      return x.lower()
  else:
      return ''
df1["title"] = df1["title"].apply(lowercase)
df1.head()
count=CountVectorizer(stop_words='english')
count_list=count.fit_transform(df1['title'])
cos_sim=cosine_similarity(count_list,count_list)
df1=df1.reset_index()
indices=pd.Series(df1.index,index=df1['contentId'])
def recommendation(contentId,cos_sim):
  ind=indices[contentId]
  sim_score=list(enumerate(cos_sim[ind]))
  sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
  sim_score = sim_score[1:11]
  movie_indices=[i[0] for i in sim_score]
  return df1['contentId'].iloc[movie_indices]
recommendation(-4029704725707465084, cos_sim)
