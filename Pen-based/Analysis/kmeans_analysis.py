import pandas as pd
import os
from Classes.AnalysisUtils import AnalysisUtils

if __name__ == "__main__":
    dataset_path = '..'
else:
    dataset_path = 'Pen-based'

# Load the K-Means results
csv_path = os.path.join(dataset_path, "Results", "CSVs", "kmeans_results.csv")
results_df = pd.read_csv(csv_path)

# Create output directories
base_path = 'plots_and_tables'
plots_path = os.path.join(base_path, 'KMeansPlots')
reports_path = os.path.join(base_path, 'KMeansReports')

# Ensure output directories exist
os.makedirs(plots_path, exist_ok=True)
os.makedirs(reports_path, exist_ok=True)

# Metrics to analyze
metrics = ['E', 'ARI', 'F1 Score', 'DBI', 'silhouette_score', 'calinski_harabasz_score', 'Time']

# 1. Create Pairplot for Hyperparameter Analysis
AnalysisUtils.create_pairplot(
    data=results_df,
    params=['k', 'Distance_Metric'],
    metric='F1 Score',  # Using F1-Score as primary performance metric
    agg_func='max',
    plots_path=plots_path
)

# 2. Create Custom Heatmap for Metric Correlations
AnalysisUtils.plot_custom_heatmap(results_df[metrics], plots_path=plots_path)

print("K-Means clustering analysis completed successfully.")
print("Output files are available in:", base_path)