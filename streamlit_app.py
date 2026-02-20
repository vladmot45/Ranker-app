import streamlit as st

GOOGLE_REVIEW_URL = "https://www.google.com/maps/place/Z%C5%82ote+ziarno+Sp.+Z.o.o/@52.2254847,21.0050983,17z/data=!3m1!4b1!4m6!3m5!1s0x471ecc81b62f0f05:0xf54b887a45c43bfc!8m2!3d52.2254847!4d21.0050983!16s%2Fg%2F11mv_49jpf?entry=ttu&g_ep=EgoyMDI2MDIxNy4wIKXMDSoASAFQAw%3D%3D"

st.set_page_config(page_title="Give us a rating!", layout="centered")

if "screen" not in st.session_state:
    st.session_state.screen = "rate"
if "rating" not in st.session_state:
    st.session_state.rating = None

def go_to_review(r: int):
    st.session_state.rating = r
    st.session_state.screen = "review"
    st.rerun()

def go_back():
    st.session_state.rating = None
    st.session_state.screen = "rate"
    st.rerun()

st.markdown(
    """
<style>
.center-col { max-width: 320px; margin: 0 auto; }
.starlink {
  display: block;
  text-align: center;
  font-size: 80px;
  line-height: 1.1;
  padding: 18px 12px;
  margin: 10px 0;
  border: 1px solid rgba(49,51,63,0.2);
  border-radius: 12px;
  text-decoration: none !important;
}
.starlink:hover { background: rgba(49,51,63,0.06); }
.starbtn button {
  width: 100% !important;
  font-size: 80px !important;
  padding: 18px 12px !important;
  border-radius: 12px !important;
}
</style>
""",
    unsafe_allow_html=True
)

if st.session_state.screen == "rate":
    st.title("Give us a rating!")
    st.markdown('<div class="center-col">', unsafe_allow_html=True)

    # 5 and 4 stars = direct external link (one click, Cloud-safe)
    st.markdown(
        f'<a class="starlink" href="{GOOGLE_REVIEW_URL}" target="_blank" rel="noopener noreferrer">{"⭐"*5}</a>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<a class="starlink" href="{GOOGLE_REVIEW_URL}" target="_blank" rel="noopener noreferrer">{"⭐"*4}</a>',
        unsafe_allow_html=True
    )

    # 3/2/1 stars = Streamlit buttons (go to review screen)
    st.markdown('<div class="starbtn">', unsafe_allow_html=True)
    if st.button("⭐⭐⭐", key="r3"):
        go_to_review(3)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="starbtn">', unsafe_allow_html=True)
    if st.button("⭐⭐", key="r2"):
        go_to_review(2)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="starbtn">', unsafe_allow_html=True)
    if st.button("⭐", key="r1"):
        go_to_review(1)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.screen == "review":
    st.title("Tell us what went wrong")
    st.write(f"Rating: {'⭐' * st.session_state.rating}")

    st.text_area("Write your review", placeholder="Explain your experience...")

    col1, col2 = st.columns(2)
    if col1.button("Submit"):
        st.success("Thank you for your feedback.")
    if col2.button("Back"):
        go_back()