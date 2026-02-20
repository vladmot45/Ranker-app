import streamlit as st

GOOGLE_REVIEW_URL = "https://www.google.com/maps/place/Z%C5%82ote+ziarno+Sp.+Z.o.o/@52.2254847,21.0050983,17z/data=!3m1!4b1!4m6!3m5!1s0x471ecc81b62f0f05:0xf54b887a45c43bfc!8m2!3d52.2254847!4d21.0050983!16s%2Fg%2F11mv_49jpf?entry=ttu&g_ep=EgoyMDI2MDIxNy4wIKXMDSoASAFQAw%3D%3D"

st.set_page_config(page_title="Give us a rating!", layout="centered")

# --- STATE ---
if "screen" not in st.session_state:
    st.session_state.screen = "rate"   # "rate" or "review"
if "rating" not in st.session_state:
    st.session_state.rating = None

def go_back():
    st.session_state.rating = None
    st.session_state.screen = "rate"
    st.query_params.clear()
    st.rerun()

# --- STYLE (all rows are the same: HTML cards) ---
st.markdown("""
<style>
.center-col { max-width: 340px; margin: 0 auto; }

.starcard{
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 80px;
  height: 140px;
  margin: 16px 0;
  border-radius: 16px;
  border: 1px solid rgba(49,51,63,0.25);
  background: rgba(255,255,255,0.02);
  text-decoration: none !important;
  cursor: pointer;
}
.starcard:hover{
  background: rgba(255,255,255,0.05);
}
</style>
""", unsafe_allow_html=True)

# --- QUERY PARAM HANDLER FOR 1–3 STARS ---
qp = st.query_params
if st.session_state.screen == "rate" and "rate" in qp:
    try:
        r = int(qp["rate"])
        if r in (1, 2, 3):
            st.session_state.rating = r
            st.session_state.screen = "review"
            st.query_params.clear()  # clean URL after selection
    except Exception:
        st.query_params.clear()

# --- UI ---
if st.session_state.screen == "rate":
    st.title("Give us a rating!")
    st.markdown('<div class="center-col">', unsafe_allow_html=True)

    # 5–4 stars: one-click external (Cloud-safe)
    st.markdown(
        f'<a class="starcard" href="{GOOGLE_REVIEW_URL}" target="_blank" rel="noopener noreferrer">{"⭐"*5}</a>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<a class="starcard" href="{GOOGLE_REVIEW_URL}" target="_blank" rel="noopener noreferrer">{"⭐"*4}</a>',
        unsafe_allow_html=True
    )

    # 3–1 stars: same-size cards, one-click, routed via query param
    st.markdown(f'<a class="starcard" href="?rate=3">{"⭐"*3}</a>', unsafe_allow_html=True)
    st.markdown(f'<a class="starcard" href="?rate=2">{"⭐"*2}</a>', unsafe_allow_html=True)
    st.markdown(f'<a class="starcard" href="?rate=1">{"⭐"*1}</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.screen == "review":
    st.title("Tell us what went wrong")
    st.write(f"Rating: {'⭐' * (st.session_state.rating or 0)}")

    st.text_area("Write your review", placeholder="Explain your experience...")

    col1, col2 = st.columns(2)
    if col1.button("Submit"):
        st.success("Thank you for your feedback.")
    if col2.button("Back"):
        go_back()