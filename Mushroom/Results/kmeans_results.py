from Classes.ResultUtils import ResultUtils
from Classes.KMeans import KMeansAlgorithm
import os
import pandas as pd

if __name__ == "__main__":
    dataset_path = '..'
else:
    dataset_path = 'Mushroom'

# Load dataset
data_path = os.path.join(dataset_path, "Preprocessing", "mushroom.csv")
data = pd.read_csv(data_path, index_col=0)
class_labels = data['Class']
X = data.drop(columns=['Class']).values

# Define configurations to test
max_k_value = 650
grid = {
    'k': [k for k in range(550, max_k_value+1)],
    'Distance_Metric': ['euclidean'],
    'Repetitions': 5  # Number of repetitions
}

# File paths for saving results
results_file = os.path.join(dataset_path, "Results", "CSVs", "kmeans_results.csv")
labels_file = os.path.join(dataset_path, "Results", "CSVs", "kmeans_cluster_labels.csv")

# Run grid search and save results
ResultUtils.runGrid(grid, KMeansAlgorithm, X, class_labels, results_file, labels_file)