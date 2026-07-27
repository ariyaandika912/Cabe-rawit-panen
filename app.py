# ===============================
# BACKGROUND CSS
# ===============================

def add_bg():

    st.markdown(
    """
    <style>

    .stApp {

    background-image:
    linear-gradient(
    rgba(255,255,255,0.92),
    rgba(255,255,255,0.92)
    ),
    url("https://images.unsplash.com/photo-1592924357228-91a4daadcfea");

    background-size: cover;

    }


    .card {

    background:white;

    padding:25px;

    border-radius:20px;

    box-shadow:
    0px 5px 20px rgba(0,0,0,0.15);

    text-align:center;

    }


    .title {

    font-size:40px;

    font-weight:bold;

    color:#b30000;

    }


    </style>

    """,
    unsafe_allow_html=True
    )


add_bg()
