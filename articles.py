from storage import liked_articles,disliked_articles,articles
from demographic_filtering import output
from content_filtering import recommendation
from flask import Flask, jsonify, Request
import csv
articles=[]
with open('articles.csv',encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    articles=data[1:]
liked_articles=[]
disliked_articles=[]

app=Flask(__name__)
@app.route("/get-articles",methods=["GET"])
def get_articles():
    artic={
        "timestamp":articles[0][3],
        "url":articles[0][12],
        "title":articles[0][13],
        "text":articles[0][14],
        "lang":articles[0][15],
        "total_events":articles[0][16]

    }
    return jsonify({
        "data":artic[0],
        "status":"succes"
    })
@app.route("/liked-articles",methods=["POST"])
def lliked_articles():
    article=articles[0]
    liked_articles.append(article)
    articles.pop(0)
    return jsonify({
        "status":"succes"
    }),201
@app.route("/disliked-articles",methods=["POST"])
def unliked_articles():
    article=articles[0]
    disliked_articles.append(article)
    articles.pop(0)
    return jsonify({
        "status":"succes"
    }),201
@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for artic in articles:
        _d = {
        "timestamp":articles[1],
        "url":articles[2],
        "title":articles[3],
        "text":articles[4],
        "lang":articles[5],
        "total_events":articles[6]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200
@app.route("/recommended-article")
def recommended_article():
    all_recommended=[]
    for liked_article in liked_articles:
        output=recommendation(liked_article[13])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended=list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data=[]
    for recommended in all_recommended:
        _d = {
            "title": recommended[3],
            "timestamp":recommended[1],
            "url":recommended[2],
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200
if __name__=="__main__":
    app.run()
