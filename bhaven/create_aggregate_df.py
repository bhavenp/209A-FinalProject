import os
import pandas as pd

def create_aggregate_df(path):
    files = os.listdir(path);
    if files[0] == '.DS_Store': #ignore the .DS_Store file that may show up first
        files = files[1:];
    full_path = path + files[0]
    result_df = pd.read_csv(full_path, low_memory=False);
    for file in files[1:]:
        if file[0:4] != "Loan":
            continue;
        print(file);
        full_path = path + file;
        new_df = pd.read_csv(full_path);
        result_df = pd.concat([result_df, new_df]);
    return result_df;