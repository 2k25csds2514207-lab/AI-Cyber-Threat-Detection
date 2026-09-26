import os
import sys
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Ensure local module directory is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_loader import load_alerts_data

st.set_page_config(
    page_title="AI Cyber Threat Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS STYLING (DAY 7 POLISH) ----------
st.markdown("""
<style>
    /* Metric Card Polish */
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 10px;
        padding: 12px 18px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        border-color: rgba(0, 240, 255, 0.35);
    }
    /* Section Divider Styling */
    hr {
        border-color: rgba(255, 255, 255, 0.08);
        margin: 18px 0;
    }
    /* Top status badge */
    .status-strip {
        background: linear-gradient(90deg, rgba(16, 185, 129, 0.15) 0%, rgba(6, 78, 59, 0.05) 100%);
        border-left: 4px solid #10b981;
        padding: 8px 14px;
        border-radius: 4px;
        font-size: 0.9rem;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:

    st.markdown("## 🛡️ AI Cyber Threat Detection")
    st.caption("Unidirectional IP Traffic Monitoring")

    st.success("● Monitoring Active (RX-Only)")

    st.markdown("---")

    st.markdown("### NAVIGATION")

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "Threat Analytics",
            "Live Alerts",
            "Traffic Analysis",
            "About Project"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### FILTERS")

    threat_type = st.selectbox(
        "Threat Type",
        [
            "All Classifications",
            "DDoS",
            "Botnet C2 Beaconing",
            "DGA / DNS Tunnelling",
            "Encrypted Malware",
            "Port Scanning",
            "Data Exfiltration"
        ]
    )

    severity = st.multiselect(
        "Severity",
        ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
        default=["HIGH", "CRITICAL"]
    )

    confidence = st.slider(
        "Minimum Confidence",
        0,
        100,
        75
    )

    time_range = st.selectbox(
        "Time Range",
        ["Last 1 Hour", "Last 6 Hours", "Last 24 Hours", "Last 7 Days"]
    )

    st.markdown("---")
    with st.expander("ℹ️ System Telemetry", expanded=False):
        st.markdown("**Diode Link:** `10 Gbps Simplex`")
        st.markdown("**Tap Mode:** `Optical RX-Only`")
        st.markdown("**Model Version:** `Random Forest v2.4`")
        st.markdown("**Egress Protection:** `Hardware Enforced`")


# ---------- TOP HEADER (COMMON) ----------
st.title("AI Cyber Threat Detection")
st.caption("Unidirectional IP Traffic Passive Monitoring & AI Threat Classification | SOC Operations")

st.info("🟢 Monitoring Active | Optical Data Diode (RX-Only) | Passive Read-Only Traffic Inspection")

st.markdown("---")

# ==========================================
# PAGE 1: OVERVIEW
# ==========================================
if page == "Overview":

    st.subheader("System Overview")
    st.caption("Executive overview of unidirectional flows, active threats, and model performance.")

    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total Flows Analyzed",
            value="128,462",
            delta="12% vs previous 24h"
        )

    with col2:
        st.metric(
            label="Threats Detected",
            value="2,843",
            delta="8% vs previous 24h"
        )

    with col3:
        st.metric(
            label="High / Critical Alerts",
            value="412",
            delta="15%",
            delta_color="inverse"
        )

    with col4:
        st.metric(
            label="Average Model Confidence",
            value="91.7%",
            delta="2% vs previous run"
        )

    st.markdown("---")

    # Interactive Plotly Charts
    ch_col1, ch_col2 = st.columns([3, 2])

    with ch_col1:
        st.markdown("### Threat Ingestion Velocity (Past 6 Hours)")
        time_df = pd.DataFrame({
            "Time": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
            "Threats": [18, 25, 21, 34, 28, 42]
        })
        fig_timeline = px.area(
            time_df,
            x="Time",
            y="Threats",
            markers=True,
            color_discrete_sequence=["#00F0FF"]
        )
        fig_timeline.update_layout(
            template="plotly_dark",
            margin=dict(l=20, r=20, t=30, b=20),
            height=280,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_timeline, width="stretch")

    with ch_col2:
        st.markdown("### Threat Share by Classification")
        threat_pie_df = pd.DataFrame({
            "Classification": ["DDoS", "Port Scanning", "Botnet C2", "DGA / DNS", "Encrypted Malware", "Data Exfiltration"],
            "Incidents": [42, 35, 31, 24, 18, 12]
        })
        fig_donut = px.pie(
            threat_pie_df,
            names="Classification",
            values="Incidents",
            hole=0.55,
            color_discrete_sequence=["#FF4B4B", "#FFA500", "#A855F7", "#3B82F6", "#06B6D4", "#10B981"]
        )
        fig_donut.update_layout(
            template="plotly_dark",
            margin=dict(l=10, r=10, t=30, b=10),
            height=280,
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_donut, width="stretch")

    st.markdown("---")

    # Data Diode Hardware Telemetry
    st.markdown("### Unidirectional Hardware Diode Status")
    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown("🔒 **Optical RX Link:** `10 Gbps Simplex (Up)`")
    with d2:
        st.markdown("⚡ **Buffer Utilization:** `18.4% (Optimal)`")
    with d3:
        st.markdown("🛡️ **Reverse Leak Prevention:** `100% Hardware Enforced`")

    st.markdown("---")

    # Recent High-Priority Alerts Snapshot
    st.markdown("### High-Priority Alerts (Snapshot)")
    df_alerts = load_alerts_data()
    high_crit_df = df_alerts[df_alerts["Severity"].isin(["CRITICAL", "HIGH"])].copy()
    sev_map = {"CRITICAL": "🔴 CRITICAL", "HIGH": "🟠 HIGH"}
    high_crit_df["Severity"] = high_crit_df["Severity"].map(sev_map)

    st.dataframe(
        high_crit_df[["Timestamp", "Flow ID", "Source", "Destination", "Threat Type", "Severity", "Confidence", "Evidence"]],
        column_config={
            "Confidence": st.column_config.ProgressColumn(
                "Confidence",
                help="AI Model prediction certainty",
                format="%d%%",
                min_value=0,
                max_value=100
            )
        },
        width="stretch",
        hide_index=True
    )


# ==========================================
# PAGE 2: THREAT ANALYTICS
# ==========================================
elif page == "Threat Analytics":

    st.subheader("Threat Analytics & Forensic Visualizations")
    st.caption("Deep-dive telemetry into detected anomaly signatures, volumetric patterns, and severity rankings.")

    # Row 1: Charts
    r1_col1, r1_col2 = st.columns(2)

    with r1_col1:
        st.markdown("### Threats Detected Over Time")
        time_df = pd.DataFrame({
            "Time": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
            "Threats": [18, 25, 21, 34, 28, 42]
        })
        fig_line = px.line(
            time_df,
            x="Time",
            y="Threats",
            markers=True,
            color_discrete_sequence=["#00F0FF"]
        )
        fig_line.update_layout(
            template="plotly_dark",
            margin=dict(l=20, r=20, t=30, b=20),
            height=300,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_line, width="stretch")

    with r1_col2:
        st.markdown("### Threat Classification Distribution")
        threat_df = pd.DataFrame({
            "Threat": [
                "DDoS",
                "Port Scanning",
                "Botnet C2",
                "DGA / DNS",
                "Encrypted Malware",
                "Data Exfiltration"
            ],
            "Count": [42, 35, 31, 24, 18, 12]
        })
        fig_bar = px.bar(
            threat_df,
            x="Threat",
            y="Count",
            color="Threat",
            color_discrete_sequence=["#FF4B4B", "#FFA500", "#A855F7", "#3B82F6", "#06B6D4", "#10B981"]
        )
        fig_bar.update_layout(
            template="plotly_dark",
            margin=dict(l=20, r=20, t=30, b=20),
            height=300,
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_bar, width="stretch")

    st.markdown("---")

    # Row 2: Severity Distribution & Confidence Analytics
    r2_col1, r2_col2 = st.columns(2)

    with r2_col1:
        st.markdown("### Severity Distribution")
        sev_df = pd.DataFrame({
            "Severity Level": ["CRITICAL", "HIGH", "MEDIUM", "LOW"],
            "Count": [412, 824, 1140, 467]
        })
        fig_sev = px.bar(
            sev_df,
            x="Severity Level",
            y="Count",
            color="Severity Level",
            color_discrete_map={
                "CRITICAL": "#EF4444",
                "HIGH": "#F97316",
                "MEDIUM": "#FBBF24",
                "LOW": "#10B981"
            }
        )
        fig_sev.update_layout(
            template="plotly_dark",
            margin=dict(l=20, r=20, t=30, b=20),
            height=300,
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_sev, width="stretch")

    with r2_col2:
        st.markdown("### Average AI Confidence by Threat Category")
        conf_df = pd.DataFrame({
            "Threat": ["DDoS", "Data Exfiltration", "Port Scanning", "DGA / DNS", "Botnet C2", "Encrypted Malware"],
            "Avg Confidence": [96.2, 93.4, 91.0, 88.5, 84.1, 78.6]
        })
        fig_conf = px.bar(
            conf_df,
            x="Threat",
            y="Avg Confidence",
            text="Avg Confidence",
            color="Avg Confidence",
            color_continuous_scale="Viridis"
        )
        fig_conf.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig_conf.update_layout(
            template="plotly_dark",
            margin=dict(l=20, r=20, t=30, b=20),
            height=300,
            yaxis=dict(range=[50, 105]),
            coloraxis_showscale=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_conf, width="stretch")


# ==========================================
# PAGE 3: LIVE ALERTS (DAY 6 & DAY 7 POLISHED)
# ==========================================
elif page == "Live Alerts":

    st.subheader("Live Threat Alerts")
    st.caption("Real-Time Flow Telemetry, Severity Classification & AI Confidence Calibration Display")

    df_alerts = load_alerts_data()

    # ---------- SEVERITY & CONFIDENCE KPI METRICS ----------
    st.markdown("### Severity & Confidence Overview")
    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    crit_count = int((df_alerts["Severity"] == "CRITICAL").sum())
    high_count = int((df_alerts["Severity"] == "HIGH").sum())
    med_count = int((df_alerts["Severity"] == "MEDIUM").sum())
    low_count = int((df_alerts["Severity"] == "LOW").sum())
    avg_conf = float(df_alerts["Confidence"].mean())

    with kpi1:
        st.metric(label="🔴 Critical", value=crit_count, delta="Immediate action", delta_color="inverse")
    with kpi2:
        st.metric(label="🟠 High", value=high_count, delta="Priority review")
    with kpi3:
        st.metric(label="🟡 Medium", value=med_count, delta="Monitored")
    with kpi4:
        st.metric(label="🟢 Low", value=low_count, delta="Informational")
    with kpi5:
        st.metric(label="🎯 Avg Confidence", value=f"{avg_conf:.1f}%", delta="Current alerts")

    st.markdown("---")

    # ---------- FILTER INTEGRATION ----------
    filtered_df = df_alerts.copy()
    if severity:
        filtered_df = filtered_df[filtered_df["Severity"].isin(severity)]
    filtered_df = filtered_df[filtered_df["Confidence"] >= confidence]
    if threat_type != "All Classifications":
        filtered_df = filtered_df[filtered_df["Threat Type"] == threat_type]

    st.markdown(
        f"**Active Filters:** Showing **{len(filtered_df)}** of **{len(df_alerts)}** alerts "
        f"| Severity: `{', '.join(severity) if severity else 'All'}` "
        f"| Min Confidence: `≥ {confidence}%` "
        f"| Threat Type: `{threat_type}`"
    )

    # ---------- ALERTS TABLE WITH PROGRESS BAR & SEVERITY BADGES ----------
    if filtered_df.empty:
        st.warning("⚠️ No alerts match current filter criteria. Try lowering the Minimum Confidence slider or adding more Severity levels.")
    else:
        display_df = filtered_df.copy()
        severity_badges = {
            "CRITICAL": "🔴 CRITICAL",
            "HIGH": "🟠 HIGH",
            "MEDIUM": "🟡 MEDIUM",
            "LOW": "🟢 LOW"
        }
        display_df["Severity Badge"] = display_df["Severity"].map(severity_badges)

        st.dataframe(
            display_df[[
                "Timestamp",
                "Flow ID",
                "Source",
                "Destination",
                "Threat Type",
                "Severity Badge",
                "Confidence",
                "Evidence"
            ]],
            column_config={
                "Confidence": st.column_config.ProgressColumn(
                    "AI Confidence",
                    help="Model prediction certainty (0-100%)",
                    format="%d%%",
                    min_value=0,
                    max_value=100
                ),
                "Severity Badge": st.column_config.TextColumn(
                    "Severity",
                    help="Impact classification level"
                )
            },
            width="stretch",
            hide_index=True
        )

    # ---------- ALERT INSPECTOR ----------
    st.markdown("---")
    st.subheader("🔍 Alert Severity & Confidence Inspector")
    st.caption("Inspect individual flow attributes, AI model confidence score, and classification evidence.")

    flow_options = df_alerts["Flow ID"].tolist()
    selected_flow = st.selectbox("Select Flow ID to Inspect:", flow_options)

    selected_alert = df_alerts[df_alerts["Flow ID"] == selected_flow].iloc[0]

    insp_col1, insp_col2 = st.columns([1, 1])

    with insp_col1:
        st.markdown("#### Severity Classification")
        sev = selected_alert["Severity"]
        if sev == "CRITICAL":
            st.error("🔴 **CRITICAL SEVERITY** — High risk of data loss or service disruption.")
        elif sev == "HIGH":
            st.warning("🟠 **HIGH SEVERITY** — Malicious traffic pattern identified.")
        elif sev == "MEDIUM":
            st.info("🟡 **MEDIUM SEVERITY** — Suspicious beaconing or anomalous connection.")
        else:
            st.success("🟢 **LOW SEVERITY** — Low-risk probe or informational event.")

        st.write(f"**Threat Type:** `{selected_alert['Threat Type']}`")
        st.write(f"**Flow Route:** `{selected_alert['Source']}` ➔ `{selected_alert['Destination']}`")
        st.write(f"**Timestamp:** `{selected_alert['Timestamp']}`")

    with insp_col2:
        st.markdown("#### AI Model Confidence Calibration")
        conf_score = int(selected_alert["Confidence"])
        st.progress(conf_score / 100)

        if conf_score >= 90:
            conf_badge = "🟢 Very High Certainty (≥ 90%)"
        elif conf_score >= 80:
            conf_badge = "🟡 High Certainty (80–89%)"
        else:
            conf_badge = "🟠 Moderate Certainty (< 80%)"

        st.markdown(f"**Confidence Level:** **{conf_score}%** — {conf_badge}")
        st.markdown(f"**Forensic Evidence:** {selected_alert['Evidence']}")


# ==========================================
# PAGE 4: TRAFFIC ANALYSIS
# ==========================================
elif page == "Traffic Analysis":

    st.subheader("Unidirectional IP Traffic Analysis")
    st.caption("Passive telemetry, transport protocol breakdown, and packet distribution across data diode.")

    # Traffic KPIs
    tkpi1, tkpi2, tkpi3, tkpi4 = st.columns(4)
    with tkpi1:
        st.metric(label="Ingress Throughput", value="4.82 Gbps", delta="Stable")
    with tkpi2:
        st.metric(label="Packet Processing Rate", value="320,400 pps", delta="+5.2%")
    with tkpi3:
        st.metric(label="Active Unidirectional Flows", value="42,108", delta="Monitored")
    with tkpi4:
        st.metric(label="Reverse Transmission Leaks", value="0.00%", delta="100% Secure")

    st.markdown("---")

    # Protocol & Packet Size Visuals
    t_col1, t_col2 = st.columns(2)

    with t_col1:
        st.markdown("### Protocol Distribution across Diode")
        proto_df = pd.DataFrame({
            "Protocol": ["TCP (Unidirectional)", "UDP", "ICMP", "DNS / Other"],
            "Percentage": [62.4, 28.7, 5.8, 3.1]
        })
        fig_proto = px.pie(
            proto_df,
            names="Protocol",
            values="Percentage",
            hole=0.5,
            color_discrete_sequence=["#3B82F6", "#06B6D4", "#F59E0B", "#10B981"]
        )
        fig_proto.update_layout(
            template="plotly_dark",
            margin=dict(l=20, r=20, t=30, b=20),
            height=300,
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_proto, width="stretch")

    with t_col2:
        st.markdown("### Packet Size Distribution (MTU Profile)")
        packet_df = pd.DataFrame({
            "Frame Size": ["64B", "128B", "256B", "512B", "1024B", "1500B (Jumbo)"],
            "Packet Volume (k)": [1250, 840, 620, 940, 1560, 2180]
        })
        fig_packet = px.bar(
            packet_df,
            x="Frame Size",
            y="Packet Volume (k)",
            color="Packet Volume (k)",
            color_continuous_scale="Teal"
        )
        fig_packet.update_layout(
            template="plotly_dark",
            margin=dict(l=20, r=20, t=30, b=20),
            height=300,
            coloraxis_showscale=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_packet, width="stretch")

    st.markdown("---")

    # Top Ingress Subnets
    st.markdown("### Top Monitored Ingress Subnets")
    subnet_data = [
        {"Subnet CIDR": "192.168.1.0/24", "Traffic Volume": "1.84 TB", "Active Flows": "14,280", "Threat Alerts": 12, "Diode Interface": "rx-port-01"},
        {"Subnet CIDR": "10.0.0.0/16", "Traffic Volume": "1.42 TB", "Active Flows": "11,850", "Threat Alerts": 9, "Diode Interface": "rx-port-01"},
        {"Subnet CIDR": "172.16.0.0/20", "Traffic Volume": "920 GB", "Active Flows": "8,420", "Threat Alerts": 4, "Diode Interface": "rx-port-02"},
        {"Subnet CIDR": "8.8.0.0/16", "Traffic Volume": "480 GB", "Active Flows": "4,120", "Threat Alerts": 1, "Diode Interface": "rx-port-02"},
    ]
    st.dataframe(pd.DataFrame(subnet_data), width="stretch", hide_index=True)


# ==========================================
# PAGE 5: ABOUT PROJECT
# ==========================================
elif page == "About Project":

    st.subheader("About the Project")
    st.caption("AI-Based Detection of Cyber Threats in Unidirectional IP Traffic")

    st.markdown("""
    ### 🎯 Problem Statement
    In critical network architectures (Defense, SCADA, ICS, and Financial Infrastructures), 
    **Physical Data Diodes** are deployed to enforce strictly unidirectional, one-way IP communication. 
    Because data cannot flow backwards:
    * Standard two-way TCP handshakes (`SYN`, `SYN-ACK`, `ACK`) do not exist.
    * Traditional bidirectional signature and firewall matching fails.
    * **Machine Learning & Statistical Flow Analysis** must passively classify anomalies using one-way ingress features alone.
    """)

    st.markdown("---")

    st.markdown("### ⚙️ System Architecture Pipeline")
    arch_col1, arch_col2, arch_col3, arch_col4 = st.columns(4)

    with arch_col1:
        st.markdown("#### 1. Ingestion")
        st.write("Optical RX-only passive tap captures unidirectional ethernet frames with zero physical return path.")

    with arch_col2:
        st.markdown("#### 2. Flow Reconstructor")
        st.write("Extracts statistical features: inter-arrival packet timing, byte entropy, burst length, and fan-out ratios.")

    with arch_col3:
        st.markdown("#### 3. AI Classifier")
        st.write("Trained Random Forest & Gradient Boosted models classify attack vectors with calibrated confidence scores.")

    with arch_col4:
        st.markdown("#### 4. SOC Alerting")
        st.write("Dispatches real-time severity ratings, forensic evidence tags, and mitigation recommendations.")

    st.markdown("---")

    st.markdown("### 📋 Supported Cyber Threat Classifications")
    threat_info = [
        {"Threat Type": "DDoS", "Unidirectional Signature": "High packet volume surge, compressed inter-arrival time", "Severity": "CRITICAL"},
        {"Threat Type": "Data Exfiltration", "Unidirectional Signature": "Abnormal sustained egress payload ratio, uncharacteristic byte count", "Severity": "CRITICAL"},
        {"Threat Type": "Port Scanning", "Unidirectional Signature": "Rapid fan-out to sequential target ports without handshake completion", "Severity": "HIGH"},
        {"Threat Type": "DGA / DNS Tunnelling", "Unidirectional Signature": "High Shannon entropy in domain queries, abnormal TXT record requests", "Severity": "HIGH"},
        {"Threat Type": "Botnet C2 Beaconing", "Unidirectional Signature": "Periodic low-jitter heartbeat flows to external IP destinations", "Severity": "MEDIUM"},
        {"Threat Type": "Encrypted Malware", "Unidirectional Signature": "Non-standard TLS client hello cipher fingerprints and payload anomalies", "Severity": "MEDIUM"},
    ]
    st.dataframe(pd.DataFrame(threat_info), width="stretch", hide_index=True)
