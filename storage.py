import csv
articles=[]
with open('articles.csv',encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    articles=data[1:]
liked_articles=[]
disliked_articles=[]
