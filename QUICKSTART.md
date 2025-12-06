# Quick Start Guide - Student Performance Analysis System

## 🚀 Getting Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
streamlit run app.py
```

### Step 3: Generate Data
1. Open the app in your browser (http://localhost:8501)
2. Click "🔄 Generate Data" in the sidebar
3. Choose sample size (default: 1000 students)

### Step 4: Explore Analysis
Navigate through the tabs:
- 📊 **Overview** - View your dataset
- 📈 **Statistical Analysis** - See correlation, chi-square, and regression results
- 🎨 **Visualizations** - Explore 15+ interactive charts
- 🔍 **Detailed Reports** - Generate comprehensive reports
- 📉 **Comparative Analysis** - Compare groups and factors
- 💾 **Export Results** - Download data and reports

---

## 🎯 Common Tasks

### Generate Custom Dataset
```python
from data_generator import generate_student_data

# Generate 500 students
df = generate_student_data(500)
df.to_csv('my_data.csv', index=False)
```

### Run Statistical Analysis
```python
from statistical_analysis import StudentPerformanceAnalyzer
import pandas as pd

df = pd.read_csv('student_performance_data.csv')
analyzer = StudentPerformanceAnalyzer(df)
results = analyzer.generate_full_report()
```

### Create Visualizations
```python
from visualizations import PerformanceVisualizer
import pandas as pd

df = pd.read_csv('student_performance_data.csv')
visualizer = PerformanceVisualizer(df)
visualizer.generate_all_visualizations('my_charts/')
```

---

## 🔧 Troubleshooting

**Problem**: Port 8501 already in use  
**Solution**: Run `streamlit run app.py --server.port 8502`

**Problem**: Module not found error  
**Solution**: Ensure you're in the project directory and dependencies are installed

**Problem**: Visualizations not displaying  
**Solution**: Clear cache with `streamlit cache clear`

---

## 📱 Contact & Support

For questions or issues, please open an issue on GitHub or contact the maintainer.

**Happy Analyzing! 📊**
