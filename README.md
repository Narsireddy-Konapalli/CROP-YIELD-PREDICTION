# Crop Yield Prediction

This project aims to predict crop yield based on environmental factors such as temperature, rainfall, humidity, soil type, weather condition, and crop type. The model used for this task is a RandomForest Regressor, and it has been hyperparameter-tuned using GridSearchCV for better performance. The interface is built using Streamlit, allowing users to input data and predict crop yield easily.

## Installation

Follow the steps below to set up and run the project locally:

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Narsireddy-Konapalli/CROP-YIELD-PREDICTION.git
    cd crop-yield-prediction
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    venv\Scripts\activate  # For Windows
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file includes the following libraries:

    ```txt
    streamlit
    pandas
    scikit-learn
    numpy
    matplotlib
    ```

4. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

## Dataset Features

The dataset used for predicting crop yield contains the following features:

- **Temperature (°C)**: The average temperature of the region in degrees Celsius.
- **Rainfall (mm)**: The amount of rainfall (in millimeters) in the region.
- **Humidity (%)**: The average humidity in percentage.
- **Soil Type**: The type of soil (categorical values):
    - ['Sandy', 'Loamy', 'Peaty', 'Clay', 'Silty']
- **Weather Condition**: The current weather condition (categorical values):
    - ['Sunny', 'Rainy', 'Stormy', 'Cloudy']
- **Crop Type**: The type of crop to be grown (categorical values):
    - ['Barley', 'Corn', 'Wheat', 'Soybeans', 'Rice']

## How It Works

1. **Data Preprocessing**: 
   - The dataset is cleaned and preprocessed to handle missing values and categorical data.
   - Categorical features such as `Soil Type`, `Weather Condition`, and `Crop Type` are encoded using one-hot encoding.

2. **Model Building**:
   - A RandomForest Regressor model is trained on the preprocessed dataset to predict the crop yield.
   - Hyperparameter tuning is performed using **GridSearchCV** to find the best combination of parameters for the model, improving its accuracy.

3. **Streamlit Interface**:
   - The Streamlit app provides an easy-to-use interface where users can input values for temperature, rainfall, humidity, soil type, weather condition, and crop type.
   - Once the inputs are provided, the model predicts the crop yield.

## Usage

1. Run the Streamlit app as described in the **Installation** section.
2. Open the provided local URL (usually `http://localhost:8501`) in your browser.
3. In the app interface:
   - Input the values for temperature, rainfall, humidity, soil type, weather condition, and crop type.
   - The app will display the predicted crop yield based on the input values.

## Interface
![crop](https://github.com/user-attachments/assets/366483ec-972e-48de-85d0-d2ef6e05818a)<br>

The Streamlit interface allows users to input the following features:

- **Temperature (°C)**
- **Rainfall (mm)**
- **Humidity (%)**
- **Soil Type**: Dropdown with options ['Sandy', 'Loamy', 'Peaty', 'Clay', 'Silty']
- **Weather Condition**: Dropdown with options ['Sunny', 'Rainy', 'Stormy', 'Cloudy']
- **Crop Type**: Dropdown with options ['Barley', 'Corn', 'Wheat', 'Soybeans', 'Rice']

Once all the inputs are provided, the model predicts the crop yield and displays the result.

## Hyperparameter Tuning with GridSearchCV

GridSearchCV was used to tune the hyperparameters of the RandomForest Regressor. Some of the parameters tuned include:

- `n_estimators`: Number of trees in the forest.
- `max_depth`: The maximum depth of the tree.
- `min_samples_split`: The minimum number of samples required to split an internal node.
- `min_samples_leaf`: The minimum number of samples required to be at a leaf node.


## Acknowledgments

- **Scikit-learn** for providing the RandomForest Regressor and GridSearchCV functionalities.
- **Streamlit** for building the user interface.
- **Pandas** and **NumPy** for data handling and preprocessing.
- **Matplotlib** for visualization.

---





