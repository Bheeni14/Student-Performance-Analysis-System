"""
Student Performance Data Generator
Generates realistic student performance data for analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

def generate_student_data(n_samples=1000):
    """
    Generate realistic student performance data with correlations
    
    Parameters:
    -----------
    n_samples : int
        Number of student records to generate (default: 1000)
    
    Returns:
    --------
    pd.DataFrame
        DataFrame containing student performance data
    """
    
    # Generate base variables
    student_ids = [f"STU{str(i).zfill(4)}" for i in range(1, n_samples + 1)]
    
    # Gender distribution
    gender = np.random.choice(['Male', 'Female'], size=n_samples, p=[0.48, 0.52])
    
    # Parental education levels
    parental_education = np.random.choice(
        ['No Education', 'High School', 'Associate Degree', 'Bachelor', 'Master', 'PhD'],
        size=n_samples,
        p=[0.10, 0.30, 0.20, 0.25, 0.12, 0.03]
    )
    
    # Study time (hours per week) - influenced by parental education
    base_study_time = np.random.normal(15, 5, n_samples)
    education_boost = np.where(
        np.isin(parental_education, ['Bachelor', 'Master', 'PhD']), 
        np.random.normal(5, 2, n_samples), 
        0
    )
    study_time = np.clip(base_study_time + education_boost, 0, 40)
    
    # Attendance percentage
    attendance = np.random.beta(8, 2, n_samples) * 100
    
    # Sleep hours (per night)
    sleep_hours = np.random.normal(7, 1.5, n_samples)
    sleep_hours = np.clip(sleep_hours, 4, 10)
    
    # Internet access at home
    internet_access = np.random.choice(['Yes', 'No'], size=n_samples, p=[0.85, 0.15])
    
    # Tutoring
    tutoring = np.random.choice(['Yes', 'No'], size=n_samples, p=[0.35, 0.65])
    
    # Extracurricular activities
    extracurricular = np.random.choice(['Yes', 'No'], size=n_samples, p=[0.45, 0.55])
    
    # Calculate exam scores based on multiple factors
    # Base score
    exam_scores = np.random.normal(60, 15, n_samples)
    
    # Study time correlation (0.68 correlation coefficient)
    exam_scores += (study_time - study_time.mean()) * 0.68 * (15 / study_time.std())
    
    # Attendance effect
    exam_scores += (attendance - attendance.mean()) * 0.3
    
    # Parental education effect
    education_mapping = {
        'No Education': -8,
        'High School': -2,
        'Associate Degree': 3,
        'Bachelor': 8,
        'Master': 12,
        'PhD': 15
    }
    exam_scores += [education_mapping[edu] for edu in parental_education]
    
    # Tutoring effect
    exam_scores += np.where(tutoring == 'Yes', np.random.normal(5, 2, n_samples), 0)
    
    # Sleep effect (optimal around 7-8 hours)
    sleep_effect = -np.abs(sleep_hours - 7.5) * 2
    exam_scores += sleep_effect
    
    # Internet access effect
    exam_scores += np.where(internet_access == 'Yes', np.random.normal(4, 1, n_samples), 0)
    
    # Add some random noise
    exam_scores += np.random.normal(0, 5, n_samples)
    
    # Clip scores to realistic range
    exam_scores = np.clip(exam_scores, 0, 100)
    
    # Pass/Fail (passing grade = 50)
    pass_fail = np.where(exam_scores >= 50, 'Pass', 'Fail')
    
    # Grade categories
    def assign_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        elif score >= 50:
            return 'E'
        else:
            return 'F'
    
    grades = [assign_grade(score) for score in exam_scores]
    
    # Create DataFrame
    df = pd.DataFrame({
        'Student_ID': student_ids,
        'Gender': gender,
        'Parental_Education': parental_education,
        'Study_Time_Hours': np.round(study_time, 1),
        'Attendance_Percentage': np.round(attendance, 1),
        'Sleep_Hours': np.round(sleep_hours, 1),
        'Internet_Access': internet_access,
        'Tutoring': tutoring,
        'Extracurricular_Activities': extracurricular,
        'Exam_Score': np.round(exam_scores, 1),
        'Grade': grades,
        'Pass_Fail': pass_fail
    })
    
    return df

if __name__ == "__main__":
    # Generate data
    df = generate_student_data(1000)
    
    # Save to CSV
    df.to_csv('student_performance_data.csv', index=False)
    print(f"Generated {len(df)} student records")
    print("\nDataset Preview:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nBasic Statistics:")
    print(df.describe())
