import streamlit as st

# --- CONFIG ---
GOOGLE_REVIEW_URL = "https://www.google.com/maps/place/Z%C5%82ote+ziarno+Sp.+Z.o.o/@52.2254847,21.0050983,17z/data=!3m1!4b1!4m6!3m5!1s0x471ecc81b62f0f05:0xf54b887a45c43bfc!8m2!3d52.2254847!4d21.0050983!16s%2Fg%2F11mv_49jpf?entry=ttu&g_ep=EgoyMDI2MDIxNy4wIKXMDSoASAFQAw%3D%3D"

st.set_page_config(page_title="Give us a rating!", layout="centered")

# --- STATE ---
if "screen" not in st.session_state:
    st.session_state.screen = "rate"   # "rate" or "review"
if "rating" not in st.session_state:
    st.session_state.rating = None
if "redirect" not in st.session_state:
    st.session_state.redirect = False

def go_to_review(r: int):
    st.session_state.rating = r
    st.session_state.screen = "review"

def go_back():
    st.session_state.screen = "rate"
    st.session_state.rating = None

def trigger_google_redirect():
    # One-click redirect attempt. Some browsers/platform policies may still block it.
    st.components.v1.html(
        f"""
        <script>
          try {{
            window.top.location.href = "{GOOGLE_REVIEW_URL}";
          }} catch (e) {{
            window.location.href = "{GOOGLE_REVIEW_URL}";
          }}
        </script>
        """,
        height=0,
    )

# --- CUSTOM STAR STYLE ---
st.markdown(
    """
<style>
.star-btn button {
    font-size: 80px !important;
    padding: 30px 45px !important;
    width: 100%;
    border-radius: 12px;
}
.center-col {
    max-width: 300px;
    margin-left: auto;
    margin-right: auto;
}
</style>
""",
    unsafe_allow_html=True
)

# --- SCREEN 1 : RATING ---
if st.session_state.screen == "rate":
    st.title("Give us a rating!")
    st.markdown('<div class="center-col">', unsafe_allow_html=True)

    # Render all buttons first, collect clicks
    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    b5 = st.button("⭐⭐⭐⭐⭐", key="r5")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    b4 = st.button("⭐⭐⭐⭐", key="r4")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    b3 = st.button("⭐⭐⭐", key="r3")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    b2 = st.button("⭐⭐", key="r2")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    b1 = st.button("⭐", key="r1")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Handle action AFTER rendering all five
    if b1:
        go_to_review(1)
        st.rerun()
    if b2:
        go_to_review(2)
        st.rerun()
    if b3:
        go_to_review(3)
        st.rerun()

    if b4 or b5:
        trigger_google_redirect()
        # no st.stop() here; page stays stable even if redirect is blocked

# --- SCREEN 2 : REVIEW ---
elif st.session_state.screen == "review":
    st.title("Tell us what went wrong")
    st.write(f"Rating: {'⭐' * st.session_state.rating}")

    st.text_area("Write your review", placeholder="Explain your experience...")

    col1, col2 = st.columns(2)
    if col1.button("Submit"):
        st.success("Thank you for your feedback.")
    if col2.button("Back"):
        go_back()
        st.rerun()