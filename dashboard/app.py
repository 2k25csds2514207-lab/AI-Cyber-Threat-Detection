import streamlit as st

st.set_page_config(
    page_title="AI Cyber Threat Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- SIDEBAR ----------
with st.sidebar:

    st.markdown("## 🛡️ AI Cyber Threat Detection")
    st.caption("Unidirectional IP Traffic Monitoring")

    st.success("● Monitoring Active")

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


# ---------- MAIN AREA ----------

st.title("AI Cyber Threat Detection")

st.subheader(
    "Unidirectional IP Traffic Monitoring & Threat Detection"
)

st.info(
    "🟢 Monitoring Active | "
    "Read-only passive traffic analysis"
)

st.markdown("---")

# ---------- DASHBOARD METRICS ----------

st.subheader("System Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Flows",
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
        label="Average Confidence",
        value="91.7%",
        delta="2%"
    )

# ---------- PLACEHOLDER SECTIONS ----------

if page == "Overview":

    st.header("Overview")

    st.write(
        "Dashboard overview will be implemented here."
    )

elif page == "Threat Analytics":

    st.header("Threat Analytics")

    st.write(
        "Threat analytics and visualizations will be added here."
    )

elif page == "Live Alerts":

    st.header("Live Alerts")

    st.write(
        "Real-time threat alerts will be displayed here."
    )

elif page == "Traffic Analysis":

    st.header("Traffic Analysis")

    st.write(
        "Traffic statistics and flow analysis will be added here."
    )

elif page == "About Project":

    st.header("About Project")

    st.write(
        "AI-Based Detection of Cyber Threats in Unidirectional IP Traffic"
    )
