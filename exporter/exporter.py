from prometheus_client import Gauge, start_http_server
import time, csv

cpu = Gauge('zos_cpu_utilization', 'CPU Utilization %')
disk_io = Gauge('zos_disk_io', 'Disk IO per second')
paging = Gauge('zos_paging_rate', 'Paging rate')

def run_exporter():
    with open('../data/simulated_rmf.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cpu.set(float(row['CPU_Utilization']))
            disk_io.set(float(row['Disk_IO_per_sec']))
            paging.set(float(row['Paging_Rate']))
            time.sleep(5)

if __name__ == "__main__":
    start_http_server(8000)
    run_exporter()
