from pathlib import Path

import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="", layout="wide")

# ----------------
# Customize these
# ----------------
NAME = "Michael C. Sevilla"
ABOUT = (
    "I am currently a fourth year BSIT student at Cebu Institute of Technology - University. "
    "I am an applied AI student and I'm interested in LLMs and building practical projects."
)
PROJECTS = [
    ("BudgetEase", "https://github.com/miikuichi/wander-list"),
    ("PayrollPro", "https://github.com/miikuichi/final-project"),
    ("IntelliTrack", "https://github.com/juswangs12/IntelliTrack"),
]
SKILLS = {"Python": 40, "Java": 60, "ReactJS": 30, "C": 20}


def button_html(link, text="Open"):
    return (
        f'<a href="{link}" target="_blank" style="text-decoration:none;">'
        f'<div style="padding:8px 12px;background:#0e76a8;color:white;'
        f'border-radius:6px;display:inline-block">{text}</div></a>'
    )


# --- Header: big photo on the left, profile info on the right
photo_col, info_col = st.columns([1, 2], gap="large")

with photo_col:
    img = Path("profile.jpg")
    if img.exists():
        st.image(str(img), use_container_width=True)
    else:
        st.markdown(
            '<div style="width:100%;aspect-ratio:1/1;border:2px dashed #999;'
            'border-radius:12px;display:flex;align-items:center;'
            'justify-content:center;color:#666">profile.jpg</div>',
            unsafe_allow_html=True,
        )

with info_col:
    st.title(NAME)
    st.write(ABOUT)
    st.markdown(
        "**Email:** michaelsevilla0927@gmail.com  •  "
        "**LinkedIn:** [profile](https://www.linkedin.com)"
    )

st.markdown("---")

# --- Tabs for sections
tabs = st.tabs(["About", "Projects", "Skills", "Resume & Contact"])

with tabs[0]:
    st.header("About me")
    st.write("- Degree: B.S. Information Technology")
    st.write("- Interests: LLMs, Applied AI, building practical projects")

with tabs[1]:
    st.header("Projects")
    for name, link in PROJECTS:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{name}**")
        with col2:
            st.markdown(button_html(link, "Open Project"), unsafe_allow_html=True)

with tabs[2]:
    st.header("Skills")
    cols = st.columns(2)
    i = 0
    for skill, val in SKILLS.items():
        with cols[i % 2]:
            st.write(f"**{skill}**")
            st.progress(val / 100)
        i += 1

with tabs[3]:
    st.header("Resume & Contact")
    resume = Path("resume.pdf")
    if resume.exists():
        with open(resume, "rb") as f:
            st.download_button("Download Resume", f, file_name="resume.pdf")
    else:
        st.info("Place `resume.pdf` next to this script to enable download.")
    st.markdown(
        "**Contact**: michaelsevilla0927@gmail.com • [LinkedIn](https://www.linkedin.com)"
    )

# small style tweaks
st.markdown(
    """
    <style>
    .stButton>button { border-radius:6px }
    </style>
    """,
    unsafe_allow_html=True,
)