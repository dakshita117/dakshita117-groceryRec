from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
top_n = pickle.load(open("Pickle/topn.p", "rb"))
dep = pickle.load(open("Pickle/dep.p", "rb"))
rec_df = pickle.load(open("Pickle/recdf.p", "rb"))
high_volume = pickle.load(open("Pickle/highvol.p", "rb"))
cosine_dists = pickle.load(open("Pickle/cosinedists.p", "rb"))
key_list = list(cosine_dists.columns)


def recommendersystem(user_id):
    u = high_volume.groupby(['user_id', 'product_name']).size(
    ).sort_values(ascending=False).unstack().fillna(0)
    u_sim = pd.DataFrame(cosine_similarity(u), index=u.index, columns=u.index)

    p = high_volume.groupby(['product_name', 'user_id']).size(
    ).sort_values(ascending=False).unstack().fillna(0)

    recommendations = pd.Series(
        np.dot(p.values, cosine_dists[user_id]), index=p.index)
    return recommendations.sort_values(ascending=False).head(15)


def prediction(person):

    val = top_n[person]
    val1 = []
    for i in range(len(val)):
        val1.append(val[i][0])
    user = dep.loc[dep['product_id'].isin(val1)]
    pn = user['product_name']
    lst = list(pn)
    lst2 = list(recommendersystem(person).keys())
    for item in lst2:
        if item not in lst:
            lst.append(item)
    return lst


def most_ordered(person):
    namee = rec_df[rec_df['user_id'] == person]  # imppp
    mer = pd.merge(namee, dep, on='product_id')
    return list(mer.product_name)


@app.route("/")
def index():
    return render_template('home.html')
    # return prediction(14293)


@app.route('/predict', methods=['POST'])
def predict():
    user = request.form['a']
    user = int(user)
    user_id = key_list[user]
    user_id = int(user_id)
    pred = prediction(user_id)
    ordered = most_ordered(user_id)
    return render_template('out_prediction.html', pred=pred, orders=ordered)


# if __name__ == "__main__":
app.run(debug=True)
