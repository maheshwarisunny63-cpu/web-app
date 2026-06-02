import streamlit as st
import time

st.set_page_config(
    page_title="Birthday Surprise",
    page_icon="🎂",
    layout="centered"
)

# ---------------- CLEAN UI ----------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #ff2e63;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.1);
    margin-top: 20px;
}

.big-text {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #ff4b4b;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg,#ff4b4b,#ff0066);
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🎂 Birthday Surprise Generator</div>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    name = st.text_input("Name", "Anonymous")
    age = st.number_input("Age", 1, 120, 18)

    message = st.text_area(
        "Message",
        f"Happy {age}th Birthday {name}! Wishing you joy and success."
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- START BUTTON ----------------
start = st.button("🎁 Start Celebration")

# ---------------- CELEBRATION ----------------
if start:

    # STEP 1: progress (build suspense)
    progress = st.progress(0)
    status = st.empty()

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
        status.text(f"Preparing celebration... {i+1}%")

    status.success("🎉 Celebration Ready!")

    # STEP 2: balloons
    st.balloons()

    # STEP 3: title reveal
    st.markdown(f"""
    <div class='card'>
        <div class='big-text'>
            🎂 Happy {age}th Birthday {name}! 🎂
        </div>
    </div>
    """, unsafe_allow_html=True)

    # STEP 4: message
    st.info(message)

    # STEP 5: AUDIO (user-triggered autoplay simulation)
    st.markdown("### 🎶 Birthday Song Starts Now")
    st.audio("birthday.mp3", autoplay=True)

    # STEP 6: confetti
    st.snow()

    st.success("🎊 Celebration complete!")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎁 About This App")
st.sidebar.info("""
A professional app designed to give birthday wishes 
to your dear friends and family members

Developed by Sunny Maheshwari a.k.a Sk Don
""")