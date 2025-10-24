import streamlit as st
import time
import random
from datetime import datetime

# ---------------------------
# PAGE CONFIGURATION
# ---------------------------
st.set_page_config(page_title="Gen-AI Court Marking Vehicle Dashboard", layout="wide")

# Title
st.markdown("<h2 style='text-align:center;color:#F8F9FA;'>🏀 Gen-AI Based Court Marking Vehicle Dashboard (Dark UI)</h2>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------
# SIDEBAR - Control Panel
# ---------------------------
st.sidebar.header("⚙️ Vehicle Control Panel")

# Vehicle control buttons
if st.sidebar.button("Start Marking"):
    status = "MARKING ACTIVE"
elif st.sidebar.button("Pause"):
    status = "PAUSED"
elif st.sidebar.button("Stop"):
    status = "STOPPED"
else:
    status = "IDLE"

# ---------------------------
# SENSOR SIMULATION DATA
# ---------------------------
gps_location = "13.0430N, 80.2110E"
speed = round(random.uniform(0.5, 1.2), 2)
paint_level = round(random.uniform(70, 100), 2)
battery_level = round(random.uniform(70, 100), 2)
error_status = "None"
ai_prediction = random.choice(["Line Detected ✅", "No Line ❌", "Obstacle Detected ⚠️"])
paint_used = round(100 - paint_level, 2)

# ---------------------------
# LAYOUT
# ---------------------------
col1, col2 = st.columns([2, 1])

# ---------------------------
# LEFT PANEL - CONSOLE VIEW
# ---------------------------
with col1:
    st.subheader("🖥️ Console View")

    st.code(f"""
+--------------------------------------------------+
|          GEN-AI COURT MARKING VEHICLE DASHBOARD  |
+--------------------------------------------------+
| [LIVE CAMERA FEED] | GPS: {gps_location}
| [AI DETECTED STATUS] | {ai_prediction}
| SPEED: {speed} m/s  | BATTERY: {battery_level}%
| STATUS: {status}
+--------------------------------------------------+
| [START] [STOP] [PAUSE] [RESET] [MANUAL CONTROL]
+--------------------------------------------------+
| PAINT LEVEL: {paint_level}% | ERRORS: {error_status}
+--------------------------------------------------+
| [Graph: Paint Used vs Time]
+--------------------------------------------------+
""", language="text")

    # Paint usage line graph simulation
    st.subheader("📊 Paint Usage Over Time")
    chart_data = {
        "Time": [datetime.now().strftime("%H:%M:%S") for _ in range(10)],
        "Paint Level (%)": [paint_level - random.uniform(0, 1) for _ in range(10)]
    }
    st.line_chart(chart_data, x="Time", y="Paint Level (%)")

# ---------------------------
# RIGHT PANEL - SENSOR DATA
# ---------------------------
with col2:
    st.subheader("📡 Sensor Data")

    st.metric("Paint Level (%)", f"{paint_level}%", delta=f"-{paint_used}% used")
    st.progress(paint_level / 100)

    st.metric("Battery (%)", f"{battery_level}%")
    st.progress(battery_level / 100)

    st.text(f"GPS Location: {gps_location}")
    st.text(f"Speed: {speed} m/s")

    st.subheader("🧠 AI Status")
    st.info(ai_prediction)

    st.subheader("⚠️ Error Status")
    st.success(error_status)

# ---------------------------
# REFRESH BUTTON
# ---------------------------
st.markdown("---")
if st.button("🔄 Refresh Dashboard"):
    st.experimental_rerun()
