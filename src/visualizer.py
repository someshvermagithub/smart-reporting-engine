import matplotlib
matplotlib.use('Agg')   # IMPORTANT FIX

import matplotlib.pyplot as plt
import seaborn as sns
import os

def ensure_dir():
    os.makedirs("reports", exist_ok=True)

def plot_bar(df, cat, val):
    plt.figure()
    df.groupby(cat)[val].sum().plot(kind='bar')

    file = f"reports/{cat}_{val}.png"
    plt.savefig(file)
    plt.close()
    return file

def plot_corr(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    numeric_df = df.select_dtypes(include='number')

    if numeric_df.shape[1] < 2:
        return None  # Not enough numeric data

    plt.figure()
    sns.heatmap(numeric_df.corr(), annot=True)

    file = "reports/corr.png"
    plt.savefig(file)
    plt.close()

    return file

def generate_charts(df):
    ensure_dir()
    charts = []

    numeric = df.select_dtypes(include='number').columns
    categorical = df.select_dtypes(include='object').columns

    for cat in categorical:
        for num in numeric:
            charts.append(plot_bar(df, cat, num))

    corr_chart = plot_corr(df)
    if corr_chart:
        charts.append(corr_chart)

    return charts