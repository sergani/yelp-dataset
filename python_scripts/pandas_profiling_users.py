import datetime
import graphviz
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
import plotly
import plotly.express as px
import re
import seaborn as sns
import swifter
import tensorflow_decision_forests as tfdf

from collections import Counter
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from lazypredict.Supervised import LazyRegressor
from matplotlib import ticker
from mlxtend.evaluate import bias_variance_decomp
from pandas_profiling import ProfileReport
from sklearn import linear_model
from sklearn import metrics
from sklearn import metrics
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import VotingClassifier
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils._testing import ignore_warnings
from tabulate import tabulate
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from xgboost import XGBClassifier

# load the users JSON file
if os.path.exists('./picklejar/df_users.pkl'):
    print('Reading pickle file!')
    df_users = pd.read_pickle('./picklejar/df_users.pkl')

else:
    print('Reading the full JSON file from disk - this may take long!')
    df_users = pd.read_json('./dataset/user.json',
                            lines=True, convert_dates=True)

    # we need to know the count of years each user has been an elite
    df_users['elite_count'] = df_users['elite'].apply(
        lambda x: len(x.split(',')))

    # we need to know the number of friends of each user
    df_users['friends_count'] = df_users['friends'].apply(
        lambda x: len(x.split(',')))

    # let's add a new column for the number of years this user has been yelping
    df_users['yelping_since_year_count'] = df_users['yelping_since'].map(years)

    # store the users dataframe to a pickle file for quicker loading next time
    df_users.to_pickle('./picklejar/df_users.pkl')

print('Dataframe shape:', df_users.shape)

profile = ProfileReport(
    df_users.drop(['yelping_since', 'elite', 'friends'], axis=1), title='Pandas Profiling Report for Yelp Users')

profile.to_file('./pandas_profiling/users.html')
