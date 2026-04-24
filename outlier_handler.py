import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_boxplot(df, column, title):
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[column])
    plt.title(title)
    plt.xlabel(column)
    plt.show()

def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    return df[(df[column] >= lower) & (df[column] <= upper)]

def visualize_outliers(df, column):
    plot_boxplot(df, column, "Before Outlier Removal")

    df_clean = remove_outliers_iqr(df, column)

    plot_boxplot(df_clean, column, "After Outlier Removal")

    return df_clean