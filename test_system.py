#!/usr/bin/env python3
"""
Test script to verify all modules work correctly
"""

print("="*80)
print("TESTING STUDENT PERFORMANCE ANALYSIS SYSTEM")
print("="*80)

# Test 1: Import all modules
print("\n1. Testing module imports...")
try:
    from data_generator import generate_student_data
    from statistical_analysis import StudentPerformanceAnalyzer
    from visualizations import PerformanceVisualizer
    from utils import ensure_directories
    from config import DEFAULT_SAMPLE_SIZE
    print("   ✓ All modules imported successfully")
except Exception as e:
    print(f"   ✗ Import error: {e}")
    exit(1)

# Test 2: Generate small dataset
print("\n2. Testing data generation...")
try:
    df = generate_student_data(100)
    print(f"   ✓ Generated {len(df)} records with {len(df.columns)} columns")
except Exception as e:
    print(f"   ✗ Data generation error: {e}")
    exit(1)

# Test 3: Run statistical analysis
print("\n3. Testing statistical analysis...")
try:
    analyzer = StudentPerformanceAnalyzer(df)
    pearson = analyzer.pearson_correlation_analysis()
    print(f"   ✓ Pearson correlation: {pearson['correlation_coefficient']}")
except Exception as e:
    print(f"   ✗ Statistical analysis error: {e}")
    exit(1)

# Test 4: Check visualization module
print("\n4. Testing visualization module...")
try:
    visualizer = PerformanceVisualizer(df)
    print("   ✓ Visualizer initialized successfully")
except Exception as e:
    print(f"   ✗ Visualization error: {e}")
    exit(1)

# Test 5: Directory structure
print("\n5. Testing directory structure...")
try:
    ensure_directories()
    print("   ✓ Directory structure verified")
except Exception as e:
    print(f"   ✗ Directory error: {e}")
    exit(1)

print("\n" + "="*80)
print("ALL TESTS PASSED ✓")
print("="*80)
print("\nYour system is ready!")
print("Run 'streamlit run app.py' to start the web application")
print("="*80 + "\n")
