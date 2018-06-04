# coding: utf-8

import gc
from sklearn.model_selection import KFold


def process_kfold(df, kfold_processor, n_splits=3, shuffle=False, random_state=777):
    kf = KFold(n_splits, shuffle=shuffle, random_state=random_state)
    k = 1
    for train_index, test_index in kf.split(df):
        kfold_processor(k, df.iloc[train_index], df.iloc[test_index])
        k += 1
        gc.collect()
