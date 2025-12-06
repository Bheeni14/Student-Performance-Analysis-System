"""
Main execution script for Student Performance Analysis System
Run complete analysis pipeline
"""

import pandas as pd
import numpy as np
from datetime import datetime
import sys
import os

# Import custom modules
from data_generator import generate_student_data
from statistical_analysis import StudentPerformanceAnalyzer
from visualizations import PerformanceVisualizer
from utils import ensure_directories, print_section_header

def main():
    """
    Execute complete analysis pipeline
    """
    print_section_header("STUDENT PERFORMANCE ANALYSIS SYSTEM", "=", 80)
    print(f"Execution started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Ensure directories exist
    ensure_directories()
    
    # Step 1: Generate or load data
    print("STEP 1: Data Generation")
    print("-" * 80)
    
    n_samples = 1000
    print(f"Generating {n_samples} student records...")
    df = generate_student_data(n_samples)
    
    # Save data
    df.to_csv('data/student_performance_data.csv', index=False)
    print(f"✓ Data saved to 'data/student_performance_data.csv'")
    print(f"✓ Generated {len(df)} records with {len(df.columns)} variables\n")
    
    # Step 2: Statistical Analysis
    print("STEP 2: Statistical Analysis")
    print("-" * 80)
    
    print("Performing comprehensive statistical analysis...")
    analyzer = StudentPerformanceAnalyzer(df)
    results = analyzer.generate_full_report()
    
    print("\n✓ Statistical analysis completed")
    print(f"  - Pearson correlation: {results['pearson_correlation']['correlation_coefficient']}")
    print(f"  - Key drivers identified: {len(results['key_drivers'])}")
    print(f"  - Chi-square statistic: {results['chi_square_test']['chi_square']:.3f}")
    print(f"  - Multiple regression R²: {results['multiple_regression']['r_squared']:.3f}\n")
    
    # Step 3: Generate Visualizations
    print("STEP 3: Visualization Generation")
    print("-" * 80)
    
    print("Generating 15+ comprehensive visualizations...")
    visualizer = PerformanceVisualizer(df)
    visualizer.generate_all_visualizations('visualizations/')
    print("✓ All visualizations saved to 'visualizations/' folder\n")
    
    # Step 4: Generate Reports
    print("STEP 4: Report Generation")
    print("-" * 80)
    
    # Summary statistics
    print("\nDataset Summary:")
    print(f"  Total Students: {len(df):,}")
    print(f"  Average Score: {df['Exam_Score'].mean():.2f}")
    print(f"  Pass Rate: {(df['Pass_Fail'] == 'Pass').sum() / len(df) * 100:.1f}%")
    print(f"  Grade A Percentage: {(df['Grade'] == 'A').sum() / len(df) * 100:.1f}%")
    
    # Key findings
    print("\nKey Findings:")
    print(f"  1. Study time correlation: {results['pearson_correlation']['correlation_coefficient']} (p < 0.001)")
    print(f"  2. Parental education effect: {max(results['chi_square_test']['pass_rates'].values()) - min(results['chi_square_test']['pass_rates'].values()):.1f}% pass rate increase")
    print(f"  3. Model explains {results['multiple_regression']['r_squared']*100:.1f}% of score variance")
    
    # Save text report
    report_filename = f"reports/analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_filename, 'w') as f:
        f.write("="*80 + "\n")
        f.write("STUDENT PERFORMANCE ANALYSIS - COMPREHENSIVE REPORT\n")
        f.write("="*80 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Dataset Size: {len(df):,} students\n")
        f.write(f"Variables: {len(df.columns)}\n\n")
        
        f.write("STATISTICAL RESULTS\n")
        f.write("-"*80 + "\n\n")
        
        f.write(f"1. Pearson Correlation (Study Time vs Score)\n")
        f.write(f"   Coefficient: {results['pearson_correlation']['correlation_coefficient']}\n")
        f.write(f"   P-value: {results['pearson_correlation']['p_value']:.6f}\n")
        f.write(f"   Interpretation: {results['pearson_correlation']['interpretation']}\n\n")
        
        f.write(f"2. Key Performance Drivers ({len(results['key_drivers'])} identified)\n")
        for driver, stats in results['key_drivers'].items():
            f.write(f"   - {driver}: {stats}\n")
        
        f.write(f"\n3. Chi-Square Test (Parental Education vs Pass/Fail)\n")
        f.write(f"   Chi-square: {results['chi_square_test']['chi_square']:.3f}\n")
        f.write(f"   P-value: {results['chi_square_test']['p_value']:.6f}\n")
        f.write(f"   Effect size (Cramér's V): {results['chi_square_test']['cramers_v']:.3f}\n\n")
        
        f.write(f"4. Multiple Regression Analysis\n")
        f.write(f"   R² Score: {results['multiple_regression']['r_squared']:.3f}\n")
        f.write(f"   Intercept: {results['multiple_regression']['intercept']:.3f}\n")
        f.write(f"   Coefficients:\n")
        for var, coef in results['multiple_regression']['coefficients'].items():
            f.write(f"     - {var}: {coef:.3f}\n")
    
    print(f"\n✓ Text report saved to '{report_filename}'")
    
    # Step 5: Summary
    print_section_header("ANALYSIS COMPLETE", "=", 80)
    print("\nOutput Files Generated:")
    print("  📊 data/student_performance_data.csv")
    print("  📈 visualizations/*.png (15+ charts)")
    print(f"  📄 {report_filename}")
    print("\nNext Steps:")
    print("  1. Review visualizations in 'visualizations/' folder")
    print("  2. Read comprehensive report in 'reports/' folder")
    print("  3. Run Streamlit app for interactive analysis: streamlit run app.py")
    print("\n" + "="*80)
    print(f"Execution completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
