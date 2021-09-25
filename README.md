

# Project Design

Performed Data Cleaning, merged tables together and did Exploratory Data Analysis (EDA).
Analyzed customer behaviour, generated insights and built data visualizations.
Defined a metric for model evaluation.
Created a shopping cart recommender system to recommend items to customers based on their purchase history.


# Recommendation Model

Using Singular Value Decomposition (SVD), we developed a "model-based" recommendation system that generates predictions about a user's rating of a previously ordered item. Rather than taking ratings directly from the user like in the movie recommendation system, We used the frequency of purchase of an item as an implicit rating, We chose to use the number of times a user has purchased an item as a stand-in for an actual rating. On a scale of 1 to 5, the rating was given. For each user, we produced a personalised re-ranking of recommended products.

To add variety to recommended products and successfully recommend products to even users who have relatively less order history, we designed a model to first find out the customers that have reordered before and the items that have been reordered before. Then calculate the cosine similarity between all those users and products. Then generate a list of 8 recommendations.




# Files

DataOverview (Notebook) - In this file, we performed EDA on data to achieve certain insights and statistical measures that are essential for the recommendation model. And to define and refine our important features variable selection, that will be used in our model.

Flipkart_SmartBag(Notebook) - Imported all relevant packages and data files and implemented our recommendation model.

App.py - Flask app containing functions to extract recommendations and previous order history from Pickle folder according to the username entered in the home.html page. The data is then sent to the out_prediction.html page for display.









