import streamlit as st

from core.ports import scan_ports
from core.ssl_check import check_ssl
from core.whois_lookup import get_whois
from core.headers import get_headers
from core.risk import calculate_risk

st.title("Cyber Risk Scanner")

domain = st.text_input("Enter Domain")

if st.button("Scan"):
    ports = scan_ports(domain)
    ssl_info = check_ssl(domain)
    whois_data = get_whois(domain)
    headers = get_headers(domain)

    risk = calculate_risk(ports, ssl_info, headers)

    st.subheader("Risk Score")
    st.metric("Risk Score", f"{risk['risk_score']}/100")

    st.subheader("Issues Found")
    for issue in risk["issues"]:
        st.write(f"- {issue}")

    st.subheader("Port Scan")
    st.json(ports)

    st.subheader("SSL Info")
    st.json(ssl_info)

    st.subheader("WHOIS Info")
    st.json(whois_data)