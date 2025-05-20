# Solar Dashboard Development

## Overview
This directory contains scripts and documentation for the Solar Potential Dashboard built with Streamlit.

## Usage Instructions
1. **Install Dependencies**:
   - Ensure a Python virtual environment is activated.
   - Install required packages:
     ```bash
     pip install streamlit pandas numpy matplotlib seaborn scipy
     ```
   - Update `requirements.txt` in the root directory with these dependencies.

2. **Run the Dashboard**:
   - Navigate to the `app` directory:
     ```bash
     cd app
     ```
   - Start the Streamlit app:
     ```bash
     streamlit run main.py
     ```
   - Access the dashboard at `http://localhost:8501` in your browser.

3. **Interact with the Dashboard**:
   - Use the sidebar to select countries and metrics (GHI, DNI, DHI).
   - Adjust the slider to view the top N regions by average metric.
   - Click "Refresh Visualization" to update the display.

## Development Process
- Created `dashboard-dev` branch to isolate dashboard development.
- Designed folder structure with `app/` for the Streamlit app and `scripts/` for documentation.
- Implemented interactive widgets (multiselect, selectbox, slider, button) for user customization.
- Planned deployment to Streamlit Community Cloud after local testing.

## Notes
- The app reads cleaned CSVs from `notebooks/data/`. Ensure these files are present locally.
- Placeholder data loading in `utils.py` assumes cleaned CSVs are available.