import streamlit as st
from urllib.parse import quote


# --- CONFIG ---
GOOGLE_REVIEW_URL = "https://www.google.com/maps/place/Z%C5%82ote+ziarno+Sp.+Z.o.o/@52.2254847,21.0050983,17z/data=!3m1!4b1!4m6!3m5!1s0x471ecc81b62f0f05:0xf54b887a45c43bfc!8m2!3d52.2254847!4d21.0050983!16s%2Fg%2F11mv_49jpf?entry=ttu&g_ep=EgoyMDI2MDIxNy4wIKXMDSoASAFQAw%3D%3D"

st.set_page_config(page_title="Give us a rating!", layout="centered")

# --- STATE ---
if "screen" not in st.session_state:
    st.session_state.screen = "rate"
if "rating" not in st.session_state:
    st.session_state.rating = None

def go_to_review(r):
    st.session_state.rating = r
    st.session_state.screen = "review"

def go_back():
    st.session_state.screen = "rate"
    st.session_state.rating = None


# --- CUSTOM STAR STYLE ---
st.markdown("""
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
""", unsafe_allow_html=True)


# --- SCREEN 1 : RATING ---
if st.session_state.screen == "rate":

    st.title("Give us a rating!")

    st.markdown('<div class="center-col">', unsafe_allow_html=True)

    # 5 stars (top)
    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    if st.button("⭐⭐⭐⭐⭐", key="r5"):
        st.success("Thank you!")
        st.markdown(
            f'<a href="{GOOGLE_REVIEW_URL}" target="_blank">'
            f'<button style="font-size:20px;padding:12px 24px;">'
            f'Continue to Google Reviews</button></a>',
            unsafe_allow_html=True
        )
        st.stop()
    st.markdown('</div>', unsafe_allow_html=True)

    # 4 stars
    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    if st.button("⭐⭐⭐⭐", key="r4"):
        st.success("Thank you!")
        st.markdown(
            f'<a href="{GOOGLE_REVIEW_URL}" target="_blank">'
            f'<button style="font-size:20px;padding:12px 24px;">'
            f'Continue to Google Reviews</button></a>',
            unsafe_allow_html=True
        )
        st.stop()
    st.markdown('</div>', unsafe_allow_html=True)

    # 3 stars
    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    if st.button("⭐⭐⭐", key="r3"):
        go_to_review(3)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2 stars
    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    if st.button("⭐⭐", key="r2"):
        go_to_review(2)
    st.markdown('</div>', unsafe_allow_html=True)

    # 1 star (bottom)
    st.markdown('<div class="star-btn">', unsafe_allow_html=True)
    if st.button("⭐", key="r1"):
        go_to_review(1)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# --- SCREEN 2 : REVIEW ---
elif st.session_state.screen == "review":

    st.title("Tell us what went wrong")

    st.write(f"Rating: {'⭐' * st.session_state.rating}")

    review = st.text_area(
        "Write your review",
        placeholder="Explain your experience..."
    )

    col1, col2 = st.columns(2)

    if col1.button("Submit"):
        st.success("Thank you for your feedback.")

    if col2.button("Back"):
        go_back()