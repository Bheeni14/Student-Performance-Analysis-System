"""
Utility functions for Student Performance Analysis System
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
import os

def ensure_directories():
    """Create necessary directories if they don't exist"""
    directories = ['data', 'visualizations', 'reports']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("✓ Directories checked/created")

def calculate_grade(score: float) -> str:
    """
    Calculate letter grade from numerical score
    
    Parameters:
    -----------
    score : float
        Numerical score (0-100)
    
    Returns:
    --------
    str : Letter grade
    """
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

def get_pass_fail(score: float, threshold: float = 50) -> str:
    """
    Determine pass/fail status
    
    Parameters:
    -----------
    score : float
        Numerical score
    threshold : float
        Passing threshold (default: 50)
    
    Returns:
    --------
    str : 'Pass' or 'Fail'
    """
    return 'Pass' if score >= threshold else 'Fail'

def calculate_summary_statistics(data: pd.Series) -> Dict:
    """
    Calculate comprehensive summary statistics
    
    Parameters:
    -----------
    data : pd.Series
        Data series
    
    Returns:
    --------
    dict : Summary statistics
    """
    return {
        'count': len(data),
        'mean': data.mean(),
        'median': data.median(),
        'std': data.std(),
        'min': data.min(),
        'max': data.max(),
        'q25': data.quantile(0.25),
        'q75': data.quantile(0.75),
        'iqr': data.quantile(0.75) - data.quantile(0.25)
    }

def validate_dataframe(df: pd.DataFrame, required_columns: List[str]) -> bool:
    """
    Validate that DataFrame has required columns
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to validate
    required_columns : list
        List of required column names
    
    Returns:
    --------
    bool : True if valid, raises ValueError otherwise
    """
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    return True

def format_pvalue(p_value: float) -> str:
    """
    Format p-value for display
    
    Parameters:
    -----------
    p_value : float
        P-value
    
    Returns:
    --------
    str : Formatted p-value string
    """
    if p_value < 0.001:
        return "< 0.001"
    elif p_value < 0.01:
        return f"{p_value:.3f}"
    else:
        return f"{p_value:.4f}"

def interpret_effect_size(effect_size: float, type: str = 'cohens_d') -> str:
    """
    Interpret effect size magnitude
    
    Parameters:
    -----------
    effect_size : float
        Effect size value
    type : str
        Type of effect size ('cohens_d', 'cramers_v', 'r')
    
    Returns:
    --------
    str : Interpretation
    """
    abs_effect = abs(effect_size)
    
    if type == 'cohens_d':
        if abs_effect < 0.2:
            return "negligible"
        elif abs_effect < 0.5:
            return "small"
        elif abs_effect < 0.8:
            return "medium"
        else:
            return "large"
    
    elif type == 'cramers_v':
        if abs_effect < 0.1:
            return "negligible"
        elif abs_effect < 0.3:
            return "small"
        elif abs_effect < 0.5:
            return "medium"
        else:
            return "large"
    
    elif type == 'r':
        if abs_effect < 0.1:
            return "negligible"
        elif abs_effect < 0.3:
            return "small"
        elif abs_effect < 0.5:
            return "medium"
        else:
            return "large"
    
    return "unknown"

def create_bins(data: pd.Series, n_bins: int = 5, labels: List[str] = None) -> pd.Series:
    """
    Create bins for continuous variable
    
    Parameters:
    -----------
    data : pd.Series
        Continuous data
    n_bins : int
        Number of bins
    labels : list
        Custom labels for bins
    
    Returns:
    --------
    pd.Series : Binned data
    """
    if labels is None:
        labels = [f"Bin {i+1}" for i in range(n_bins)]
    
    return pd.cut(data, bins=n_bins, labels=labels)

def export_to_excel(dataframes: Dict[str, pd.DataFrame], filename: str):
    """
    Export multiple DataFrames to Excel with separate sheets
    
    Parameters:
    -----------
    dataframes : dict
        Dictionary of sheet_name: DataFrame pairs
    filename : str
        Output filename
    """
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for sheet_name, df in dataframes.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"✓ Exported to {filename}")

def print_section_header(title: str, char: str = "=", width: int = 80):
    """
    Print formatted section header
    
    Parameters:
    -----------
    title : str
        Section title
    char : str
        Character for border
    width : int
        Total width
    """
    print("\n" + char * width)
    print(title.center(width))
    print(char * width)

if __name__ == "__main__":
    # Test utility functions
    ensure_directories()
    print("\n✓ All utility functions loaded successfully")
