import os
import pandas as pd

from pandas_profiling import ProfileReport

if os.path.exists('./picklejar/df_tips.pkl'):
    # load the pickle file
    print('Reading pickle file!')
    df_tips = pd.read_pickle('./picklejar/df_tips.pkl')

    print('Dataframe shape:', df_tips.shape)

    # generate the pandas profiling report
    profile = ProfileReport(df_tips.drop(['user_id', 'business_id', 'text', 'yelping_since',
                            'elite', 'friends'], axis=1), title='Pandas Profiling Report for Yelp Tips')

    profile.to_file('./pandas_profiling/tips.html')

else:
    exit()
