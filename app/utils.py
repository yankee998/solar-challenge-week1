import pandas as pd

def load_data():
    # Adjust path to read from notebooks/data/ relative to app/
    benin_df = pd.read_csv('../notebooks/data/benin_clean.csv')
    sierra_leone_df = pd.read_csv('../notebooks/data/sierra_leone_clean.csv')
    togo_df = pd.read_csv('../notebooks/data/togo_clean.csv')
    benin_df['Country'] = 'Benin'
    sierra_leone_df['Country'] = 'Sierra Leone'
    togo_df['Country'] = 'Togo'
    return pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)

def plot_boxplot(data, metric):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import io
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Country', y=metric, data=data)
    plt.title(f'{metric} by Country')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf

def get_top_regions(data, metric, n=3):
    # Placeholder: Using Country as proxy for regions
    top = data.groupby('Country')[metric].mean().sort_values(ascending=False).head(n)
    return top.to_frame().reset_index()
# utils.py