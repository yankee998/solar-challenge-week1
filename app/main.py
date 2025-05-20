import streamlit as st
from utils import load_data, plot_boxplot, get_top_regions
import matplotlib.pyplot as plt
from io import BytesIO

# Load data
data = load_data()

# Title
st.title("Solar Potential Dashboard")

# Sidebar for country selection
st.sidebar.header("Filter Options")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=['Benin', 'Sierra Leone', 'Togo'],
    default=['Benin', 'Sierra Leone', 'Togo']
)
filtered_data = data[data['Country'].isin(selected_countries)]

# Metric selection
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Display boxplot
if filtered_data.empty:
    st.warning("No data available for selected countries.")
else:
    plot_buf = plot_boxplot(filtered_data, metric)
    st.image(plot_buf, caption=f'{metric} Boxplot', use_column_width=True)

# Top regions table
st.subheader("Top Regions by Average Metric")
top_regions = get_top_regions(filtered_data, metric)
st.table(top_regions)

# Interactive button to refresh or customize
if st.button("Refresh Visualization"):
    st.experimental_rerun()

# Add a slider for number of top regions
n_regions = st.slider("Number of Top Regions", min_value=1, max_value=5, value=3)
top_regions = get_top_regions(filtered_data, metric, n=n_regions)
st.subheader(f"Top {n_regions} Regions by Average {metric}")
st.table(top_regions)