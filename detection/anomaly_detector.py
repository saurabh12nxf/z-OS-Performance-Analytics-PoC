import pandas as pd

df = pd.read_csv('../data/simulated_rmf.csv')
df['zscore'] = (df['CPU_Utilization'] - df['CPU_Utilization'].mean()) / df['CPU_Utilization'].std()
df['anomaly'] = df['zscore'].abs() > 2
anomalies = df[df['anomaly']]
print("Detected Anomalies:\n", anomalies)
