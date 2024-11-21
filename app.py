from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/job_predict'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class JobData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    business_travel = db.Column(db.Integer)
    department = db.Column(db.Integer)
    distance_from_home = db.Column(db.Integer)
    education = db.Column(db.Integer)
    education_field = db.Column(db.Integer)
    environment_satisfaction = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    job_involvement = db.Column(db.Integer)
    job_level = db.Column(db.Integer)
    job_role = db.Column(db.Integer)
    job_satisfaction = db.Column(db.Integer)
    marital_status = db.Column(db.Integer)
    monthly_income = db.Column(db.Integer)
    salary_slab = db.Column(db.Integer)
    overtime = db.Column(db.Integer)
    total_working_years = db.Column(db.Integer)
    work_life_balance = db.Column(db.Integer)
    years_at_company = db.Column(db.Integer)
    years_in_current_role = db.Column(db.Integer)
    prediction_result = db.Column(db.String(50))

model_path = 'model/final_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            age = request.form.get('age')
            business_travel = request.form.get('business_travel')
            department = request.form.get('department')
            distance_from_home = request.form.get('distance_from_home')
            education = request.form.get('education')
            education_field = request.form.get('education_field')
            environment_satisfaction = request.form.get('environment_satisfaction')
            gender = request.form.get('gender')
            job_involvement = request.form.get('job_involvement')
            job_level = request.form.get('job_level')
            job_role = request.form.get('job_role')
            job_satisfaction = request.form.get('job_satisfaction')
            marital_status = request.form.get('marital_status')
            monthly_income = request.form.get('monthly_income')
            salary_slab = request.form.get('salary_slab')
            overtime = request.form.get('overtime')
            total_working_years = request.form.get('total_working_years')
            work_life_balance = request.form.get('work_life_balance')
            years_at_company = request.form.get('years_at_company')
            years_in_current_role = request.form.get('years_in_current_role')

            if not all([age, business_travel, department, distance_from_home, education, education_field, environment_satisfaction, gender, job_involvement, job_level, job_role, job_satisfaction, marital_status, monthly_income, salary_slab, overtime, total_working_years, work_life_balance, years_at_company, years_in_current_role]):
                return jsonify({
                    "error": True,
                    "message": "Mohon lengkapi semua field!"
                }), 400

            age = int(age)
            business_travel = int(business_travel)
            department = int(department)
            distance_from_home = int(distance_from_home)
            education = int(education)
            education_field = int(education_field)
            environment_satisfaction = int(environment_satisfaction)
            gender = int(gender)
            job_involvement = int(job_involvement)
            job_level = int(job_level)
            job_role = int(job_role)
            job_satisfaction = int(job_satisfaction)
            marital_status = int(marital_status)
            monthly_income = int(monthly_income)
            salary_slab = int(salary_slab)
            overtime = int(overtime)
            total_working_years = int(total_working_years)
            work_life_balance = int(work_life_balance)
            years_at_company = int(years_at_company)
            years_in_current_role = int(years_in_current_role)

            features = [age, business_travel, department, distance_from_home, education, education_field, environment_satisfaction, gender, job_involvement, job_level, job_role, job_satisfaction, marital_status, monthly_income, salary_slab, overtime, total_working_years, work_life_balance, years_at_company, years_in_current_role]
            prediction = model.predict([features])
            output = "LEAVES" if prediction[0] == 1 else "STAYED"

            new_data = JobData(
                age=age, 
                business_travel=business_travel, 
                department=department, 
                distance_from_home=distance_from_home, 
                education=education, 
                education_field=education_field, 
                environment_satisfaction=environment_satisfaction, 
                gender=gender, 
                job_involvement=job_involvement, 
                job_level=job_level, 
                job_role=job_role, 
                job_satisfaction=job_satisfaction, 
                marital_status=marital_status, 
                monthly_income=monthly_income,
                salary_slab=salary_slab, 
                overtime=overtime, 
                total_working_years=total_working_years, 
                work_life_balance=work_life_balance, 
                years_at_company=years_at_company, 
                years_in_current_role=years_in_current_role,
                prediction_result=output
            )
            db.session.add(new_data)
            db.session.commit()

            return jsonify({
                "error": False,
                "prediction_text": output,
                "input_data": {
                    "Age": age,
                    "Business Travel": business_travel,
                    "Department": department,
                    "Distance From Home": distance_from_home,
                    "Education": education,
                    "Education Field": education_field,
                    "Environment Satisfaction": environment_satisfaction,
                    "Gender": gender,
                    "Job Involvement": job_involvement,
                    "Job Level": job_level,
                    "Job Role": job_role,
                    "Job Satisfaction": job_satisfaction,
                    "Marital Status": marital_status,
                    "Monthly Income": monthly_income,
                    "Salary Slab": salary_slab,
                    "Overtime": overtime,
                    "Total Working Years": total_working_years,
                    "Work Life Balance": work_life_balance,
                    "Years At Company": years_at_company,
                    "Years In Current Role": years_in_current_role                    
                }
            })

        except Exception as e:
            print(f"Error occurred: {e}")
            return jsonify({
                "error": True,
                "message": "Harap masukkan data yang valid di setiap form.",
                "input_data": {}
            })

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
