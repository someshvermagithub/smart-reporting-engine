def clean_data(df):
    df = df.copy()  # 🔥 FIX

    df = df.drop_duplicates()

    for col in df.columns:
        if df[col].dtype == 'object':
            df.loc[:, col] = df[col].fillna("Unknown")
        else:
            df.loc[:, col] = df[col].fillna(df[col].median())

    return df