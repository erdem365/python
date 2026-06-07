#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.units import cm, mm
import sys
import os
import tempfile
import warnings
warnings.filterwarnings('ignore')

# Optional: set matplotlib font for better compatibility
plt.rcParams['font.family'] = 'DejaVu Sans'

class DataAnalysisTool:
    def __init__(self, csv_file):
        """
        Loads the CSV file and performs basic checks.
        """
        self.file_name = csv_file
        try:
            self.df = pd.read_csv(csv_file, encoding='utf-8')
        except UnicodeDecodeError:
            self.df = pd.read_csv(csv_file, encoding='latin1')
        except Exception as e:
            raise Exception(f"Unable to read file: {e}")
        
        self.numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        print(f"Dataset: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        print(f"Numeric columns: {len(self.numeric_cols)}")
        
    def missing_data_report(self):
        """Creates a missing data table."""
        missing_counts = self.df.isnull().sum()
        missing_percent = (missing_counts / len(self.df)) * 100
        missing_df = pd.DataFrame({
            'Missing Count': missing_counts,
            'Missing Percent (%)': missing_percent
        })
        missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Percent (%)', ascending=False)
        return missing_df
    
    def outlier_report(self):
        """
        Detects outliers using the IQR method.
        For each numeric column: outlier count, lower/upper bounds.
        """
        outlier_info = []
        for col in self.numeric_cols:
            data = self.df[col].dropna()
            if len(data) == 0:
                continue
            Q1 = data.quantile(0.25)
            Q3 = data.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = data[(data < lower_bound) | (data > upper_bound)]
            outlier_info.append({
                'Column': col,
                'Outlier Count': len(outliers),
                'Outlier Ratio (%)': round(100 * len(outliers) / len(data), 2),
                'Lower Bound': round(lower_bound, 3),
                'Upper Bound': round(upper_bound, 3)
            })
        return pd.DataFrame(outlier_info)
    
    def correlation_matrix(self):
        """Correlation matrix between numeric columns."""
        if len(self.numeric_cols) < 2:
            return None
        return self.df[self.numeric_cols].corr()
    
    def histogram_figure(self, output_path):
        """Plots histograms for all numeric columns and saves the figure."""
        if not self.numeric_cols:
            return None
        n_cols = min(3, len(self.numeric_cols))
        n_rows = (len(self.numeric_cols) + n_cols - 1) // n_cols
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows))
        axes = axes.flatten() if n_rows * n_cols > 1 else [axes]
        
        for i, col in enumerate(self.numeric_cols):
            self.df[col].dropna().hist(ax=axes[i], bins=20, edgecolor='black', alpha=0.7)
            axes[i].set_title(col)
            axes[i].set_xlabel('Value')
            axes[i].set_ylabel('Frequency')
        # Hide any empty subplots
        for j in range(i+1, len(axes)):
            axes[j].set_visible(False)
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        return output_path
    
    def boxplot_figure(self, output_path):
        """Plots boxplots for all numeric columns and saves the figure."""
        if not self.numeric_cols:
            return None
        fig, ax = plt.subplots(figsize=(max(6, len(self.numeric_cols)*0.8), 6))
        # Prepare data (drop missing)
        data_to_plot = [self.df[col].dropna().values for col in self.numeric_cols]
        bp = ax.boxplot(data_to_plot, labels=self.numeric_cols, vert=True, patch_artist=True)
        ax.set_title('Boxplot for Numeric Variables (Outliers shown as •)')
        ax.set_ylabel('Values')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        return output_path
    
    def generate_pdf_report(self, output_pdf="data_analysis_report.pdf"):
        """Generates a PDF report with all analysis results using ReportLab."""
        doc = SimpleDocTemplate(output_pdf, pagesize=A4,
                                rightMargin=2*cm, leftMargin=2*cm,
                                topMargin=2*cm, bottomMargin=2*cm)
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        subtitle_style = styles['Heading2']
        normal_style = styles['Normal']
        
        # Custom table style
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ])
        
        story = []
        
        # Title
        story.append(Paragraph(f"Data Analysis Report: {os.path.basename(self.file_name)}", title_style))
        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph(f"Generated on: {pd.Timestamp.now().strftime('%d.%m.%Y %H:%M')}", normal_style))
        story.append(Spacer(1, 0.5*cm))
        
        # 1. Dataset Overview
        story.append(Paragraph("1. Dataset Overview", subtitle_style))
        overview_data = [
            ["Property", "Value"],
            ["Number of Rows", str(self.df.shape[0])],
            ["Number of Columns", str(self.df.shape[1])],
            ["Numeric Columns", str(len(self.numeric_cols))],
            ["Categorical Columns", str(len(self.categorical_cols))],
        ]
        overview_table = Table(overview_data, colWidths=[5*cm, 8*cm])
        overview_table.setStyle(table_style)
        story.append(overview_table)
        story.append(Spacer(1, 0.5*cm))
        
        # 2. Missing Data
        story.append(Paragraph("2. Missing Data Analysis", subtitle_style))
        missing_df = self.missing_data_report()
        if missing_df.empty:
            story.append(Paragraph("No missing data found.", normal_style))
        else:
            # Convert DataFrame to list of lists
            data_missing = [missing_df.columns.tolist()] + missing_df.reset_index().values.tolist()
            # Fix column names
            data_missing[0] = ['Column Name', 'Missing Count', 'Missing Percent (%)']
            missing_table = Table(data_missing, colWidths=[5*cm, 3*cm, 3*cm])
            missing_table.setStyle(table_style)
            story.append(missing_table)
        story.append(Spacer(1, 0.5*cm))
        
        # 3. Outlier Detection
        story.append(Paragraph("3. Outlier Analysis (IQR Method)", subtitle_style))
        outlier_df = self.outlier_report()
        if outlier_df.empty:
            story.append(Paragraph("No numeric columns or no outliers found.", normal_style))
        else:
            data_outlier = [outlier_df.columns.tolist()] + outlier_df.values.tolist()
            outlier_table = Table(data_outlier, colWidths=[3*cm, 2.5*cm, 2.5*cm, 2.5*cm, 2.5*cm])
            outlier_table.setStyle(table_style)
            story.append(outlier_table)
        story.append(Spacer(1, 0.5*cm))
        
        # 4. Correlation Matrix
        story.append(Paragraph("4. Correlation Matrix (Numeric Variables)", subtitle_style))
        corr_matrix = self.correlation_matrix()
        if corr_matrix is None or corr_matrix.empty:
            story.append(Paragraph("At least two numeric columns are required for correlation matrix.", normal_style))
        else:
            # Show as table
            corr_rounded = corr_matrix.round(2).fillna('')
            corr_list = [corr_rounded.columns.tolist()] + corr_rounded.values.tolist()
            # Add row headers (column names)
            for i, col_name in enumerate(corr_rounded.columns):
                corr_list[i+1].insert(0, col_name)
            corr_list[0].insert(0, ' ')
            corr_table = Table(corr_list, colWidths=[1.8*cm] * (len(corr_rounded.columns)+1))
            corr_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
            ]))
            story.append(corr_table)
            story.append(Paragraph("Note: Values are Pearson correlation coefficients. 1 = perfect positive, -1 = perfect negative.", normal_style))
            
            # Add heatmap image
            fig, ax = plt.subplots(figsize=(8, 6))
            im = ax.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1, aspect='auto')
            ax.set_xticks(np.arange(len(corr_matrix.columns)))
            ax.set_yticks(np.arange(len(corr_matrix.columns)))
            ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
            ax.set_yticklabels(corr_matrix.columns)
            for i in range(len(corr_matrix.columns)):
                for j in range(len(corr_matrix.columns)):
                    ax.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}", ha='center', va='center', color='black', fontsize=8)
            plt.colorbar(im, ax=ax, label='Correlation')
            plt.title('Correlation Heatmap')
            plt.tight_layout()
            heatmap_path = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
            plt.savefig(heatmap_path, dpi=120, bbox_inches='tight')
            plt.close()
            story.append(Spacer(1, 0.5*cm))
            story.append(Image(heatmap_path, width=16*cm, height=12*cm))
            os.unlink(heatmap_path)
        story.append(PageBreak())
        
        # 5. Histograms
        story.append(Paragraph("5. Histograms (Distribution of Numeric Variables)", subtitle_style))
        hist_path = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
        if self.histogram_figure(hist_path):
            story.append(Image(hist_path, width=17*cm, height=12*cm))
            os.unlink(hist_path)
        else:
            story.append(Paragraph("No numeric columns available to plot histograms.", normal_style))
        story.append(Spacer(1, 0.5*cm))
        
        # 6. Boxplots
        story.append(Paragraph("6. Boxplots (Outlier and Quartile View)", subtitle_style))
        box_path = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
        if self.boxplot_figure(box_path):
            story.append(Image(box_path, width=17*cm, height=10*cm))
            os.unlink(box_path)
        else:
            story.append(Paragraph("No numeric columns available to plot boxplots.", normal_style))
        
        # Build the PDF
        doc.build(story)
        print(f"\n PDF report created: {output_pdf}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python data_analysis_tool.py <csv_file_path> [output_pdf_name]")
        print("Example: python data_analysis_tool.py data.csv report.pdf")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    output_pdf = sys.argv[2] if len(sys.argv) > 2 else "data_analysis_report.pdf"
    
    try:
        analyzer = DataAnalysisTool(csv_file)
        analyzer.generate_pdf_report(output_pdf)
        print("\nAnalysis completed.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
