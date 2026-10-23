# ⚡ Cloud Infrastructure Telemetry Dashboard (CloudWatch Simulator)

A single-file cloud infrastructure monitoring and telemetry dashboard built with Python, Streamlit, and Altair. This project simulates an observability control plane (such as **Amazon CloudWatch**, **Prometheus & Grafana**, or **Datadog**) tracking CPU, Memory, Disk, and Network performance across an enterprise virtual machine cluster.

Built for engineering portfolio showcases, academic project presentations, and cloud architecture viva examinations.

---

## 🌟 Key Features

- **Multi-Instance Fleet Monitoring**: Live health telemetry across web servers, AI GPU inference nodes, database replicas, and background workers.
- **Resource Utilization Meters**: Dynamic progress bars and percentage metrics for CPU, RAM memory (GB), Disk I/O, and Network throughput (MB/s).
- **Threshold-Driven Alarms**: Automated status badges (Healthy / Warning / Critical) triggered by configurable resource saturation points.
- **Interactive Incident Simulator**:
  - **Simulate Traffic Surge**: Spikes web cluster CPU load above 90% and fires a simulated CloudWatch alarm.
  - **Simulate Memory Leak**: Sinks database RAM availability below 10%.
  - **Trigger Cloud Auto-Scaler**: Simulates an Auto Scaling Group (ASG) provisioning extra replica instances to rebalance cluster load.
  - **Reset to Baseline**: Restores cluster telemetry to healthy steady-state.
- **Time-Series Utilization Graphs**: Interactive 24-hour visualization of compute load and bandwidth consumption.
- **Observability Event Stream**: Real-time event log capturing alarm notifications and auto-scaling events.
- **Clear Academic Disclaimer**: Clearly designates all metrics as simulated for portfolio demonstration.

---

## 📐 Cloud Computing Concepts Demonstrated

1. **Observability (Three Pillars)**: Metrics (numerical aggregates), Logs (event records), and Traces (request journeys).
2. **Horizontal vs Vertical Auto-Scaling**: Scaling out (adding VM instances to a fleet) vs scaling up (adding bigger CPU/RAM to a single VM).
3. **Cloud Alarms & Notification Pipelines**: How metrics exceed threshold conditions to trigger alerting systems (e.g. AWS CloudWatch Alarms + SNS).
4. **Capacity Planning & High Availability**: Maintaining redundant compute resources across Availability Zones to prevent service degradation under peak load.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip package manager

### 1. Installation
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/cloud-resource-dashboard.git
cd cloud-resource-dashboard
pip install -r requirements.txt
```

### 2. Run the Application
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

---

## 📁 Repository Structure

```text
cloud-resource-dashboard/
├── app.py                     # Single-file Streamlit application (UI + Telemetry simulator)
├── requirements.txt           # Minimal dependencies (streamlit, pandas, altair)
└── README.md                  # Comprehensive documentation & Viva guide
```

---

## 🎓 College Viva Preparation Guide

- **Q: What is the difference between AWS CloudWatch and AWS CloudTrail?**
  - **A:** CloudWatch monitors system performance, application metrics, alarms, and resource logs (observability). CloudTrail records user and API activity (who made what API call, from which IP, and when) for governance, security, and auditing.
- **Q: What is an Auto Scaling Group (ASG)?**
  - **A:** An ASG contains a collection of EC2 instances managed as a logical unit. It uses launch templates and scaling policies to automatically adjust the number of instances based on demand or scheduled events.
- **Q: Why is horizontal scaling preferred over vertical scaling in the cloud?**
  - **A:** Horizontal scaling (scale-out) offers near-infinite elastic scalability without downtime, eliminates single points of failure, and allows instances to be distributed across multiple availability zones.

---

## 🔮 Limitations & Future Improvements

- **Agent Integration**: In production, metrics are collected by daemons such as the AWS CloudWatch Agent or Prometheus node_exporter installed on VM hosts.
- **Distributed Tracing**: Future versions can demonstrate AWS X-Ray distributed trace visualizations.
- **Live AWS CloudWatch API**: Add Boto3 SDK support to pull real CloudWatch metrics when provided with AWS IAM credentials.

---

## 📄 License
MIT License. Created for AI & Data Science Engineering Portfolio.
