# Portfolio Website Project
# Portfolio Website — Steven Rolka

This repository contains a personal portfolio and resume site built with Streamlit.

## What it contains
- `app.py` — Streamlit app displaying profile, resume (PDF + Markdown), projects, and contact form.
- `assets/` — static assets including `Steven_Rolka_Resume.pdf` and `Steven_Rolka_Resume.md`.

## Run locally

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

3. Open the URL shown in the terminal (usually http://localhost:8501).

## Deploy to Streamlit Community Cloud

1. Push this repo to GitHub (already done).
2. Go to https://streamlit.io/cloud and create a new app from your GitHub repository.
3. Set the main file to `app.py`. Streamlit Cloud will install `requirements.txt` automatically.

## Notes

- `assets/Steven_Rolka_Resume.pdf` and `assets/Steven_Rolka_Resume.md` are included. `assets/resume.pdf` is the canonical path the app uses; if `assets/resume.pdf` is missing the app will copy `Steven_Rolka_Resume.pdf` into place at runtime.
- If you prefer not to commit the PDF, add `assets/resume.pdf` to `.gitignore` and keep only the Markdown resume committed.
- If Chrome blocks the embedded PDF preview, use the Download button or the text view (expander) provided in the Resume section.

## Next steps and suggestions

- Personalize the `PROFILE` section in `app.py` (name, email, LinkedIn/GitHub already set to Steven Rolka and your GitHub account).
- Add project `repo_url` and `demo_url` values in `app.py` for each project card.
- Optionally add a small smoke test to ensure the app imports successfully.

---
