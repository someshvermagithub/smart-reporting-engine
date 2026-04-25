def generate_kpis(df):
    kpis = {}
    for col in df.select_dtypes(include='number'):
        kpis[col] = {
            "mean": round(df[col].mean(), 2),
            "sum": round(df[col].sum(), 2)
        }
    return kpis


def generate_insights(df):
    insights = []

    for col in df.select_dtypes(include='number'):
        if df[col].mean() > df[col].median():
            insights.append(f"{col} shows presence of high-value outliers")

    return insights