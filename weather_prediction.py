import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("Indian_Climate_Dataset_2024_2025.csv")

df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

original_city = df['City'].copy()

city_encoder = LabelEncoder()
state_encoder = LabelEncoder()
aqi_encoder = LabelEncoder()

df['City'] = city_encoder.fit_transform(df['City'])
df['State'] = state_encoder.fit_transform(df['State'])
df['AQI_Category'] = aqi_encoder.fit_transform(df['AQI_Category'])

X = df[
[
'City',
'State',
'Temperature_Max (°C)',
'Temperature_Min (°C)',
'Humidity (%)',
'Rainfall (mm)',
'Wind_Speed (km/h)',
'AQI',
'AQI_Category',
'Pressure (hPa)',
'Cloud_Cover (%)',
'Year',
'Month',
'Day'
]
]

y = df['Temperature_Avg (°C)']

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X,y)


st.title("🌦️ AI Weather & Ocean Safety Prediction System")

st.write("Machine Learning based weather prediction system for fishermen")


cities = sorted(original_city.unique())

selected_city = st.selectbox(
    "Select City",
    cities
)


city_data = df[
    original_city == selected_city
].iloc[-1]


if st.button("Predict Weather"):


    input_data = city_data[X.columns].values.reshape(1,-1)

    prediction = model.predict(input_data)


    st.success(
        f"🌡️ Predicted Average Temperature: {prediction[0]:.2f} °C"
    )


    st.subheader(
        f"Weather Details - {selected_city}"
    )


    col1, col2 = st.columns(2)


    with col1:


        st.metric(
            "Maximum Temperature",
            f"{city_data['Temperature_Max (°C)']} °C"
        )


        st.metric(
            "Minimum Temperature",
            f"{city_data['Temperature_Min (°C)']} °C"
        )


        st.metric(
            "Humidity",
            f"{city_data['Humidity (%)']} %"
        )


        st.metric(
            "Rainfall",
            f"{city_data['Rainfall (mm)']} mm"
        )


    with col2:


        st.metric(
            "Wind Speed",
            f"{city_data['Wind_Speed (km/h)']} km/h"
        )


        st.metric(
            "AQI",
            city_data['AQI']
        )


        st.metric(
            "Pressure",
            f"{city_data['Pressure (hPa)']} hPa"
        )


        st.metric(
            "Cloud Cover",
            f"{city_data['Cloud_Cover (%)']} %"
        )



    st.divider()


    st.title("🌊 Ocean Current Prediction")


    wind = city_data['Wind_Speed (km/h)']
    rain = city_data['Rainfall (mm)']
    cloud = city_data['Cloud_Cover (%)']


    ocean_current = (
        (wind * 0.05) +
        (rain * 0.02) +
        (cloud * 0.01)
    )


    st.metric(
        "Estimated Ocean Current Speed",
        f"{ocean_current:.2f} m/s"
    )



    if ocean_current < 1.5 and wind < 25 and rain < 20:


        st.success(
            "🟢 SAFE FOR FISHING"
        )


        st.write(
        """
        ✔ Calm ocean condition  
        ✔ Low current speed  
        ✔ Fishermen can go fishing
        """
        )



    elif ocean_current < 3 and wind < 40:


        st.warning(
            "🟡 BE CAREFUL"
        )


        st.write(
        """
        ⚠ Moderate ocean current  
        ⚠ Small boats should be careful  
        ⚠ Check weather before travelling
        """
        )



    else:


        st.error(
            "🔴 DANGEROUS - DO NOT GO FISHING"
        )


        st.write(
        """
        ❌ Strong ocean currents  
        ❌ Unsafe wind conditions  
        ❌ Fishing not recommended
        """
        )




st.sidebar.title("Project Information")


st.sidebar.write(
"""
AI Weather Prediction System

Features:

• Random Forest ML Model  
• Temperature Prediction  
• Rainfall Monitoring  
• AQI Analysis  
• Ocean Current Prediction  
• Fishermen Safety Decision
"""
)