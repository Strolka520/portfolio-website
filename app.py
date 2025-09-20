import base64
import pathlib
import datetime
import urllib.parse
from typing import List, Dict

import streamlit as st

# --------------------
# Basic Page Settings
# --------------------
st.set_page_config(
    page_title="Steven Rolka — Portfolio",
    page_icon="📁",
    layout="wide",
)

# --------------------
# Helper Functions
# --------------------
ASSETS_DIR = pathlib.Path("assets")
RESUME_PATH = ASSETS_DIR / "resume.pdf"


def ensure_assets_folder() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)


def ensure_resume_present() -> None:
    """If the canonical resume.pdf is missing, but an uploaded Steven_Rolka_Resume.pdf exists, copy it into place."""
    fallback = ASSETS_DIR / "Steven_Rolka_Resume.pdf"
    if not RESUME_PATH.exists() and fallback.exists():
        # copy the fallback file to the expected path
        with fallback.open("rb") as src, RESUME_PATH.open("wb") as dst:
            dst.write(src.read())


def pdf_to_base64(path: pathlib.Path) -> str:
    with path.open("rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    return b64


def card(title: str, body: str, footer: str = "") -> None:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-body">{body}</div>
            <div class="card-footer">{footer}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def project_card(p: Dict[str, str]) -> None:
    repo_link = f"<a href='{p.get('repo_url','#')}' target='_blank'>Repo</a>" if p.get("repo_url") else ""
    demo_link = f"<a href='{p.get('demo_url','#')}' target='_blank'>Demo</a>" if p.get("demo_url") else ""
    links = " • ".join([x for x in [repo_link, demo_link] if x])

    tech = p.get("tech", "")
    footer = f"{tech}"
    if links:
        footer = f"{footer} — {links}" if footer else links

    card(p.get("title", "Untitled Project"), p.get("description", ""), footer)


# --------------------
# Style Overrides
# --------------------
st.markdown(
    """
    <style>
      .card {background: #ffffff; border: 1px solid rgba(0,0,0,0.07); padding: 1rem 1.25rem; border-radius: 14px; box-shadow: 0 1px 2px rgba(0,0,0,0.04);} 
      .card + .card { margin-top: 0.75rem; }
      .card-title { font-weight: 700; font-size: 1.05rem; margin-bottom: 0.25rem; }
      .card-body { opacity: 0.9; }
      .card-footer { margin-top: 0.5rem; font-size: 0.92rem; opacity: 0.8; }
      .tag { display:inline-block; padding: 0.15rem 0.5rem; border-radius: 999px; border: 1px solid rgba(0,0,0,0.1); font-size: 0.8rem; margin-right: 0.25rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------
# Content
# --------------------
PROFILE = {
    "name": "Steven Rolka",
    "role": "Senior BI / Data Engineer",
    "location": "Midwest, USA",
    "email": "rolka.steven@outlook.com",
    "linkedin": "https://www.linkedin.com/in/steven-rolka",
    "github": "https://github.com/Strolka520",
    "blurb": (
        "I design and build analytics platforms, dimensional models, and metadata-driven pipelines. "
        "This portfolio highlights selected projects and my experience in Microsoft Fabric, Spark, and Streamlit."
    ),
}

PROJECTS: List[Dict[str, str]] = [
    {
        "title": "Mortgage Rates Explorer",
        "description": "Interactive dashboards showing mortgage rate trends at national, regional, state, and local levels.",
        "tech": "Python, Streamlit, Pandas, Plotly",
        "repo_url": "",
        "demo_url": "",
    },
    {
        "title": "Housing Price Trends",
        "description": "Analysis of house price movements across geographies, with visualization of affordability indices.",
        "tech": "Python, Streamlit, SQL, Power BI",
        "repo_url": "",
        "demo_url": "",
    },
    {
        "title": "Big Company Data (Twitter, Amazon, GitHub)",
        "description": "Data ingestion and analysis pipelines using APIs from Twitter, Amazon, and GitHub to uncover trends.",
        "tech": "APIs, Python, Streamlit, Spark",
        "repo_url": "",
        "demo_url": "",
    },
    {
        "title": "Microsoft Fabric Insights (Medium Article)",
        "description": "Medium-style writeup and demo project based on prior Fabric presentation work, scrubbed for public sharing.",
        "tech": "Microsoft Fabric, Delta, PySpark",
        "repo_url": "",
        "demo_url": "",
    },
    {
        "title": "AI Chatbot Prototype",
        "description": "Exploratory chatbot built with Python and Streamlit, showcasing conversational AI integration.",
        "tech": "Python, Streamlit, OpenAI API",
        "repo_url": "",
        "demo_url": "",
    },
]

# --------------------
# Sidebar
# --------------------
with st.sidebar:
    profile_path = ASSETS_DIR / "profile.png"
    if profile_path.exists():
        try:
            import base64 as _base64

            _b = profile_path.read_bytes()
            _b64 = _base64.b64encode(_b).decode("utf-8")
            st.markdown(
                f"""
                <div style='display:flex; justify-content:center; align-items:center; padding:8px 0;'>
                  <img src='data:image/png;base64,{_b64}' alt='profile' style='width:123px;height:123px;object-fit:cover;border-radius:50%;border:1px solid rgba(0,0,0,0.08);'/>
                </div>
                """,
                unsafe_allow_html=True,
            )
        except Exception:
            pass

    section = st.radio("Go to", ["Home", "Resume", "Projects", "Contact"], index=0)
    st.write("\n")
    st.markdown("## Links")
    st.markdown(f"[LinkedIn]({PROFILE['linkedin']})")
    st.markdown(f"[GitHub]({PROFILE['github']})")

# --------------------
# Sections
# --------------------
if section == "Home":
    left, right = st.columns([2, 1])
    with left:
        st.title(PROFILE["name"])
        st.subheader(PROFILE["role"])
        st.write(PROFILE["blurb"])
        st.write("### Highlights")
        card("Enterprise Data Fabric", "Led design and implementation of a medallion architecture with metadata-driven pipelines, improving reliability and time-to-insight.")
        card("DataNexus Platform", "Built a Streamlit portal for BI engineering workflows (discovery, ingestion requests, and schema drift detection).")
    with right:
        st.write("### At a glance")
        st.markdown(f"<span class='tag'>Fabric</span><span class='tag'>Spark</span><span class='tag'>Delta</span><span class='tag'>Power BI</span>", unsafe_allow_html=True)
        st.write("### Contact")
        st.write(PROFILE["email"])
        st.write(PROFILE["location"])

elif section == "Resume":
    st.header("Resume")
    ensure_assets_folder()
    ensure_resume_present()
    if RESUME_PATH.exists():
        with RESUME_PATH.open("rb") as f:
            st.download_button(
                label="Download PDF",
                data=f,
                file_name="resume.pdf",
                mime="application/pdf",
            )
        b64_pdf = pdf_to_base64(RESUME_PATH)
        # pdf_iframe = f"""
    #         <iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="900px"></iframe>
    #     """
    #     st.components.v1.html(pdf_iframe, height=900, scrolling=True)
    # else:
    #     st.info("Place resume PDF at ./assets/resume.pdf to enable download and preview.")

    md_path = ASSETS_DIR / "Steven_Rolka_Resume.md"
    if md_path.exists():
        try:
            md_text = md_path.read_text(encoding="utf-8")
            st.markdown(md_text)
        except Exception:
            st.warning("Could not read the Markdown resume file.")

elif section == "Projects":
    st.header("Projects")
    for p in PROJECTS:
        project_card(p)

elif section == "Contact":
    st.header("Contact")
    st.caption("Use the form or email me directly.")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message", height=160)
        submitted = st.form_submit_button("Generate Email Draft")
    if submitted:
        subject = urllib.parse.quote(f"Portfolio Inquiry — {name}")
        body_lines = [f"From: {name}", f"Email: {email}", "", message]
        body = urllib.parse.quote("\n".join(body_lines))
        mailto = f"mailto:{PROFILE['email']}?subject={subject}&body={body}"
        st.success("Draft created. Click below to open your email client.")
        st.markdown(f"[Open Email Draft]({mailto})")

# --------------------
# Footer
# --------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("© " + str(datetime.datetime.now().year) + " Steven Rolka. Built with Python.")
