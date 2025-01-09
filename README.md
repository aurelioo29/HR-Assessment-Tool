# ⚖️ HR Assessment Tool ⚖️ 

## 🌟 Overview

HR Assessment Tool is a web application designed to help HR departments assess employee performance and decide whether employees should stay with the company or be considered for leave, based on various performance metrics.

## 📂 Project Structure

### Files and Directories

- **app.py**: Main Flask application file for routing, form submissions, and predictions.
- **job_predict.sql**: SQL script for creating and populating the `job_data` table in the database.
- **model/final_model.pkl**: Trained machine learning model used for employee performance predictions.
- **static/assets/styling.css**: Custom CSS for styling the web application.
- **static/script.js**: JavaScript for form handling and result display.
- **templates/index.html**: HTML template for the user interface.
- **requirements.txt**: List of Python dependencies for the project.

## ⚙️ Setup and Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/aurelioo29/HR-Assessment-Tool.git
   ```

   ```sh
   cd HR-Assessment-Tool
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
   env\Scripts\activate
   ```

3. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up the database**:

   - Ensure MySQL is installed and running.
   - Create a database named `job_predict`.
   - Import `job_predict.sql` into the database.

5. **Run the Flask application**:

   ```sh
   python app.py
   ```

6. **Access the application**:

   Open your web browser and navigate to `http://127.0.0.1:5000`. 🌐

## 📝 Usage

1. Fill out the form with employee attributes. 🏥
2. Click the "**Prediksi**" button for the prediction. 🔮
3. The result will be shown along with the input data and classification report. 📊

## 📦 Dependencies

This project uses the following dependencies:

- Flask
- Flask-SQLAlchemy
- MySQL-connector-python
- PyMySQL
- scikit-learn
- numpy
- scipy
- joblib

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request. ✨
