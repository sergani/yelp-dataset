import os
import pandas as pd

from pandas_profiling import ProfileReport

if os.path.exists('./picklejar/df_checkins.pkl'):
    # load the pickle file
    print('Reading pickle file!')
    df_checkins = pd.read_pickle('./picklejar/df_checkins.pkl')

    print('Dataframe shape:', df_checkins.shape)

    # generate the pandas profiling report
    profile = ProfileReport(df_checkins.drop(['business_id', 'date'], axis=1),
                            title='Pandas Profiling Report for Yelp Checkins')

    profile.to_file('./pandas_profiling/checkins.html')

else:
    exit()
