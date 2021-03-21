import csv
import os
import pandas as pd

# calculate here how big the price difference is and where the market is going

# dirname = os.path.dirname(__file__)

def last_row_info(param):
    # read the last line of the csv
    # last_row():
    results_df = pd.read_csv('../starthack2021-coffeelion-alpiq/results/results.csv')
    # last_row_df = results_df.tail(1)
    # text = str(text)
    # price = last_row[text]
    # return last_row_df[param]
    return results_df[param].iloc[-1]

print(last_row_info('price'))

# Energy sold


# difference


# create alert