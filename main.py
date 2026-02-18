from pathlib import Path

import streamlit as st


st.set_page_config(page_title="My Portfolio", page_icon="", layout="wide")

st.title("My Portfolio")

# Update these values with your own details.
NAME = "Michael C. Sevilla"
ABOUT = (
	"I am currently a fourth year BSIT student at Cebu Institute of Technology - University. Currently, I am"
	"an applied AI student and I'm interested in LLMs and building practical projects."
)

# Add your real project links here.
PROJECTS = [
	("IntelliTrack", "https://github.com/juswangs12/IntelliTrack"),
	("PayrollPro", "https://github.com/miikuichi/final-project"),
	("BudgetEase", "https://github.com/miikuichi/wander-list"),
]

photo_col, info_col = st.columns([1, 3], gap="large")

with photo_col:
	image_path = Path("profile.jpg")
	if image_path.exists():
		st.image(str(image_path), use_container_width=True)
	import streamlit as st
	from pathlib import Path

	st.set_page_config(page_title="Portfolio", layout="wide", page_icon="👩‍💻")

	# ----------------
	# Customize these
	# ----------------
	NAME = "Your Name"
	ABOUT = "Applied AI student — I build data projects and small ML demos."
	PROJECTS = [
		("Air Quality Analysis", "https://github.com/your-username/air-quality"),
		("NumPy Notebooks", "https://github.com/your-username/numpy-notebooks"),
		("DS Exercises", "https://github.com/your-username/ds-exercises"),
	]
	SKILLS = {"Python": 90, "NumPy": 85, "Pandas": 80, "ML": 70}

	def button_html(link, text="Open"):
		return (
			f'<a href="{link}" target="_blank" style="text-decoration:none;">'
			f'<div style="padding:8px 12px;background:#0e76a8;color:white;border-radius:6px;display:inline-block">{text}</div></a>'
		)


	# --- Header with photo and bio
	left, right = st.columns([1, 3], gap="large")
	with left:
		img = Path("profile.jpg")
		if img.exists():
			st.image(str(img), width=220)
		else:
			st.markdown(
				'<div style="width:220px;height:220px;border:2px dashed #999;border-radius:12px;display:flex;align-items:center;justify-content:center;color:#666">profile.jpg</div>',
				unsafe_allow_html=True,
			)

	with right:
		st.title(NAME)
		st.write(ABOUT)
		st.markdown(
			"**Email:** you@example.com  •  **LinkedIn:** [profile](https://www.linkedin.com)")

	st.markdown("---")


	# --- Tabs for sections
	tabs = st.tabs(["About", "Projects", "Skills", "Resume & Contact"])

	with tabs[0]:
		st.header("About me")
		st.write("- Degree: B.S. Applied AI (expected YYYY)")
		st.write("- Interests: data cleaning, visualization, ML prototyping")
		with st.expander("Education & Coursework"):
			st.write("- Course 1, Course 2, Course 3")

	with tabs[1]:
		st.header("Projects")
		for name, link in PROJECTS:
			col1, col2 = st.columns([3, 1])
			with col1:
				st.markdown(f"**{name}**")
				st.write("Short 1–2 line description of the project and tech used.")
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
		st.markdown("\n**Contact**: you@example.com • [LinkedIn](https://www.linkedin.com)")


	# small style tweaks
	st.markdown(
		"""
		<style>
		.stButton>button { border-radius:6px }
		</style>
		""",
		unsafe_allow_html=True,
	)