import streamlit as st
import requests

API_URL = "https://leads-scraper-production.up.railway.app"

st.set_page_config(page_title="Deal Flow Assistant", layout="wide")
st.title("🤖 Deal Flow Assistant")

st.markdown("Paste a list of company URLs below (one per line):")

urls_text = st.text_area("Company URLs", height=200)
urls = [u.strip() for u in urls_text.split("\n") if u.strip()]

if "results" not in st.session_state:
    st.session_state.results = []

if st.button("Analyze Companies") and urls:
    with st.spinner("Scraping and generating insights..."):
        try:
            response = requests.post(f"{API_URL}/scrape", json={"urls": urls})
            response.raise_for_status()
            st.session_state.results = response.json()
        except Exception as e:
            st.error(f"Scraping failed: {e}")

for i, result in enumerate(st.session_state.results):
    st.divider()
    st.subheader(result['url'])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"**Tech Stack:** {', '.join(result.get('tech_stack', [])) or '-'}")
        st.markdown(
            f"**Neglect Signals:** Footer Year: {result['neglect_signals'].get('footer_year', '-')}, Last Blog: {result['neglect_signals'].get('last_blog_post', '-')}")

        st.markdown(
            f"**Stability Signals:** {', '.join(result.get('stability_signals', [])) or '-'}")
        st.markdown(
            f"**Growth Signals:** {', '.join(result.get('growth_signals', [])) or '-'}")
    with col2:
        st.metric("💡 Fit Score", result.get('fit_score', '-'))

    st.expander("📄 Deal Memo").write(result.get('deal_memo', 'Not available'))

    with st.expander("✉️ Outreach Email"):
        if result.get("outreach_email"):
            st.write(result["outreach_email"])
        else:
            if st.button(f"Generate Outreach Email", key=f"outreach_btn_{i}"):
                with st.spinner("Generating outreach email..."):
                    try:
                        res = requests.post(
                            f"{API_URL}/generate-outreach-email", json={"data": result})
                        if res.status_code == 200:
                            st.session_state.results[i]["outreach_email"] = res.json().get(
                                "outreach_email")
                            st.success("Outreach email generated!")
                            st.write(
                                st.session_state.results[i]["outreach_email"])
                        else:
                            st.error("Failed to generate outreach email.")
                    except Exception as e:
                        st.error(f"Error: {e}")