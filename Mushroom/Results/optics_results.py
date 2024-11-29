# OPTICS results extraction
import os
import pandas as pd
import time
from Classes.EvaluationUtils import EvaluationUtils
from sklearn.cluster import OPTICS


if __name__ == "__main__" or "__mp_main__":
    dataset_path = '..'
else:
    dataset_path = 'Mushroom'

def clustering(X, metric, algorithm):
    """
    Perform OPTICS clustering with specified metric and algorithm
    """
    optics = OPTICS(
        metric=metric,
        algorithm=algorithm,
        min_samples=20,  # Allows reasonable density requirement for smaller clusters
        xi=0.02,  # Controls steepness for identifying clusters
        min_cluster_size=0.02  # Ensures clusters with a reasonable number of mushrooms
    )

    return optics.fit_predict(X)

# Load data
data_path = os.path.join(dataset_path, "Preprocessing", "mushroom.csv")
data = pd.read_csv(data_path)
class_labels = data['Class']
X = data.drop(columns=['Unnamed: 0', 'Class']).values

# Test configurations
distances = ['euclidean', 'manhattan', 'cosine']
algorithms = ['auto', 'brute', 'ball_tree', 'kd_tree',]

# Perform clustering
results = []
for dist in distances:
    if dist == 'cosine':
        algorithms = ['auto', 'brute']
    for algorithm in algorithms:
        start_time = time.time()
        cluster_pred = clustering(X, dist, algorithm)
        end_time = time.time()
        metrics = EvaluationUtils.evaluate(X, class_labels, cluster_pred)
        current_algorithm = f'Optics, {dist}, {algorithm})'
        execution_time = end_time - start_time
        results.append({
            'Algorithm': current_algorithm,
            **metrics,
            'Time': execution_time
        })

# Save results
results_df = pd.DataFrame(results)
csv_path = os.path.join(dataset_path, 'Results/CSVs/optics_results.csv')
results_df.to_csv(csv_path, index=False)

