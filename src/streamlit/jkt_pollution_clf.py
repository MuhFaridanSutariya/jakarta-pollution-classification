import os
import streamlit as st
from PIL import Image
import requests
import yaml

current_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(current_dir, '../../config/config.yaml')

# Load the config from the specified file path
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

st.set_page_config(
    page_title="Jakarta Pollution Classification",
    page_icon=":bar_chart:",
    layout="centered"
)

# upload image
img_path = Image.open(config['assets']['img_directory'])
st.image(img_path)
st.title("Jakarta Pollution Classifier")

# create an empty list to store the results
results = []

# Define the stasiun options
stasiun_options = [
    'DKI1 (Bunderan HI)',
    'DKI2 (Kelapa Gading)',
    'DKI3 (Jagakarsa)',
    'DKI4 (Lubang Buaya)',
    'DKI5 (Kebon Jeruk) Jakarta Barat'
]

range_co = [-1, 100]
range_no2 = [-1, 100]
range_o3 = [-1, 160]
range_pm10 = [-1, 800]
range_pm25 = [-1, 400]
range_so2 = [-1, 500]

with st.form(key="jakarta_pollution_form", clear_on_submit=True):
    stasiun = st.selectbox(
        "Select the station:",
        options=stasiun_options,
        help="Example value: DKI1 (Bunderan HI)"
    )

    pm10 = st.number_input(
        label="Enter PM10 value:",
        min_value=range_pm10[0],
        max_value=range_pm10[1],
        help="Example value: 65.0"
    )

    pm25 = st.number_input(
        label="Enter PM2.5 value:",
        min_value=range_pm25[0],
        max_value=range_pm25[1],
        help="Example value: 101.0"
    )

    so2 = st.number_input(
        label="Enter SO2 (Sulfur Dioxide) value:",
        min_value=range_so2[0],
        max_value=range_so2[1],
        help="Example value: 24.0"
    )

    co = st.number_input(
        label="Enter CO (Carbon Monoxide) value:",
        min_value=range_co[0],
        max_value=range_co[1],
        help="Example value: 19.0"
    )

    o3 = st.number_input(
        label="Enter O3 (Ozone) value:",
        min_value=range_o3[0],
        max_value=range_o3[1],
        help="Example value: 19.0"
    )

    no2 = st.number_input(
        label="Enter NO2 (Nitrogen Dioxide) value:",
        min_value=range_no2[0],
        max_value=range_no2[1],
        help="Example value: 41.0"
    )

    submitted = st.form_submit_button("Predict")
    
    if submitted:
        # collect data from form
        form_data = {
            "stasiun": stasiun,
            "pm10": pm10,
            "pm25": pm25,
            "so2": so2,
            "co": co,
            "o3": o3,
            "no2": no2
        }

        # sending the data to the prediction server
        with st.spinner("Sending data to the prediction server... please wait..."):
            res = requests.post("{}".format(config['server']['url']), json=form_data).json()

        # parse the prediction result
        if res['status'] == 200:
            results.append(res['message'])  # add the result to the list of results
            st.success(f"Result: {res['message']}")
        else:
            st.error(f"Error in prediction. Please check your code: {res}")