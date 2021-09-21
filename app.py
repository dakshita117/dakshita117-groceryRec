from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
top_n = pickle.load(open("Pickle/topn.p", "rb"))
dep = pickle.load(open("Pickle/dep.p", "rb"))
rec_df = pickle.load(open("Pickle/recdf.p", "rb"))
key_list = list(top_n.keys())


def prediction(person):
    val = top_n[person]
    val1 = []
    for i in range(len(val)):
        val1.append(val[i][0])
    user = dep.loc[dep['product_id'].isin(val1)]
    pn = user['product_name']
    lst = list(pn)
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
