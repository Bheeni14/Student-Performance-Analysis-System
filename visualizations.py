"""
Comprehensive Visualization Module
Generates 15+ visualizations for student performance analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

class PerformanceVisualizer:
    """
    Comprehensive visualization suite for student performance data
    """
    
    def __init__(self, data):
        """
        Initialize visualizer with data
        
        Parameters:
        -----------
        data : pd.DataFrame
            Student performance dataset
        """
        self.data = data.copy()
        self.color_palette = sns.color_palette("husl", 10)
    
    def plot_correlation_heatmap(self, figsize=(12, 8)):
        """
        1. Correlation Heatmap - Shows relationships between numerical variables
        """
        numerical_cols = ['Study_Time_Hours', 'Attendance_Percentage', 
                         'Sleep_Hours', 'Exam_Score']
        
        corr_matrix = self.data[numerical_cols].corr()
        
        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='coolwarm', 
                   center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                   vmin=-1, vmax=1, ax=ax)
        plt.title('Correlation Heatmap - Student Performance Variables', 
                 fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        
        return fig
    
    def plot_exam_score_distribution(self, figsize=(12, 6)):
        """
        2. Exam Score Distribution - Histogram with KDE
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        sns.histplot(data=self.data, x='Exam_Score', bins=30, kde=True, 
                    color='#3498db', alpha=0.7, ax=ax)
        
        # Add mean and median lines
        mean_score = self.data['Exam_Score'].mean()
        median_score = self.data['Exam_Score'].median()
        
        ax.axvline(mean_score, color='red', linestyle='--', linewidth=2, 
                  label=f'Mean: {mean_score:.1f}')
        ax.axvline(median_score, color='green', linestyle='--', linewidth=2, 
                  label=f'Median: {median_score:.1f}')
        
        ax.set_title('Distribution of Exam Scores', fontsize=16, fontweight='bold')
        ax.set_xlabel('Exam Score', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.legend()
        plt.tight_layout()
        
        return fig
    
    def plot_study_time_vs_score_scatter(self, figsize=(12, 8)):
        """
        3. Scatter Plot - Study Time vs Exam Score with regression line
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        sns.regplot(data=self.data, x='Study_Time_Hours', y='Exam_Score', 
                   scatter_kws={'alpha':0.5, 's':50}, 
                   line_kws={'color':'red', 'linewidth':2}, ax=ax)
        
        # Calculate and display correlation
        from scipy.stats import pearsonr
        corr, p_value = pearsonr(self.data['Study_Time_Hours'], self.data['Exam_Score'])
        
        ax.text(0.05, 0.95, f'Correlation: {corr:.3f}\np-value: {p_value:.6f}', 
               transform=ax.transAxes, fontsize=12, verticalalignment='top',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        ax.set_title('Study Time vs Exam Score (Pearson Correlation)', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Study Time (Hours per Week)', fontsize=12)
        ax.set_ylabel('Exam Score', fontsize=12)
        plt.tight_layout()
        
        return fig
    
    def plot_parental_education_boxplot(self, figsize=(14, 8)):
        """
        4. Box Plot - Exam Scores by Parental Education
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        education_order = ['No Education', 'High School', 'Associate Degree', 
                          'Bachelor', 'Master', 'PhD']
        
        sns.boxplot(data=self.data, x='Parental_Education', y='Exam_Score', 
                   order=education_order, palette='Set2', ax=ax)
        
        ax.set_title('Exam Score Distribution by Parental Education Level', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Parental Education Level', fontsize=12)
        ax.set_ylabel('Exam Score', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        return fig
    
    def plot_attendance_impact(self, figsize=(12, 8)):
        """
        5. Scatter Plot - Attendance vs Exam Score
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        scatter = ax.scatter(self.data['Attendance_Percentage'], 
                           self.data['Exam_Score'],
                           c=self.data['Exam_Score'], cmap='RdYlGn', 
                           alpha=0.6, s=50)
        
        # Add regression line
        z = np.polyfit(self.data['Attendance_Percentage'], self.data['Exam_Score'], 1)
        p = np.poly1d(z)
        ax.plot(self.data['Attendance_Percentage'].sort_values(), 
               p(self.data['Attendance_Percentage'].sort_values()), 
               "r--", linewidth=2, label=f'y={z[0]:.2f}x+{z[1]:.2f}')
        
        plt.colorbar(scatter, label='Exam Score')
        ax.set_title('Attendance Impact on Exam Performance', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Attendance Percentage (%)', fontsize=12)
        ax.set_ylabel('Exam Score', fontsize=12)
        ax.legend()
        plt.tight_layout()
        
        return fig
    
    def plot_grade_distribution_pie(self, figsize=(10, 10)):
        """
        6. Pie Chart - Grade Distribution
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        grade_counts = self.data['Grade'].value_counts().sort_index()
        colors = ['#2ecc71', '#3498db', '#f39c12', '#e74c3c', '#95a5a6', '#34495e']
        
        wedges, texts, autotexts = ax.pie(grade_counts, labels=grade_counts.index, 
                                          autopct='%1.1f%%', colors=colors,
                                          startangle=90, textprops={'fontsize': 12})
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title('Grade Distribution Among Students', 
                    fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        
        return fig
    
    def plot_pass_fail_by_education(self, figsize=(12, 8)):
        """
        7. Stacked Bar Chart - Pass/Fail Rate by Parental Education
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        education_order = ['No Education', 'High School', 'Associate Degree', 
                          'Bachelor', 'Master', 'PhD']
        
        pass_fail_counts = pd.crosstab(self.data['Parental_Education'], 
                                       self.data['Pass_Fail'], normalize='index') * 100
        
        pass_fail_counts = pass_fail_counts.reindex(education_order)
        
        pass_fail_counts.plot(kind='bar', stacked=True, ax=ax, 
                             color=['#e74c3c', '#2ecc71'], width=0.7)
        
        ax.set_title('Pass/Fail Rate by Parental Education (Chi-Square Analysis)', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Parental Education Level', fontsize=12)
        ax.set_ylabel('Percentage (%)', fontsize=12)
        ax.legend(title='Status', loc='upper left')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        return fig
    
    def plot_sleep_hours_violin(self, figsize=(12, 8)):
        """
        8. Violin Plot - Sleep Hours by Pass/Fail
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        sns.violinplot(data=self.data, x='Pass_Fail', y='Sleep_Hours', 
                      palette={'Pass': '#2ecc71', 'Fail': '#e74c3c'}, ax=ax)
        
        ax.set_title('Sleep Hours Distribution: Pass vs Fail', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Status', fontsize=12)
        ax.set_ylabel('Sleep Hours per Night', fontsize=12)
        plt.tight_layout()
        
        return fig
    
    def plot_tutoring_impact(self, figsize=(12, 8)):
        """
        9. Bar Plot - Tutoring Impact on Scores
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        tutoring_stats = self.data.groupby('Tutoring')['Exam_Score'].agg(['mean', 'std'])
        
        bars = ax.bar(tutoring_stats.index, tutoring_stats['mean'], 
                     yerr=tutoring_stats['std'], capsize=10, 
                     color=['#e74c3c', '#2ecc71'], alpha=0.7, width=0.6)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}',
                   ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        ax.set_title('Impact of Tutoring on Exam Scores', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Tutoring', fontsize=12)
        ax.set_ylabel('Average Exam Score', fontsize=12)
        ax.set_ylim([0, 100])
        plt.tight_layout()
        
        return fig
    
    def plot_internet_access_comparison(self, figsize=(12, 8)):
        """
        10. Box Plot - Internet Access Impact
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        sns.boxplot(data=self.data, x='Internet_Access', y='Exam_Score', 
                   palette={'Yes': '#3498db', 'No': '#e74c3c'}, ax=ax)
        sns.swarmplot(data=self.data, x='Internet_Access', y='Exam_Score', 
                     color='black', alpha=0.3, size=3, ax=ax)
        
        ax.set_title('Exam Score Distribution by Internet Access', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Internet Access at Home', fontsize=12)
        ax.set_ylabel('Exam Score', fontsize=12)
        plt.tight_layout()
        
        return fig
    
    def plot_gender_comparison(self, figsize=(12, 8)):
        """
        11. Violin Plot - Gender Comparison
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        sns.violinplot(data=self.data, x='Gender', y='Exam_Score', 
                      palette={'Male': '#3498db', 'Female': '#e91e63'}, 
                      inner='box', ax=ax)
        
        ax.set_title('Exam Score Distribution by Gender', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Gender', fontsize=12)
        ax.set_ylabel('Exam Score', fontsize=12)
        plt.tight_layout()
        
        return fig
    
    def plot_multifactor_analysis(self, figsize=(14, 8)):
        """
        12. Facet Grid - Multi-factor Analysis
        """
        g = sns.FacetGrid(self.data, col='Tutoring', row='Internet_Access', 
                         height=4, aspect=1.5, margin_titles=True)
        g.map(sns.scatterplot, 'Study_Time_Hours', 'Exam_Score', alpha=0.6)
        g.add_legend()
        g.fig.suptitle('Multi-factor Analysis: Study Time vs Score', 
                      fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()
        
        return g.fig
    
    def plot_performance_trends_heatmap(self, figsize=(14, 10)):
        """
        13. Heatmap - Performance Trends Across Multiple Variables
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        # Create bins for continuous variables
        self.data['Study_Time_Bin'] = pd.cut(self.data['Study_Time_Hours'], 
                                             bins=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])
        self.data['Attendance_Bin'] = pd.cut(self.data['Attendance_Percentage'], 
                                            bins=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])
        
        # Create pivot table
        pivot_data = self.data.pivot_table(values='Exam_Score', 
                                          index='Study_Time_Bin', 
                                          columns='Attendance_Bin', 
                                          aggfunc='mean')
        
        sns.heatmap(pivot_data, annot=True, fmt='.1f', cmap='YlOrRd', 
                   linewidths=0.5, cbar_kws={'label': 'Average Exam Score'}, ax=ax)
        
        ax.set_title('Average Exam Score: Study Time vs Attendance Heatmap', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Attendance Level', fontsize=12)
        ax.set_ylabel('Study Time Level', fontsize=12)
        plt.tight_layout()
        
        return fig
    
    def plot_extracurricular_impact(self, figsize=(12, 8)):
        """
        14. Bar Plot - Extracurricular Activities Impact
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        extra_stats = self.data.groupby('Extracurricular_Activities')['Exam_Score'].agg(['mean', 'median', 'std'])
        
        x = np.arange(len(extra_stats.index))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, extra_stats['mean'], width, 
                      label='Mean', color='#3498db', alpha=0.8)
        bars2 = ax.bar(x + width/2, extra_stats['median'], width, 
                      label='Median', color='#2ecc71', alpha=0.8)
        
        ax.set_title('Impact of Extracurricular Activities on Exam Scores', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Extracurricular Activities', fontsize=12)
        ax.set_ylabel('Exam Score', fontsize=12)
        ax.set_xticks(x)
        ax.set_xticklabels(extra_stats.index)
        ax.legend()
        
        # Add value labels
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.1f}', ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()
        
        return fig
    
    def plot_comprehensive_summary(self, figsize=(20, 12)):
        """
        15. Comprehensive Dashboard - Multiple subplots
        """
        fig = plt.figure(figsize=figsize)
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
        
        # 1. Score Distribution
        ax1 = fig.add_subplot(gs[0, 0])
        self.data['Exam_Score'].hist(bins=30, color='skyblue', edgecolor='black', ax=ax1)
        ax1.set_title('Score Distribution', fontweight='bold')
        ax1.set_xlabel('Exam Score')
        ax1.set_ylabel('Frequency')
        
        # 2. Pass Rate
        ax2 = fig.add_subplot(gs[0, 1])
        pass_counts = self.data['Pass_Fail'].value_counts()
        ax2.pie(pass_counts, labels=pass_counts.index, autopct='%1.1f%%', 
               colors=['#2ecc71', '#e74c3c'], startangle=90)
        ax2.set_title('Pass/Fail Rate', fontweight='bold')
        
        # 3. Grade Distribution
        ax3 = fig.add_subplot(gs[0, 2])
        grade_counts = self.data['Grade'].value_counts().sort_index()
        ax3.bar(grade_counts.index, grade_counts.values, color='coral')
        ax3.set_title('Grade Distribution', fontweight='bold')
        ax3.set_xlabel('Grade')
        ax3.set_ylabel('Count')
        
        # 4. Study Time vs Score
        ax4 = fig.add_subplot(gs[1, 0])
        ax4.scatter(self.data['Study_Time_Hours'], self.data['Exam_Score'], 
                   alpha=0.5, c='purple')
        ax4.set_title('Study Time vs Score', fontweight='bold')
        ax4.set_xlabel('Study Time (hrs)')
        ax4.set_ylabel('Score')
        
        # 5. Attendance vs Score
        ax5 = fig.add_subplot(gs[1, 1])
        ax5.scatter(self.data['Attendance_Percentage'], self.data['Exam_Score'], 
                   alpha=0.5, c='green')
        ax5.set_title('Attendance vs Score', fontweight='bold')
        ax5.set_xlabel('Attendance %')
        ax5.set_ylabel('Score')
        
        # 6. Sleep Hours vs Score
        ax6 = fig.add_subplot(gs[1, 2])
        ax6.scatter(self.data['Sleep_Hours'], self.data['Exam_Score'], 
                   alpha=0.5, c='orange')
        ax6.set_title('Sleep vs Score', fontweight='bold')
        ax6.set_xlabel('Sleep (hrs)')
        ax6.set_ylabel('Score')
        
        # 7. Tutoring Impact
        ax7 = fig.add_subplot(gs[2, 0])
        tutoring_mean = self.data.groupby('Tutoring')['Exam_Score'].mean()
        ax7.bar(tutoring_mean.index, tutoring_mean.values, color=['#e74c3c', '#2ecc71'])
        ax7.set_title('Tutoring Impact', fontweight='bold')
        ax7.set_ylabel('Avg Score')
        
        # 8. Internet Access Impact
        ax8 = fig.add_subplot(gs[2, 1])
        internet_mean = self.data.groupby('Internet_Access')['Exam_Score'].mean()
        ax8.bar(internet_mean.index, internet_mean.values, color=['#e74c3c', '#3498db'])
        ax8.set_title('Internet Access Impact', fontweight='bold')
        ax8.set_ylabel('Avg Score')
        
        # 9. Gender Comparison
        ax9 = fig.add_subplot(gs[2, 2])
        gender_mean = self.data.groupby('Gender')['Exam_Score'].mean()
        ax9.bar(gender_mean.index, gender_mean.values, color=['#3498db', '#e91e63'])
        ax9.set_title('Gender Comparison', fontweight='bold')
        ax9.set_ylabel('Avg Score')
        
        fig.suptitle('Comprehensive Student Performance Dashboard', 
                    fontsize=20, fontweight='bold', y=0.995)
        
        return fig
    
    def generate_all_visualizations(self, save_path='visualizations/'):
        """
        Generate and save all 15 visualizations
        
        Parameters:
        -----------
        save_path : str
            Directory to save visualizations
        """
        import os
        os.makedirs(save_path, exist_ok=True)
        
        visualizations = [
            ('correlation_heatmap', self.plot_correlation_heatmap),
            ('exam_score_distribution', self.plot_exam_score_distribution),
            ('study_time_vs_score', self.plot_study_time_vs_score_scatter),
            ('parental_education_boxplot', self.plot_parental_education_boxplot),
            ('attendance_impact', self.plot_attendance_impact),
            ('grade_distribution_pie', self.plot_grade_distribution_pie),
            ('pass_fail_by_education', self.plot_pass_fail_by_education),
            ('sleep_hours_violin', self.plot_sleep_hours_violin),
            ('tutoring_impact', self.plot_tutoring_impact),
            ('internet_access_comparison', self.plot_internet_access_comparison),
            ('gender_comparison', self.plot_gender_comparison),
            ('multifactor_analysis', self.plot_multifactor_analysis),
            ('performance_trends_heatmap', self.plot_performance_trends_heatmap),
            ('extracurricular_impact', self.plot_extracurricular_impact),
            ('comprehensive_summary', self.plot_comprehensive_summary),
        ]
        
        print(f"Generating {len(visualizations)} visualizations...")
        for name, func in visualizations:
            try:
                fig = func()
                fig.savefig(f'{save_path}{name}.png', dpi=300, bbox_inches='tight')
                plt.close(fig)
                print(f"✓ Saved: {name}.png")
            except Exception as e:
                print(f"✗ Error generating {name}: {e}")
        
        print(f"\nAll visualizations saved to {save_path}")

if __name__ == "__main__":
    # Load data
    df = pd.read_csv('student_performance_data.csv')
    
    # Create visualizer
    visualizer = PerformanceVisualizer(df)
    
    # Generate all visualizations
    visualizer.generate_all_visualizations()
