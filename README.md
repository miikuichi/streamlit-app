# Streamlit Portfolio

This folder contains a simple Streamlit portfolio app.

How to run locally

```powershell
# (optional) create and activate a venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install requirements (from repo root)
python -m pip install -r requirements.txt

# run the app (from repo root)
python -m streamlit run Streamlit\main.py
```

Customize:

- Edit `main.py` to change `NAME`, `ABOUT`, `PROJECTS`, and `SKILLS`.
- Add your profile image as `Streamlit/profile.jpg` to replace the placeholder.
- Add `Streamlit/resume.pdf` to enable the resume download button.

Deploy to Streamlit Community Cloud:

1. Push the repository to GitHub.
2. Go to https://share.streamlit.io → New app → choose the repo and branch.
3. Set the main file path to `Streamlit/main.py` and deploy.
