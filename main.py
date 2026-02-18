from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Michael's Portfolio", page_icon="M", layout="wide")

# ── Stardew Valley aesthetic styles (injected first so classes are available) ─
st.html(
    """
    <link href="https://fonts.googleapis.com/css2?family=VT323&family=Lato:wght@400;700&display=swap" rel="stylesheet">
    <style>

    /* Background & base font */
    [data-testid="stAppViewContainer"] {
        background-color: #f7e7c6;
        background-image:
            radial-gradient(circle at 20% 30%, rgba(74,124,89,0.08) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(139,105,20,0.07) 0%, transparent 50%);
    }
    [data-testid="stHeader"] { background: transparent; }
    html, body, [class*="css"] { font-family: 'Lato', sans-serif; color: #3b2a1a; }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: #e8d5a3;
        border-radius: 6px;
        border: 2px solid #8b6914;
        gap: 4px;
        padding: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'VT323', monospace;
        font-size: 20px;
        color: #5a3e2b;
        background: #fdf0d5;
        border-radius: 4px;
        border: 2px solid transparent;
        padding: 4px 16px;
        letter-spacing: 1px;
    }
    .stTabs [aria-selected="true"] {
        background: #4a7c59 !important;
        color: #fdf0d5 !important;
        border: 2px solid #2d5a3d !important;
        box-shadow: 2px 2px 0 #2d5a3d;
    }
    .stTabs [data-baseweb="tab-highlight"] { display: none; }
    .stTabs [data-baseweb="tab-border"] { display: none; }

    /* Cards */
    .sdv-card {
        background: #fdf0d5;
        border: 2px solid #8b6914;
        border-radius: 8px;
        box-shadow: 3px 3px 0 #5a3e2b;
        padding: 16px 20px;
        margin-bottom: 12px;
    }

    /* Profile card elements */
    .sdv-name {
        font-family: 'VT323', monospace;
        font-size: 48px;
        color: #5a3e2b;
        line-height: 1.1;
        letter-spacing: 2px;
    }
    .sdv-tag {
        font-size: 14px;
        color: #4a7c59;
        font-weight: 700;
        letter-spacing: 1px;
        margin: 6px 0 10px 0;
    }
    .sdv-about {
        font-size: 15px;
        color: #3b2a1a;
        line-height: 1.6;
        margin-bottom: 12px;
    }
    .sdv-contact {
        font-size: 14px;
        color: #5a3e2b;
        border-top: 1px dashed #8b6914;
        padding-top: 10px;
    }

    /* Section headers */
    .sdv-section-header {
        font-family: 'VT323', monospace;
        font-size: 34px;
        color: #5a3e2b;
        letter-spacing: 2px;
        margin-bottom: 12px;
        border-bottom: 3px solid #8b6914;
        padding-bottom: 4px;
    }

    /* Skill label */
    .sdv-skill-label {
        padding: 8px 14px;
        margin-bottom: 4px;
        font-size: 15px;
        font-weight: 700;
        color: #3b2a1a;
    }

    /* Progress bar */
    [data-testid="stProgress"] > div > div > div {
        background: #4a7c59;
        border-radius: 4px;
    }
    [data-testid="stProgress"] > div > div {
        background: #e8d5a3;
        border: 1px solid #8b6914;
        border-radius: 4px;
    }

    /* Download / action buttons */
    .stDownloadButton > button, .stButton > button {
        font-family: 'VT323', monospace;
        font-size: 20px;
        background: #4a7c59;
        color: #fdf0d5;
        border: 2px solid #2d5a3d;
        border-radius: 4px;
        box-shadow: 2px 2px 0 #2d5a3d;
        letter-spacing: 1px;
        padding: 6px 20px;
    }
    .stDownloadButton > button:hover, .stButton > button:hover {
        background: #2d5a3d;
        color: #fdf0d5;
        border-color: #1a3d28;
    }

    /* Image frame */
    [data-testid="stImage"] img {
        border: 4px solid #8b6914;
        border-radius: 8px;
        box-shadow: 4px 4px 0 #5a3e2b;
    }

    /* Ensure brown text everywhere inside cards and tabs */
    .sdv-card, .sdv-card p, .sdv-card b, .sdv-card span,
    .sdv-section-header,
    [data-baseweb="tab-panel"] p,
    [data-baseweb="tab-panel"] span,
    [data-baseweb="tab-panel"] b {
        color: #3b2a1a;
    }

    /* Sidebar (if ever used) */
    [data-testid="stSidebar"] { background-color: #e8d5a3; }

    </style>
    """
)

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
        f'<div style="padding:8px 16px;background:#4a7c59;color:#fdf0d5;'
        f'border-radius:4px;display:inline-block;font-family:VT323,monospace;'
        f'font-size:18px;border:2px solid #2d5a3d;letter-spacing:1px;'
        f'box-shadow:2px 2px 0 #2d5a3d;">{text}</div></a>'
    )


def pixel_divider():
    st.markdown(
        '<div style="text-align:center;font-size:18px;color:#8b6914;'
        'letter-spacing:8px;margin:8px 0;">- - - - - - - - - -</div>',
        unsafe_allow_html=True,
    )


# --- Header: photo on left, profile card on right
photo_col, info_col = st.columns([1, 2], gap="large")

with photo_col:
    img = Path("profile.jpg")
    if img.exists():
        st.image(str(img), use_container_width=True)
    else:
        st.markdown(
            '<div style="width:100%;aspect-ratio:1/1;border:4px solid #8b6914;'
            'border-radius:8px;box-shadow:4px 4px 0 #5a3e2b;display:flex;'
            'align-items:center;justify-content:center;color:#8b6914;'
            'font-family:VT323,monospace;font-size:20px;background:#fdf0d5;">'
            '[ profile.jpg ]</div>',
            unsafe_allow_html=True,
        )

with info_col:
    st.markdown(
        f'<div class="sdv-card">'
        f'<div class="sdv-name">{NAME}</div>'
        f'<div class="sdv-tag">BSIT Student  |  Applied AI</div>'
        f'<div class="sdv-about">{ABOUT}</div>'
        f'<div class="sdv-contact">'
        f'Email: <a href="mailto:michaelsevilla0927@gmail.com" style="color:#4a7c59;">michaelsevilla0927@gmail.com</a>'
        f'&nbsp;&nbsp;|&nbsp;&nbsp;'
        f'<a href="https://www.linkedin.com" target="_blank" style="color:#4a7c59;">LinkedIn</a>'
        f'</div></div>',
        unsafe_allow_html=True,
    )

pixel_divider()

# --- Tabs for sections
tabs = st.tabs(["About", "Projects", "Skills", "Resume & Contact"])

with tabs[0]:
    st.markdown('<div class="sdv-section-header">About Me</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sdv-card">'
        '<p><b>Degree:</b> B.S. Information Technology — Cebu Institute of Technology - University</p>'
        '<p><b>Interests:</b> Large Language Models, Applied AI, building practical projects</p>'
        '<p><b>Currently learning:</b> Prompt engineering, ML fundamentals, full-stack development</p>'
        '</div>',
        unsafe_allow_html=True,
    )

with tabs[1]:
    st.markdown('<div class="sdv-section-header">Projects</div>', unsafe_allow_html=True)
    for name, link in PROJECTS:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f'<div class="sdv-card"><b>{name}</b></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div style="padding-top:10px">' + button_html(link, "Open") + '</div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="sdv-section-header">Skills</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    i = 0
    for skill, val in SKILLS.items():
        with cols[i % 2]:
            st.markdown(
                f'<div class="sdv-card sdv-skill-label">'
                f'<span>{skill}</span><span style="float:right;color:#8b6914">{val}%</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
            st.progress(val / 100)
        i += 1

with tabs[3]:
    st.markdown('<div class="sdv-section-header">Resume & Contact</div>', unsafe_allow_html=True)
    resume = Path("resume.pdf")
    st.markdown('<div class="sdv-card">', unsafe_allow_html=True)
    if resume.exists():
        with open(resume, "rb") as f:
            st.download_button("Download Resume", f, file_name="resume.pdf")
    else:
        st.info("Place `resume.pdf` next to this script to enable the download button.")
    st.markdown(
        "**Email:** michaelsevilla0927@gmail.com  "
        "**LinkedIn:** [profile](https://www.linkedin.com)"
    )
    st.markdown('</div>', unsafe_allow_html=True)

