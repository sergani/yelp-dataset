import os
import pandas as pd

from pandas_profiling import ProfileReport

if os.path.exists('./picklejar/df_reviews.pkl'):
    # load the pickle file
    print('Reading pickle file!')
    df_reviews = pd.read_pickle('./picklejar/df_reviews.pkl')

    print('Dataframe shape:', df_reviews.shape)

    # generate the pandas profiling report
    profile = ProfileReport(df_reviews.drop(['review_id', 'user_id', 'business_id', 'yelping_since',
                            'friends', 'elite'], axis=1),
                            title='Pandas Profiling Report for Yelp Reviews',
                            minimal=True,
                            lazy=True)

    profile.to_file('./pandas_profiling/reviews.html')

else:
    exit()