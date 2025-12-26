import pandas as pd
import os
from datetime import datetime

def load_data():
    files = os.listdir("data/historical")
    data = pd.DataFrame()
    for file in files:
        df = pd.read_csv(os.path.join("data/historical", file))
        df['datetime'] = pd.to_datetime(df['datetime'])
        data = pd.concat([data, df])
    data.sort_values('datetime', inplace=True)
    return data
