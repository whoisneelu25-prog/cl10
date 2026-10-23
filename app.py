import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
import altair as alt

# -------------------------------------------------------------
# Page Configuration & UI Theme
# -------------------------------------------------------------
st.set_page_config(
    page_title="CloudWatch | Cloud Infrastructure Telemetry Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for modern cloud monitoring console
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        padding: 24px;
        border-radius: 14px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.2);
        border: 1px solid #334155;
    }
    .main-header h1 {
        margin: 0;
        font-size: 26px;
        font-weight: 700;
        color: white !important;
    }
    .main-header p {
        margin-top: 6px;
        margin-bottom: 0;
        font-size: 14px;
        opacity: 0.9;
        color: #94a3b8;
    }
    
    .disclaimer-banner {
        background-color: #f8fafc;
        border-left: 4px solid #0284c7;
        color: #334155;
        padding: 10px 16px;
        border-radius: 6px;
        font-size: 13px;
        margin-bottom: 20px;
    }
    
    .badge-healthy {
        background-color: #dcfce7;
        color: #15803d;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 12px;
        display: inline-block;
    }
    .badge-warn {
        background-color: #fef9c3;
        color: #a16207;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 12px;
        display: inline-block;
    }
    .badge-critical {
        background-color: #fee2e2;
        color: #b91c1c;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 12px;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Simulated Infrastructure Fleet State
# -------------------------------------------------------------
if "fleet" not in st.session_state:
    st.session_state.fleet = {
        "web-prod-node-01": {"type": "t3.large", "cpu": 42.0, "ram_gb": 5.4, "ram_max": 8.0, "disk_pct": 52.0, "net_mb_s": 14.2, "status": "Healthy"},
        "ai-inference-worker-gpu": {"type": "g4dn.xlarge", "cpu": 68.5, "ram_gb": 11.2, "ram_max": 16.0, "disk_pct": 64.0, "net_mb_s": 28.5, "status": "Healthy"},
        "db-primary-replica": {"type": "r6g.xlarge", "cpu": 54.0, "ram_gb": 24.8, "ram_max": 32.0, "disk_pct": 78.0, "net_mb_s": 8.1, "status": "Healthy"},
        "event-stream-consumer": {"type": "t3.medium", "cpu": 22.0, "ram_gb": 2.1, "ram_max": 4.0, "disk_pct": 34.0, "net_mb_s": 4.5, "status": "Healthy"}
    }

if "alarm_logs" not in st.session_state:
    st.session_state.alarm_logs = [
        {"timestamp": "2026-10-23 09:30:00", "instance": "Fleet-Wide", "severity": "INFO", "message": "Telemetry streaming established with 10-second sampling resolution."},
        {"timestamp": "2026-10-23 09:45:12", "instance": "db-primary-replica", "severity": "OK", "message": "Automated snapshot backup completed successfully."}
    ]

# -------------------------------------------------------------
# Header
# -------------------------------------------------------------
st.markdown("""
<div class="main-header">
    <h1>⚡ CloudWatch — Infrastructure Telemetry Dashboard</h1>
    <p>Real-time simulated observability console for cloud instances, cluster metrics, alarms, and auto-scaling events.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="disclaimer-banner">
    ℹ️ <strong>Simulated Metrics Notice:</strong> All metrics, utilization percentages, and server topologies displayed are synthesized for academic demonstration and cloud observability architecture presentation.
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Sidebar: Cloud Concepts & Viva Guide
# -------------------------------------------------------------
with st.sidebar:
    st.subheader("🌐 Cloud Monitoring Controls")
    selected_region = st.selectbox("Cloud Region:", ["ap-south-1 (Mumbai)", "us-east-1 (N. Virginia)", "eu-central-1 (Frankfurt)"])
    sampling_rate = st.selectbox("Metrics Metric Resolution:", ["10 Seconds (High-Res)", "1 Minute", "5 Minutes"])
    
    st.markdown("---")
    st.subheader("🚨 Incident Injection Controls")
    st.caption("Trigger realistic cloud workload scenarios during your presentation:")
    
    if st.button("🔥 Simulate Traffic Surge", use_container_width=True):
        st.session_state.fleet["web-prod-node-01"]["cpu"] = 94.2
        st.session_state.fleet["web-prod-node-01"]["net_mb_s"] = 112.5
        st.session_state.fleet["web-prod-node-01"]["status"] = "Critical"
        st.session_state.alarm_logs.insert(0, {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "instance": "web-prod-node-01",
            "severity": "ALARM",
            "message": "CPUUtilization > 85.0% threshold breached for 1 consecutive period."
        })
        st.toast("Simulated traffic surge triggered! web-prod-node-01 CPU spiked.", icon="🔥")
        st.rerun()

    if st.button("🧠 Simulate Memory Leak", use_container_width=True):
        st.session_state.fleet["db-primary-replica"]["ram_gb"] = 30.5
        st.session_state.fleet["db-primary-replica"]["status"] = "Warning"
        st.session_state.alarm_logs.insert(0, {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "instance": "db-primary-replica",
            "severity": "WARNING",
            "message": "MemoryUtilization > 90% threshold breached (30.5 GB / 32 GB consumed)."
        })
        st.toast("Simulated memory leak triggered on database node.", icon="⚠️")
        st.rerun()

    if st.button("⚖️ Trigger Cloud Auto-Scaler", use_container_width=True):
        # Auto-scale reduces load by distributing
        st.session_state.fleet["web-prod-node-01"]["cpu"] = 45.0
        st.session_state.fleet["web-prod-node-01"]["net_mb_s"] = 25.0
        st.session_state.fleet["web-prod-node-01"]["status"] = "Healthy"
        st.session_state.alarm_logs.insert(0, {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "instance": "AutoScalingGroup",
            "severity": "RECOVERY",
            "message": "ASG scaled out 1 instance: launched 'web-prod-node-02'. Load normalized."
        })
        st.toast("Auto-scaler launched new instance! Cluster healthy.", icon="✅")
        st.rerun()

    if st.button("🔄 Reset to Baseline Metrics", use_container_width=True):
        st.session_state.fleet = {
            "web-prod-node-01": {"type": "t3.large", "cpu": 42.0, "ram_gb": 5.4, "ram_max": 8.0, "disk_pct": 52.0, "net_mb_s": 14.2, "status": "Healthy"},
            "ai-inference-worker-gpu": {"type": "g4dn.xlarge", "cpu": 68.5, "ram_gb": 11.2, "ram_max": 16.0, "disk_pct": 64.0, "net_mb_s": 28.5, "status": "Healthy"},
            "db-primary-replica": {"type": "r6g.xlarge", "cpu": 54.0, "ram_gb": 24.8, "ram_max": 32.0, "disk_pct": 78.0, "net_mb_s": 8.1, "status": "Healthy"},
            "event-stream-consumer": {"type": "t3.medium", "cpu": 22.0, "ram_gb": 2.1, "ram_max": 4.0, "disk_pct": 34.0, "net_mb_s": 4.5, "status": "Healthy"}
        }
        st.toast("Fleet metrics restored to baseline normal.", icon="🔄")
        st.rerun()

    st.markdown("---")
    with st.expander("🎓 College Viva Q&A Guide", expanded=False):
        st.markdown("""
**Q1: What are the Three Pillars of Observability?**
- **Metrics:** Numeric aggregated telemetry over intervals (e.g. CPU %, Network bytes).
- **Logs:** Immutable timestamped textual records of specific discrete application events.
- **Traces:** End-to-end request lifecycle paths across microservices.

**Q2: How does Cloud Auto-Scaling work?**
- Metric alarms (like CPU > 80% for 3 minutes) trigger an Auto Scaling Group (ASG) policy. The ASG launches additional VM instances behind a load balancer to distribute the load (Horizontal Scaling).

**Q3: What is Horizontal vs Vertical Scaling?**
- **Horizontal Scaling (Scale Out):** Adding more machine instances to the pool.
- **Vertical Scaling (Scale Up):** Adding more CPU/RAM to a single existing virtual machine (often requires downtime).
        """)

# -------------------------------------------------------------
# Top Fleet Aggregates
# -------------------------------------------------------------
instances = list(st.session_state.fleet.values())
avg_cpu = np.mean([inst["cpu"] for inst in instances])
total_ram_used = sum([inst["ram_gb"] for inst in instances])
total_ram_cap = sum([inst["ram_max"] for inst in instances])
ram_pct = (total_ram_used / total_ram_cap) * 100
total_net_bw = sum([inst["net_mb_s"] for inst in instances])
critical_count = sum(1 for inst in instances if inst["status"] != "Healthy")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Fleet Average CPU", f"{avg_cpu:.1f}%", delta="Normal" if avg_cpu < 70 else "High Load", delta_color="normal" if avg_cpu < 70 else "inverse")
c2.metric("Aggregate Memory Usage", f"{total_ram_used:.1f} / {total_ram_cap:.1f} GB", delta=f"{ram_pct:.1f}% utilized")
c3.metric("Fleet Network Throughput", f"{total_net_bw:.1f} MB/s")
c4.metric("Active Cloud Alarms", f"{critical_count} Alert(s)", delta="All Normal" if critical_count == 0 else "Threshold Warning", delta_color="normal" if critical_count == 0 else "inverse")

st.markdown("<hr style='margin: 16px 0;'>", unsafe_allow_html=True)

# -------------------------------------------------------------
# Instance Cards Grid
# -------------------------------------------------------------
st.subheader("🖥️ Cloud Compute Instances Telemetry")

for name, stats in st.session_state.fleet.items():
    with st.container():
        card_col1, card_col2, card_col3, card_col4 = st.columns([2.5, 2.5, 2.5, 1.5])
        
        with card_col1:
            st.markdown(f"**{name}**")
            st.caption(f"Instance Type: `{stats['type']}` | Status: `{stats['status']}`")
            # Badge
            if stats["status"] == "Healthy":
                st.markdown('<span class="badge-healthy">HEALTHY</span>', unsafe_allow_html=True)
            elif stats["status"] == "Warning":
                st.markdown('<span class="badge-warn">WARNING</span>', unsafe_allow_html=True)
            else:
                st.markdown('<span class="badge-critical">CRITICAL ALARM</span>', unsafe_allow_html=True)

        with card_col2:
            cpu_val = stats["cpu"]
            st.markdown(f"**CPU Utilization:** `{cpu_val:.1f}%`")
            st.progress(min(1.0, cpu_val / 100.0))
            if cpu_val > 80:
                st.caption("⚠️ High CPU load threshold exceeded!")

        with card_col3:
            ram_val = stats["ram_gb"]
            ram_max = stats["ram_max"]
            ram_pct_inst = (ram_val / ram_max) * 100
            st.markdown(f"**Memory (RAM):** `{ram_val:.1f} GB / {ram_max:.1f} GB`")
            st.progress(min(1.0, ram_pct_inst / 100.0))

        with card_col4:
            st.metric("Net I/O", f"{stats['net_mb_s']} MB/s")
            st.metric("Disk Used", f"{stats['disk_pct']}%")

        st.markdown("<hr style='margin: 12px 0; border: 0.5px solid #f1f5f9;'>", unsafe_allow_html=True)

# -------------------------------------------------------------
# Telemetry Charts & Alarm Event Feed
# -------------------------------------------------------------
tab_charts, tab_events = st.tabs(["📈 Simulated Time-Series Metrics", "🚨 CloudWatch Alarms & Events"])

with tab_charts:
    st.subheader("Simulated 24-Hour Utilization Curve")
    # Generate realistic historical time-series data for demonstration
    timestamps = pd.date_range(end=datetime.now(), periods=24, freq="h")
    simulated_df = pd.DataFrame({
        "Timestamp": timestamps,
        "Web Cluster CPU (%)": np.clip(np.random.normal(stats["cpu"], 5, 24), 10, 100),
        "Network Bandwidth (MB/s)": np.clip(np.random.normal(stats["net_mb_s"], 4, 24), 2, 120),
        "Database Memory (%)": np.clip(np.random.normal(70, 3, 24), 50, 95)
    })
    
    st.line_chart(simulated_df, x="Timestamp", y=["Web Cluster CPU (%)", "Network Bandwidth (MB/s)"])

with tab_events:
    st.subheader("Observability Event Stream")
    df_alarms = pd.DataFrame(st.session_state.alarm_logs)
    st.dataframe(df_alarms, use_container_width=True, hide_index=True)
