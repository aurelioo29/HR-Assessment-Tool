# Employee Performance Assessment Website

## Overview

This project is a web application designed to predict employee attrition using machine learning. The application allows users to input various employee attributes and receive a prediction on whether the employee will stay or leave the company.

## Project Structure

## Files and Directories

- **app.py**: The main Flask application file that handles routing, form submissions, and predictions.
- **job_predict.sql**: SQL script to create and populate the `job_data` table in the database.
- **model/final_model.pkl**: The trained machine learning model used for predictions.
- **static/assets/styling.css**: Custom CSS for styling the web application.
- **static/script.js**: JavaScript file for handling form submissions and displaying results.
- **templates/index.html**: HTML template for the web application's user interface.
- **requirements.txt**: List of Python dependencies required for the project.

## Setup and Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/aurelioo29/hr-analytic.git
   cd hr-analytic
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv env
   ```

   - On macOS/Linux:

   ```sh
   source env/bin/activate
   ```

   - On Windows:

   ```sh
   source env/bin/activate
   ```

   Activate environtment

   ```sh
   env\Scripts\activate
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database**:

   - Ensure you have MySQL installed and running.
   - Create a database named `job_predict`.
   - Run the SQL and import our database `job_predict.sql`.

5. **Run the Flask application**:

   ```sh
   python app.py
   ```

6. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Fill out the form with the required employee attributes.
2. Click the "Prediksi" button to get the prediction.
3. The prediction result will be displayed along with the input data and classification report.

## Dependencies

- Flask
- Flask-SQLAlchemy
- MySQL-connector-python
- PyMySQL
- scikit-learn
- numpy
- scipy
- joblib

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
