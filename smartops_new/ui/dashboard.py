import streamlit as st
import time
from core.shared_state import STATE, LOCK

st.set_page_config(layout="wide")
st.title("🧠 SmartOps – Real-Time System Monitor")

cpu_chart = st.line_chart([])
mem_chart = st.line_chart([])
disk_chart = st.line_chart([])
alert_box = st.empty()

while True:
    with LOCK:
        cpu = STATE["cpu"]
        mem = STATE["memory"]
        disk = STATE["disk"]
        alerts = STATE["alerts"][-5:]

    cpu_chart.add_rows([cpu])
    mem_chart.add_rows([mem])
    disk_chart.add_rows([disk])

    if alerts:
        alert_box.warning("\n".join(alerts))
    else:
        alert_box.success("All systems stable")

    time.sleep(2)
