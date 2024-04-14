# Heart Disease Prediction ML Project

Welcome to the Heart Disease Prediction ML Project! This project leverages machine learning techniques to predict the risk of heart disease in individuals based on health data. The project includes a user-friendly Streamlit app that provides an interactive experience for making predictions and visualizing data.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

## Overview
The project utilizes machine learning algorithms such as logistic regression, decision trees, and support vector machines to assess medical data and provide predictions on heart disease risk. The Streamlit app offers a convenient interface for inputting health data and viewing predictions.

## Features
- **Interactive Predictions**: Use the Streamlit app to input health data and receive heart disease risk predictions in real-time.
- **Data Visualization**: Explore visualizations of health data and model performance for better understanding.
- **Customizable Models**: Experiment with different machine learning models and parameters to optimize predictions.

## Usage
To run the Streamlit app, use the following command:
```bash
streamlit run app.py
```
The app will open in your default web browser at `http://localhost:8501`.

## Data Sources
The project uses a publicly available dataset on heart disease, which includes features such as age, cholesterol levels, blood pressure, and other medical history data. Please refer to the code and documentation for more details on data sources.

## Project Structure
- `app.py`: Main Streamlit app for the prediction system.
- `data/`: Directory containing datasets used for model training and testing.
- `models/`: Directory containing trained models and related code.
- `notebooks/`: Jupyter notebooks for data exploration and model development.

## Technologies Used
- Python
- Streamlit
- scikit-learn
- pandas
- numpy
- matplotlib (for data visualization)
- Other libraries and frameworks 
