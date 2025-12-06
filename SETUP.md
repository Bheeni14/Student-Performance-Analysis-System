# 🚀 Setup Instructions - Student Performance Analysis System

## Prerequisites Check

Before starting, ensure you have:
- [ ] Python 3.8 or higher installed
- [ ] pip package manager available
- [ ] At least 4GB RAM
- [ ] 500MB free disk space
- [ ] Modern web browser

### Verify Python Installation

```batch
python --version
```

Should show: `Python 3.8.x` or higher

---

## Installation Steps

### Step 1: Navigate to Project Directory

```batch
cd d:\student
```

### Step 2: (Optional but Recommended) Create Virtual Environment

**Windows:**
```batch
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your command prompt.

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```batch
pip install -r requirements.txt
```

This will install:
- pandas (data analysis)
- numpy (numerical computing)
- seaborn (visualizations)
- matplotlib (plotting)
- scipy (statistics)
- streamlit (web app)
- plotly (interactive charts)
- scikit-learn (machine learning)
- openpyxl (Excel export)

**Installation should take 2-5 minutes.**

### Step 4: Verify Installation

```batch
python test_system.py
```

If successful, you'll see:
```
================================
ALL TESTS PASSED ✓
================================
```

---

## Usage Options

### Option 1: Launch Web Application (Recommended)

**Double-click:** `run_app.bat` (Windows)

**Or run manually:**
```batch
streamlit run app.py
```

The application will automatically open in your browser at:
```
http://localhost:8501
```

**What you'll see:**
- Beautiful modern interface
- Sidebar for data generation
- 6 main tabs for analysis
- Real-time visualizations

**First steps in the app:**
1. Click "🔄 Generate Data" in sidebar
2. Choose sample size (default: 1000)
3. Explore the tabs!

---

### Option 2: Run Complete Analysis

**Double-click:** `run_analysis.bat` (Windows)

**Or run manually:**
```batch
python main.py
```

**What it does:**
1. Generates 1,000 student records
2. Runs 7+ statistical tests
3. Creates 15+ visualizations
4. Generates comprehensive report

**Output files:**
- `data/student_performance_data.csv`
- `visualizations/*.png` (15 charts)
- `reports/analysis_report_[timestamp].txt`

**Time:** ~30-60 seconds

---

### Option 3: Python Script

Create your own analysis script:

```python
# my_analysis.py
from data_generator import generate_student_data
from statistical_analysis import StudentPerformanceAnalyzer
from visualizations import PerformanceVisualizer

# Generate data
print("Generating data...")
df = generate_student_data(1000)
df.to_csv('my_data.csv', index=False)

# Analyze
print("Analyzing data...")
analyzer = StudentPerformanceAnalyzer(df)
results = analyzer.generate_full_report()

# Print key findings
print(f"\nKey Findings:")
print(f"Correlation: {results['pearson_correlation']['correlation_coefficient']}")
print(f"Key Drivers: {len(results['key_drivers'])}")
print(f"R² Score: {results['multiple_regression']['r_squared']:.3f}")

# Visualize
print("\nGenerating visualizations...")
visualizer = PerformanceVisualizer(df)
visualizer.generate_all_visualizations('my_charts/')

print("\n✓ Complete!")
```

Run it:
```batch
python my_analysis.py
```

---

## Common Commands

### Start Web App
```batch
streamlit run app.py
```

### Run Full Analysis
```batch
python main.py
```

### Generate Data Only
```batch
python data_generator.py
```

### Test Installation
```batch
python test_system.py
```

### View Available Streamlit Ports
```batch
streamlit --help
```

### Run on Different Port
```batch
streamlit run app.py --server.port 8502
```

---

## Troubleshooting

### Problem: "Python is not recognized"
**Solution:** Add Python to your PATH environment variable

**Windows:**
1. Search "Environment Variables" in Start Menu
2. Edit "Path" under System Variables
3. Add Python installation directory
4. Restart command prompt

---

### Problem: "pip is not recognized"
**Solution:** Reinstall Python with "Add to PATH" checked

Or use:
```batch
python -m pip install -r requirements.txt
```

---

### Problem: "Module not found" after installation
**Solution:** 
```batch
# Upgrade pip first
python -m pip install --upgrade pip

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

---

### Problem: "Port 8501 already in use"
**Solution:**
```batch
# Use different port
streamlit run app.py --server.port 8502

# Or kill existing Streamlit processes (Windows)
taskkill /F /IM streamlit.exe
```

---

### Problem: "Permission denied" when creating files
**Solution:**
- Run Command Prompt as Administrator
- Or change to directory where you have write permissions

---

### Problem: Visualizations not displaying in Streamlit
**Solution:**
```batch
# Clear Streamlit cache
streamlit cache clear

# Restart app
streamlit run app.py
```

---

### Problem: "Memory Error" with large datasets
**Solution:**
- Reduce sample size to 500 or fewer
- Close other applications
- Use 64-bit Python

---

## Directory Structure After Setup

```
d:\student\
│
├── Core Files (You created these)
│   ├── app.py
│   ├── main.py
│   ├── data_generator.py
│   ├── statistical_analysis.py
│   ├── visualizations.py
│   ├── utils.py
│   ├── config.py
│   └── test_system.py
│
├── Documentation
│   ├── README.md
│   ├── DOCUMENTATION.md
│   ├── QUICKSTART.md
│   ├── PROJECT_SUMMARY.md
│   └── SETUP.md (this file)
│
├── Configuration
│   ├── requirements.txt
│   ├── .gitignore
│   ├── LICENSE
│   ├── run_app.bat
│   └── run_analysis.bat
│
├── Generated Directories (created automatically)
│   ├── data/
│   ├── visualizations/
│   └── reports/
│
└── Virtual Environment (if you created it)
    └── venv/
```

---

## What to Do Next

### For Portfolio/Resume
1. ✅ System is ready to showcase
2. ✅ Take screenshots of the web app
3. ✅ Include key metrics (1000 records, 15 visualizations, 0.68 correlation)
4. ✅ Highlight technologies (Python, Pandas, Streamlit, Statistical Modeling)

### For GitHub
1. Create new repository
2. Upload all files (except venv/ folder)
3. Add screenshots to README
4. Include PROJECT_SUMMARY.md as overview

### For Demonstration
1. Run `streamlit run app.py`
2. Generate 1,000 records
3. Walk through each tab
4. Show key findings
5. Export results

### For Further Development
1. Read DOCUMENTATION.md for API reference
2. Modify data_generator.py for custom variables
3. Add new statistical tests in statistical_analysis.py
4. Create custom visualizations in visualizations.py
5. Enhance UI in app.py

---

## Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Project downloaded to d:\student
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] System test passed (`python test_system.py`)
- [ ] Web app launched (`streamlit run app.py`)
- [ ] Data generated (clicked button in sidebar)
- [ ] Explored all 6 tabs
- [ ] Reviewed generated files in data/ and visualizations/

---

## Support Resources

### Included Documentation
1. **README.md** - Project overview
2. **QUICKSTART.md** - 5-minute guide
3. **DOCUMENTATION.md** - Complete technical reference
4. **PROJECT_SUMMARY.md** - Achievement summary
5. **SETUP.md** - This file

### External Resources
- Streamlit Docs: https://docs.streamlit.io/
- Pandas Docs: https://pandas.pydata.org/docs/
- Seaborn Gallery: https://seaborn.pydata.org/examples/
- SciPy Stats: https://docs.scipy.org/doc/scipy/reference/stats.html

---

## System Requirements

### Minimum
- Python 3.8
- 2GB RAM
- 250MB disk space
- Windows 10 / macOS 10.14 / Ubuntu 18.04

### Recommended
- Python 3.10+
- 4GB RAM
- 500MB disk space
- Windows 11 / macOS 12+ / Ubuntu 22.04
- Modern browser (Chrome, Firefox, Edge)

---

## Final Verification

Run this command to ensure everything is working:

```batch
python test_system.py && streamlit run app.py
```

If the test passes and the app opens, you're all set! 🎉

---

## Getting Help

If you encounter issues:

1. **Check this file** for troubleshooting section
2. **Review DOCUMENTATION.md** for detailed information
3. **Run test_system.py** to identify problems
4. **Check Python version** (`python --version`)
5. **Verify dependencies** (`pip list`)

---

**🎓 Student Performance Analysis System**

**Setup Status:** ✅ Ready to Use

**Next Step:** Double-click `run_app.bat` or run `streamlit run app.py`

---

*Last Updated: 2024-12-06*
