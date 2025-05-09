# z/OS Performance Analytics PoC

This proof-of-concept simulates RMF MON III performance metrics, exports them to Prometheus, visualizes them in Grafana, and uses a simple anomaly detection model.

## Features
- Simulated z/OS metrics: CPU, Disk I/O, Paging
- Live metrics exported using Prometheus
- Real-time Grafana dashboards
- Anomaly detection using Z-score

## Folder Structure
See detailed breakdown in the repo.

## Getting Started
1. Install Prometheus, Grafana, and Python dependencies.
2. Start Prometheus and Grafana.
3. Run the Python Prometheus exporter.
4. Build dashboards in Grafana.
5. Run anomaly detector for performance insight.

