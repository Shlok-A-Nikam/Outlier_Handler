import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def handle_outliers_iqr_multi(df, columns):
    
    df_copy = df.copy()

    for col in columns:
        plt.figure(figsize=(10,4))

        
        plt.subplot(1,2,1)
        sns.boxplot(x=df_copy[col])
        plt.title(f"{col} - Before")

        
        Q1 = df_copy[col].quantile(0.25)
        Q3 = df_copy[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

       
        outliers = df_copy[(df_copy[col] < lower) | (df_copy[col] > upper)]
        print(f"{col} → Outliers detected: {len(outliers)}")

        
        df_copy[col] = df_copy[col].clip(lower, upper)

        
        plt.subplot(1,2,2)
        sns.boxplot(x=df_copy[col])
        plt.title(f"{col} - After (Capped)")

        plt.tight_layout()
        plt.show()

    return df_copy
