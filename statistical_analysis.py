"""
Statistical Analysis Module
Performs comprehensive statistical tests and analyses on student performance data
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency, pearsonr, spearmanr, ttest_ind, f_oneway
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

class StudentPerformanceAnalyzer:
    """
    Comprehensive statistical analyzer for student performance data
    """
    
    def __init__(self, data):
        """
        Initialize analyzer with student data
        
        Parameters:
        -----------
        data : pd.DataFrame
            Student performance dataset
        """
        self.data = data.copy()
        self.results = {}
    
    def pearson_correlation_analysis(self):
        """
        Calculate Pearson correlation between study time and exam scores
        
        Returns:
        --------
        dict : Correlation results with coefficient and p-value
        """
        correlation, p_value = pearsonr(
            self.data['Study_Time_Hours'], 
            self.data['Exam_Score']
        )
        
        result = {
            'correlation_coefficient': round(correlation, 3),
            'p_value': p_value,
            'significant': p_value < 0.05,
            'interpretation': self._interpret_correlation(correlation)
        }
        
        self.results['pearson_correlation'] = result
        return result
    
    def _interpret_correlation(self, corr):
        """Interpret correlation strength"""
        abs_corr = abs(corr)
        if abs_corr >= 0.7:
            strength = "strong"
        elif abs_corr >= 0.4:
            strength = "moderate"
        elif abs_corr >= 0.2:
            strength = "weak"
        else:
            strength = "very weak"
        
        direction = "positive" if corr > 0 else "negative"
        return f"{strength} {direction} correlation"
    
    def correlation_matrix_analysis(self):
        """
        Calculate correlation matrix for all numerical variables
        
        Returns:
        --------
        pd.DataFrame : Correlation matrix
        """
        numerical_cols = ['Study_Time_Hours', 'Attendance_Percentage', 
                         'Sleep_Hours', 'Exam_Score']
        
        corr_matrix = self.data[numerical_cols].corr()
        self.results['correlation_matrix'] = corr_matrix
        return corr_matrix
    
    def chi_square_test(self, var1='Parental_Education', var2='Pass_Fail'):
        """
        Perform chi-square test for independence
        
        Parameters:
        -----------
        var1 : str
            First categorical variable
        var2 : str
            Second categorical variable
        
        Returns:
        --------
        dict : Chi-square test results
        """
        # Create contingency table
        contingency_table = pd.crosstab(self.data[var1], self.data[var2])
        
        # Perform chi-square test
        chi2, p_value, dof, expected = chi2_contingency(contingency_table)
        
        # Calculate effect size (Cramér's V)
        n = contingency_table.sum().sum()
        min_dim = min(contingency_table.shape) - 1
        cramers_v = np.sqrt(chi2 / (n * min_dim))
        
        # Calculate pass rates by parental education
        pass_rates = self.data.groupby(var1)[var2].apply(
            lambda x: (x == 'Pass').sum() / len(x) * 100
        ).round(2)
        
        result = {
            'chi_square': round(chi2, 3),
            'p_value': p_value,
            'degrees_of_freedom': dof,
            'significant': p_value < 0.05,
            'cramers_v': round(cramers_v, 3),
            'contingency_table': contingency_table,
            'pass_rates': pass_rates.to_dict()
        }
        
        self.results['chi_square_test'] = result
        return result
    
    def anova_test(self, categorical_var='Parental_Education', numerical_var='Exam_Score'):
        """
        Perform one-way ANOVA test
        
        Parameters:
        -----------
        categorical_var : str
            Categorical grouping variable
        numerical_var : str
            Numerical variable to compare
        
        Returns:
        --------
        dict : ANOVA test results
        """
        groups = [group[numerical_var].values for name, group in self.data.groupby(categorical_var)]
        
        f_stat, p_value = f_oneway(*groups)
        
        # Calculate group means
        group_means = self.data.groupby(categorical_var)[numerical_var].agg(['mean', 'std', 'count'])
        
        result = {
            'f_statistic': round(f_stat, 3),
            'p_value': p_value,
            'significant': p_value < 0.05,
            'group_statistics': group_means.to_dict()
        }
        
        self.results['anova_test'] = result
        return result
    
    def t_test_analysis(self, group_var='Gender', test_var='Exam_Score'):
        """
        Perform independent t-test
        
        Parameters:
        -----------
        group_var : str
            Binary grouping variable
        test_var : str
            Variable to test
        
        Returns:
        --------
        dict : T-test results
        """
        groups = self.data[group_var].unique()
        
        if len(groups) != 2:
            return {"error": "T-test requires exactly 2 groups"}
        
        group1_data = self.data[self.data[group_var] == groups[0]][test_var]
        group2_data = self.data[self.data[group_var] == groups[1]][test_var]
        
        t_stat, p_value = ttest_ind(group1_data, group2_data)
        
        # Calculate effect size (Cohen's d)
        mean_diff = group1_data.mean() - group2_data.mean()
        pooled_std = np.sqrt(((len(group1_data)-1)*group1_data.std()**2 + 
                              (len(group2_data)-1)*group2_data.std()**2) / 
                             (len(group1_data) + len(group2_data) - 2))
        cohens_d = mean_diff / pooled_std
        
        result = {
            'group_1': groups[0],
            'group_2': groups[1],
            't_statistic': round(t_stat, 3),
            'p_value': p_value,
            'significant': p_value < 0.05,
            'cohens_d': round(cohens_d, 3),
            'mean_difference': round(mean_diff, 2),
            f'{groups[0]}_mean': round(group1_data.mean(), 2),
            f'{groups[1]}_mean': round(group2_data.mean(), 2)
        }
        
        self.results['t_test'] = result
        return result
    
    def multiple_regression_analysis(self):
        """
        Perform multiple linear regression analysis
        
        Returns:
        --------
        dict : Regression results
        """
        # Prepare features
        X = self.data[['Study_Time_Hours', 'Attendance_Percentage', 'Sleep_Hours']].copy()
        y = self.data['Exam_Score'].copy()
        
        # Handle missing values
        X = X.fillna(X.mean())
        
        # Fit model
        model = LinearRegression()
        model.fit(X, y)
        
        # Calculate R-squared
        r_squared = model.score(X, y)
        
        # Get coefficients
        coefficients = dict(zip(X.columns, model.coef_))
        
        result = {
            'r_squared': round(r_squared, 3),
            'intercept': round(model.intercept_, 3),
            'coefficients': {k: round(v, 3) for k, v in coefficients.items()},
            'feature_importance': self._calculate_feature_importance(X, model.coef_)
        }
        
        self.results['multiple_regression'] = result
        return result
    
    def _calculate_feature_importance(self, X, coef):
        """Calculate normalized feature importance"""
        importance = np.abs(coef) * X.std().values
        importance = importance / importance.sum() * 100
        return dict(zip(X.columns, np.round(importance, 2)))
    
    def identify_key_performance_drivers(self, threshold_pvalue=0.05):
        """
        Identify key performance drivers with p-value < threshold
        
        Parameters:
        -----------
        threshold_pvalue : float
            P-value threshold for significance
        
        Returns:
        --------
        dict : Key drivers and their statistics
        """
        drivers = {}
        
        # Test correlation of each numerical variable with Exam_Score
        numerical_vars = ['Study_Time_Hours', 'Attendance_Percentage', 'Sleep_Hours']
        
        for var in numerical_vars:
            corr, p_val = pearsonr(self.data[var], self.data['Exam_Score'])
            if p_val < threshold_pvalue:
                drivers[var] = {
                    'correlation': round(corr, 3),
                    'p_value': p_val,
                    'effect': 'positive' if corr > 0 else 'negative'
                }
        
        # Test categorical variables
        categorical_vars = ['Parental_Education', 'Tutoring', 'Internet_Access']
        
        for var in categorical_vars:
            try:
                groups = [group['Exam_Score'].values for name, group in self.data.groupby(var)]
                f_stat, p_val = f_oneway(*groups)
                if p_val < threshold_pvalue:
                    drivers[var] = {
                        'f_statistic': round(f_stat, 3),
                        'p_value': p_val,
                        'effect': 'significant'
                    }
            except:
                pass
        
        self.results['key_drivers'] = drivers
        return drivers
    
    def calculate_confidence_intervals(self, variable='Exam_Score', confidence=0.95):
        """
        Calculate confidence intervals for a variable
        
        Parameters:
        -----------
        variable : str
            Variable name
        confidence : float
            Confidence level (default: 0.95)
        
        Returns:
        --------
        dict : Confidence interval results
        """
        data = self.data[variable].dropna()
        mean = data.mean()
        sem = stats.sem(data)
        ci = stats.t.interval(confidence, len(data)-1, loc=mean, scale=sem)
        
        result = {
            'mean': round(mean, 2),
            'confidence_level': confidence,
            'lower_bound': round(ci[0], 2),
            'upper_bound': round(ci[1], 2),
            'margin_of_error': round(ci[1] - mean, 2)
        }
        
        return result
    
    def generate_full_report(self):
        """
        Generate comprehensive statistical analysis report
        
        Returns:
        --------
        dict : Complete analysis results
        """
        print("Performing comprehensive statistical analysis...")
        
        # Perform all analyses
        self.pearson_correlation_analysis()
        self.correlation_matrix_analysis()
        self.chi_square_test()
        self.anova_test()
        self.t_test_analysis()
        self.multiple_regression_analysis()
        self.identify_key_performance_drivers()
        
        return self.results

if __name__ == "__main__":
    # Load data
    df = pd.read_csv('student_performance_data.csv')
    
    # Create analyzer
    analyzer = StudentPerformanceAnalyzer(df)
    
    # Generate full report
    results = analyzer.generate_full_report()
    
    print("\n" + "="*80)
    print("STATISTICAL ANALYSIS REPORT")
    print("="*80)
    
    print("\n1. Pearson Correlation (Study Time vs Exam Score):")
    print(f"   Correlation Coefficient: {results['pearson_correlation']['correlation_coefficient']}")
    print(f"   P-value: {results['pearson_correlation']['p_value']:.6f}")
    print(f"   Interpretation: {results['pearson_correlation']['interpretation']}")
    
    print("\n2. Key Performance Drivers (p < 0.05):")
    for driver, stats in results['key_drivers'].items():
        print(f"   - {driver}: {stats}")
    
    print("\n3. Chi-Square Test (Parental Education vs Pass/Fail):")
    print(f"   Chi-square: {results['chi_square_test']['chi_square']}")
    print(f"   P-value: {results['chi_square_test']['p_value']:.6f}")
    print(f"   Significant: {results['chi_square_test']['significant']}")
