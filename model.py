"""
California Housing, End to End with Scikit-Learn

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - load_housing
import os
import tarfile
import tempfile
import urllib.request
import pandas as pd

def load_housing():
    # TODO: Download housing.tgz once into tempfile.gettempdir() and read housing/housing.csv from it.
    url = 'https://github.com/ageron/data/raw/main/housing.tgz'
    path = os.path.join(tempfile.gettempdir(), 'housing.tgz')
    
    if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)
    
    with tarfile.open(path) as tar:
        with tar.extractfile('housing/housing.csv') as f:
            df = pd.read_csv(f)
    return df

# Step 2 - income_categories
def income_categories(df):
    # TODO: pd.cut median_income with edges [0, 1.5, 3, 4.5, 6, inf] and labels 1..5; return an int Series.
    return pd.cut(df["median_income"], bins=[0.0, 1.5, 3, 4.5, 6, np.inf], labels=[1, 2, 3, 4, 5]).astype(int)

# Step 3 - stratified_split
import sklearn

def stratified_split(df, test_size=0.2, random_state=42):
    # TODO: train_test_split stratified on income_categories(df); return (train_set, test_set).
    X_train, X_test = sklearn.model_selection.train_test_split(df, test_size=test_size, random_state=random_state, stratify=income_categories(df))
    return (X_train, X_test)

# Step 4 - explore_correlations (not yet solved)
# TODO: implement

# Step 5 - add_ratio_features (not yet solved)
# TODO: implement

# Step 6 - split_features_labels (not yet solved)
# TODO: implement

# Step 7 - ClusterSimilarity (not yet solved)
# TODO: implement

# Step 8 - numeric_pipeline (not yet solved)
# TODO: implement

# Step 9 - categorical_pipeline (not yet solved)
# TODO: implement

# Step 10 - build_preprocessing (not yet solved)
# TODO: implement

# Step 11 - rmse (not yet solved)
# TODO: implement

# Step 12 - dummy_baseline_rmse (not yet solved)
# TODO: implement

# Step 13 - cross_val_rmse (not yet solved)
# TODO: implement

# Step 14 - linear_model (not yet solved)
# TODO: implement

# Step 15 - forest_model (not yet solved)
# TODO: implement

# Step 16 - random_search (not yet solved)
# TODO: implement

# Step 17 - test_rmse (not yet solved)
# TODO: implement

# Step 18 - bootstrap_rmse_ci (not yet solved)
# TODO: implement

# Step 19 - feature_importances (not yet solved)
# TODO: implement

# Step 20 - worst_errors (not yet solved)
# TODO: implement

# Step 21 - save_and_reload (not yet solved)
# TODO: implement

# Step 22 - predict_new (not yet solved)
# TODO: implement

