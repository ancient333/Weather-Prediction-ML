# AI WEATHER PREDICTION

The AI Weather Prediction System is a machine learning based application designed to predict average temperature using historical Indian climate data. 
The system uses a Random Forest Regression model to analyze different weather and environmental parameters and provide a predicted temperature for the selected city.
The application also displays important weather information such as maximum temperature, minimum temperature, humidity, rainfall, wind speed, AQI, pressure, and cloud cover. 
It also estimates ocean current speed and provides a basic safety recommendation for fishermen based on weather conditions.

# Technologies

* Python
* Streamlit
* Pandas
* Scikit-learn
* Random Forest Regression
* Visual Studio Code
* CSV Dataset

# Features

* Predicts average temperature using Machine Learning.
* Uses a Random Forest Regression model.
* Allows users to select a city.
* Displays maximum and minimum temperature.
* Displays humidity and rainfall information.
* Displays wind speed and AQI.
* Displays pressure and cloud cover.
* Estimates ocean current speed.
* Provides fishing safety recommendations.
* Provides a simple and user-friendly interface using Streamlit.

# Machine Learning Model

The project uses a Random Forest Regression model for predicting the average temperature.

The model uses weather and environmental parameters such as:

* City
* State
* Maximum Temperature
* Minimum Temperature
* Humidity
* Rainfall
* Wind Speed
* AQI
* AQI Category
* Pressure
* Cloud Cover
* Year
* Month
* Day

The target value predicted by the model is the Average Temperature.

Random Forest is used because it can work with multiple input features and can capture relationships between different weather parameters.

# The Process

The system begins by loading historical climate data from the CSV dataset. The date column is converted into a date format, and year, month, and day are extracted from it.

Categorical values such as city, state, and AQI category are converted into numerical values using Label Encoding so that they can be used by the machine learning model.

The selected weather parameters are then used as input features, while the average temperature is used as the target value.

A Random Forest Regression model is trained using the available climate data. When the user selects a city and clicks the prediction button, the latest available weather data for that city is given to the trained model.

The model then predicts the average temperature and displays the result along with other weather details.

The system also calculates an estimated ocean current speed using wind speed, rainfall, and cloud cover. Based on the estimated current, wind speed, and rainfall, the application provides a basic fishing safety recommendation.

# How can it be improved

* Use real-time weather and ocean data through APIs.
* Use real-time ocean current information instead of an estimated value.
* Train the model using a larger and more recent dataset.
* Compare Random Forest with other machine learning algorithms.
* Add weather forecasting for multiple future days.
* Add interactive maps for different locations.
* Improve the fishermen safety system using real-time marine weather data.
* Add automatic weather and safety alerts.
* Deploy the application online so it can be accessed from anywhere.

# Running the project

1. Install Python and Visual Studio Code (VS Code) on your system.

2. Place the project files (`weather_prediction.py` and `Indian_Climate_Dataset_2024_2025.csv`) in the same project folder.

3. Open the project folder in VS Code and open the integrated terminal.

4. Install the required Python libraries using:

```bash
pip install streamlit pandas scikit-learn
```

5. Run the application using:

```bash
python -m streamlit run weather_prediction.py
```

6. The Streamlit application will open in your web browser. You can select a city and click the Predict Weather button to view the predicted temperature, weather details, ocean current estimation, and fishing safety recommendation.

The application will normally be available at:

http://localhost:8501/
