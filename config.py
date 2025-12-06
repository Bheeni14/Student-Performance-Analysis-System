# Configuration file for Student Performance Analysis System

# Data Generation Settings
DEFAULT_SAMPLE_SIZE = 1000
MIN_SAMPLE_SIZE = 100
MAX_SAMPLE_SIZE = 10000

# Statistical Thresholds
SIGNIFICANCE_LEVEL = 0.05
CONFIDENCE_INTERVAL = 0.95
PASSING_GRADE = 50

# Visualization Settings
FIGURE_DPI = 300
DEFAULT_FIGSIZE = (12, 8)
COLOR_PALETTE = "husl"

# Grade Boundaries
GRADE_BOUNDARIES = {
    'A': 90,
    'B': 80,
    'C': 70,
    'D': 60,
    'E': 50,
    'F': 0
}

# Correlation Strength Thresholds
CORRELATION_STRONG = 0.7
CORRELATION_MODERATE = 0.4
CORRELATION_WEAK = 0.2

# File Paths
DATA_DIR = "data"
VISUALIZATION_DIR = "visualizations"
REPORTS_DIR = "reports"
