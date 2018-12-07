import os
import pandas as pd


def create_aggregate_df(path, prefix):
    '''
    path: the path file path to folder in which the LoanStats or RejectStats is contained
    prefix: either 'Loan' or 'Reject'
    '''
    files = os.listdir(path);
    result_df = None;
    result_df_empty = True; #check for if dataframe is empty

    for file in files:
        if file[0:len(prefix)] != prefix: #skip files that don't meet our prefix 
            continue;
        full_path = path + file;
        print("Added ", file);
        if result_df_empty: #if a file has not been imported yet
            result_df = pd.read_csv(full_path, low_memory=False);
            result_df_empty = False;
            continue;
        #adding more to result_df
        new_df = pd.read_csv(full_path, low_memory=False);
        result_df = pd.concat([result_df, new_df]);
    return result_df;