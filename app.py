import os
from datetime import datetime

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# PROFILE CONFIGURATION
# ---------------------------------------------------------------------------
NAME = "Colyn Pacaldo"
SECTION = "CS365 - Section F1"
PROGRAM = "BS Computer Science"
YEAR = "3rd Year"
TAGLINE = "Computer science student building practical web applications, mobile tools, and exploring algorithmic problem solving."
GITHUB_URL = "https://github.com/colynpacaldo"
LEETCODE_URL = "https://leetcode.com/u/ColynS/"

st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# DATA & REPOSITORIES
# ---------------------------------------------------------------------------
@st.cache_data
def load_skills() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Skill": ["Python", "Django", "JavaScript", "Android (Java/Kotlin)", "HTML/CSS", "SQL", "Git", "Data Structures"],
            "Category": ["Backend", "Backend", "Frontend", "Mobile", "Frontend", "Database", "Tools", "Computer Science"],
            "Level (1-10)": [9, 8, 8, 7, 8, 7, 8, 8],
            "Years": [3, 2, 2, 2, 3, 2, 3, 2],
        }
    )

skills = load_skills()

PROJECTS = {
    "pixelshelf": {
        "title": "PixelShelf",
        "role": "Creator & Full-Stack Developer",
        "tools": ["Python", "Django", "JavaScript", "HTML5 Canvas", "SQLite", "Supabase"],
        "outcome": "A 2D game asset catalog and web-based sprite previewer organized via Django vertical slicing. Features an in-browser sprite animator with frame-stepping, automatic grid detection, and canvas contrast testing.",
        "link": "https://github.com/colynpacaldo/PixelShelf",
    },
    "pathfinder": {
        "title": "PathFinder-Access",
        "role": "Android Developer",
        "tools": ["Android SDK", "Java / Kotlin", "Gradle", "XML"],
        "outcome": "A crowdsourced Android application designed to help individuals with mobility challenges navigate communities safely by reporting, upvoting, and filtering real-time accessibility barriers.",
        "link": "https://github.com/colynpacaldo/PathFinder-Access",
    },
    "flowstate": {
        "title": "FlowState",
        "role": "Developer",
        "tools": ["JavaScript", "HTML5", "CSS3", "Git"],
        "outcome": "A minimalist workflow and focus session utility designed to reduce digital clutter and facilitate uninterrupted deep work blocks.",
        "link": "https://github.com/colynpacaldo/FlowState",
    },
}

if "messages" not in st.session_state:
    st.session_state.messages = []
if "likes" not in st.session_state:
    st.session_state.likes = {key: 0 for key in PROJECTS}

# ---------------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------------
with st.sidebar:
    if os.path.exists("photo.jpg"):
        st.image("photo.jpg", caption=NAME, use_container_width=True)
    else:
        st.markdown(
            f"""
            <div class="sidebar-avatar-placeholder">
                <div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 0.25rem;">{NAME}</div>
                <div style="font-size: 0.85rem; opacity: 0.8;">{PROGRAM}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class="sidebar-meta-block">
            <div class="sidebar-name-darkened">{NAME}</div>
            <div class="sidebar-sub-darkened">{PROGRAM} • {YEAR}</div>
            <div class="sidebar-sub-darkened">{SECTION}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### Profiles")
    st.link_button("GitHub", GITHUB_URL, use_container_width=True)
    st.link_button("LeetCode", LEETCODE_URL, use_container_width=True)

    st.markdown("---")
    st.markdown("### Preferences")
    show_fun = st.checkbox("Show fun facts", value=True)

    st.markdown("---")
    st.markdown("### Export")
    bio_txt = (
        f"{NAME}\n{PROGRAM}, {YEAR}\n{SECTION}\n"
        f"GitHub: {GITHUB_URL}\nLeetCode: {LEETCODE_URL}\n\n"
        f"Bio: {TAGLINE}\n"
    )
    st.download_button(
        "Download Bio (.txt)",
        bio_txt,
        file_name="colyn_pacaldo_bio.txt",
        use_container_width=True,
    )
    st.download_button(
        "Download Skills (.csv)",
        skills.to_csv(index=False),
        file_name="colyn_pacaldo_skills.csv",
        mime="text/csv",
        use_container_width=True,
    )

# ---------------------------------------------------------------------------
# PERMANENT DARK THEME TOKENS & STYLES
# ---------------------------------------------------------------------------
ACCENT = "#E05A38"
BG_COLOR = "#0D1117"
SIDEBAR_BG = "#161B22"
SURFACE = "#1E2430"
SURFACE_HOVER = "#273040"
TEXT_MAIN = "#F0F6FC"
TEXT_MUTED = "#9DA7B3"
BORDER_COLOR = "#30363D"
PILL_BG = "#21262D"
INPUT_BG = "#161B22"
SHADOW = "0 8px 24px rgba(0, 0, 0, 0.45)"
ACTIVE_TAB_SHADOW = "0 4px 14px rgba(224, 90, 56, 0.4)"
NAME_COLOR = "#FFFFFF"
SUB_COLOR = "#D1D5DB"

def themed(chart):
    return (
        chart.configure(
            background="transparent",
            autosize=alt.AutoSizeParams(type="fit", contains="padding"),
        )
        .configure_view(stroke=None)
        .configure_axis(
            labelColor=TEXT_MUTED,
            titleColor=TEXT_MUTED,
            gridColor=BORDER_COLOR,
            domainColor=BORDER_COLOR,
            tickColor=BORDER_COLOR,
        )
        .configure_legend(labelColor=TEXT_MAIN, titleColor=TEXT_MAIN)
    )

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap');

:root {{
  --accent: {ACCENT};
  --bg-color: {BG_COLOR};
  --sidebar-bg: {SIDEBAR_BG};
  --surface: {SURFACE};
  --surface-hover: {SURFACE_HOVER};
  --text-main: {TEXT_MAIN};
  --text-muted: {TEXT_MUTED};
  --border: {BORDER_COLOR};
  --pill-bg: {PILL_BG};
  --input-bg: {INPUT_BG};
  --shadow: {SHADOW};
  --active-tab-shadow: {ACTIVE_TAB_SHADOW};
  --name-color: {NAME_COLOR};
  --sub-color: {SUB_COLOR};
  --radius: 12px;
}}

/* ELIMINATE TOP HEADER & WHITE BAR */
header[data-testid="stHeader"],
header[data-testid="stHeader"] > div,
.stApp > header,
[data-testid="stHeader"] {{
  background-color: var(--bg-color) !important;
  background: var(--bg-color) !important;
  border-bottom: 1px solid var(--border) !important;
}}

[data-testid="stDecoration"] {{
  display: none !important;
}}

/* GLOBAL APP BASE */
.stApp {{
  background-color: var(--bg-color) !important;
  color: var(--text-main) !important;
  font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
}}

.block-container {{
  max-width: 1080px;
  padding: 2.2rem 2rem 4rem;
}}

h1, h2, h3, h4, .brand-font {{
  font-family: 'Fraunces', Georgia, serif !important;
  color: var(--text-main) !important;
  letter-spacing: -0.015em;
}}

p, span, label, div {{
  color: var(--text-main);
}}

/* SIDEBAR */
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div,
section[data-testid="stSidebar"] div[data-testid="stSidebarContent"],
section[data-testid="stSidebar"] div[data-testid="stSidebarUserContent"],
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div {{
  background-color: var(--sidebar-bg) !important;
  background: var(--sidebar-bg) !important;
  border-right: none !important;
  box-shadow: none !important;
}}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h4,
[data-testid="stSidebar"] .stMarkdown {{
  color: var(--text-main) !important;
}}

[data-testid="stSidebar"] .stCaption,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
  color: var(--text-muted) !important;
}}

[data-testid="stSidebar"] hr {{
  border-color: var(--border) !important;
}}

.sidebar-meta-block {{
  margin: 0.6rem 0 1rem;
}}
.sidebar-name-darkened {{
  font-family: 'Fraunces', Georgia, serif;
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--name-color) !important;
  line-height: 1.25;
  margin-bottom: 0.25rem;
}}
.sidebar-sub-darkened {{
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--sub-color) !important;
  line-height: 1.45;
}}

.sidebar-avatar-placeholder {{
  text-align: center;
  padding: 1.5rem 1rem;
  border-radius: var(--radius);
  border: 1px dashed var(--border);
  background: var(--surface);
  margin-bottom: 1rem;
}}

/* HERO SECTION */
@keyframes riseUp {{
  from {{
    opacity: 0;
    transform: translateY(10px);
  }}
  to {{
    opacity: 1;
    transform: translateY(0);
  }}
}}

.hero {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 5px solid var(--accent);
  border-radius: var(--radius);
  padding: 2rem 2.2rem;
  margin-bottom: 1.75rem;
  box-shadow: var(--shadow);
  animation: riseUp 0.4s ease-out both;
}}
.eyebrow {{
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 0.4rem;
}}
.hero h1 {{
  font-size: clamp(2.2rem, 5vw, 3rem);
  line-height: 1.15;
  margin: 0 0 0.65rem;
}}
.hero .tagline {{
  color: var(--text-muted);
  font-size: 1.05rem;
  line-height: 1.5;
  max-width: 44rem;
  margin-bottom: 1.25rem;
}}

/* PILL BADGES */
.pill {{
  display: inline-block;
  padding: 0.3rem 0.8rem;
  margin: 0 0.4rem 0.4rem 0;
  border: 1px solid var(--border);
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-main);
  background: var(--pill-bg);
  transition: border-color 0.2s ease, transform 0.2s ease;
}}
.pill:hover {{
  border-color: var(--accent);
  transform: translateY(-1px);
}}
.pill.accent {{
  border-color: var(--accent);
  color: #FFFFFF;
  background: var(--accent);
}}

/* TABS */
.stTabs [data-baseweb="tab-list"] {{
  display: flex;
  gap: 0.6rem;
  padding: 0.5rem;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}}

.stTabs [data-baseweb="tab"] {{
  flex: 1 1 auto;
  text-align: center;
  padding: 0.7rem 1.2rem !important;
  border-radius: 8px !important;
  font-weight: 600 !important;
  font-size: 0.92rem !important;
  color: var(--text-muted) !important;
  background: transparent !important;
  border: 1px solid transparent !important;
  cursor: pointer;
  transition: all 0.22s ease-in-out !important;
}}

.stTabs [data-baseweb="tab"]:hover {{
  color: var(--text-main) !important;
  background: var(--surface-hover) !important;
  border-color: var(--border) !important;
  transform: translateY(-2px);
}}

.stTabs [data-baseweb="tab"][aria-selected="true"] {{
  color: #FFFFFF !important;
  background: var(--accent) !important;
  border-color: var(--accent) !important;
  box-shadow: var(--active-tab-shadow) !important;
  transform: translateY(-2px);
}}

.stTabs [data-baseweb="tab-highlight"] {{
  display: none !important;
}}

[data-baseweb="tab-panel"] {{
  padding-top: 1.5rem;
  animation: riseUp 0.35s ease-out both;
}}

/* STATS METRICS */
[data-testid="stMetric"] {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1rem 1.25rem;
  box-shadow: var(--shadow);
  transition: transform 0.2s ease;
}}
[data-testid="stMetric"]:hover {{
  transform: translateY(-2px);
  border-color: var(--accent);
}}
[data-testid="stMetricLabel"] {{
  color: var(--text-muted) !important;
  font-size: 0.8rem;
  font-weight: 600;
}}
[data-testid="stMetricValue"] {{
  font-family: 'Fraunces', Georgia, serif !important;
  font-size: 1.8rem !important;
  color: var(--text-main) !important;
}}

/* BUTTONS */
.stButton > button,
.stDownloadButton > button,
.stLinkButton > a,
[data-testid="stFormSubmitButton"] > button {{
  background: var(--surface) !important;
  color: var(--text-main) !important;
  border: 1px solid var(--border) !important;
  border-radius: 9px !important;
  font-weight: 600 !important;
  font-size: 0.9rem !important;
  padding: 0.5rem 1rem !important;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
  transition: all 0.2s ease !important;
}}

.stButton > button:hover,
.stDownloadButton > button:hover,
.stLinkButton > a:hover,
[data-testid="stFormSubmitButton"] > button:hover {{
  border-color: var(--accent) !important;
  color: var(--accent) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
}}

/* INPUTS */
div[data-testid="stTextArea"] div[data-baseweb="textarea"],
div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] div[data-baseweb="base-input"],
div[data-testid="stTextInput"] div[data-baseweb="input"],
div[data-testid="stTextInput"] input,
textarea {{
  background-color: var(--input-bg) !important;
  background: var(--input-bg) !important;
  color: var(--text-main) !important;
  -webkit-text-fill-color: var(--text-main) !important;
  border: 1px solid var(--border) !important;
  border-radius: 9px !important;
}}

div[data-testid="stSelectbox"] div[data-baseweb="select"],
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
div[data-testid="stMultiSelect"] div[data-baseweb="select"],
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {{
  background-color: var(--input-bg) !important;
  background: var(--input-bg) !important;
  border: 1px solid var(--border) !important;
  border-radius: 9px !important;
  color: var(--text-main) !important;
}}

div[data-baseweb="popover"],
div[data-baseweb="popover"] *:not(svg):not(path) {{
  background-color: var(--surface) !important;
  color: var(--text-main) !important;
  -webkit-text-fill-color: var(--text-main) !important;
}}

/* EXPANDER */
details[data-testid="stExpander"],
[data-testid="stExpander"] {{
  background-color: var(--surface) !important;
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  overflow: hidden !important;
}}

/* CONTACT FORM CONTAINER */
div[data-testid="stForm"],
.stForm {{
  background-color: var(--surface) !important;
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  padding: 1.5rem !important;
  box-shadow: var(--shadow) !important;
}}

/* TABLES */
div[data-testid="stTable"],
div[data-testid="stTable"] > div,
div[data-testid="stTable"] table {{
  background-color: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  color: var(--text-main) !important;
  overflow: hidden !important;
}}

div[data-testid="stTable"] th {{
  background-color: var(--pill-bg) !important;
  color: var(--text-main) !important;
  border-bottom: 1px solid var(--border) !important;
  font-weight: 700 !important;
}}

/* CHART OVERFLOW FIX */
[data-testid="stVegaLiteChart"] {{
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  padding: 1rem 1rem 0.5rem !important;
  box-sizing: border-box !important;
  overflow: hidden !important;
  box-shadow: var(--shadow);
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
}}

[data-testid="stVegaLiteChart"] > div {{
  max-width: 100% !important;
  overflow: hidden !important;
}}

[data-testid="stVegaLiteChart"] svg {{
  background: transparent !important;
  display: block !important;
  max-width: 100% !important;
}}

[data-testid="stVegaLiteChart"] text {{
  fill: var(--text-muted) !important;
  font-family: 'Plus Jakarta Sans', system-ui, sans-serif !important;
}}

[data-testid="stVegaLiteChart"] .role-axis path.domain,
[data-testid="stVegaLiteChart"] .role-axis-tick line {{
  stroke: var(--border) !important;
}}

[data-testid="stVegaLiteChart"] .role-axis-grid line {{
  stroke: var(--border) !important;
  stroke-opacity: 0.5 !important;
}}

/* PROJECT CARDS */
[class*="st-key-card_"] {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.35rem;
  box-shadow: var(--shadow);
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}}

[class*="st-key-card_"]:hover {{
  transform: translateY(-3px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.12);
  border-color: var(--accent);
}}

.card-title {{
  font-family: 'Fraunces', Georgia, serif;
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
  color: var(--text-main);
}}
.card-role {{
  color: var(--accent);
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 0.65rem;
}}
.card-body {{
  color: var(--text-muted);
  font-size: 0.9rem;
  line-height: 1.5;
  margin: 0.75rem 0 1.2rem;
}}

.section-title {{
  font-family: 'Fraunces', Georgia, serif;
  font-size: 1.65rem;
  font-weight: 700;
  color: var(--text-main);
  margin: 1.5rem 0 0.25rem;
}}
.section-sub {{
  color: var(--text-muted);
  font-size: 0.92rem;
  margin-bottom: 1.25rem;
}}

.footer {{
  color: var(--text-muted);
  font-size: 0.85rem;
  text-align: center;
  padding: 2rem 0 1rem;
}}
</style>
""",
    unsafe_allow_html=True,
)

def section(title: str, sub: str = ""):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if sub:
        st.markdown(f'<div class="section-sub">{sub}</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
st.markdown(
    f"""
<div class="hero">
  <div class="eyebrow">Portfolio</div>
  <h1>{NAME}</h1>
  <div class="tagline">{TAGLINE}</div>
  <div>
    <span class="pill accent">{PROGRAM}</span>
    <span class="pill">{YEAR}</span>
    <span class="pill">{SECTION}</span>
    <span class="pill">Cebu City, Philippines</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# STATS METRICS
# ---------------------------------------------------------------------------
m1, m2, m3, m4 = st.columns(4)
m1.metric("Featured Projects", len(PROJECTS))
m2.metric("Tracked Skills", len(skills))
m3.metric("Coding Experience", f"{int(skills['Years'].max())} Years")
m4.metric("Avg. Rating", f"{skills['Level (1-10)'].mean():.1f} / 10")

st.write("")

# ---------------------------------------------------------------------------
# TABS
# ---------------------------------------------------------------------------
tab_about, tab_auto, tab_skills, tab_projects, tab_contact = st.tabs(
    ["About", "Autobiography", "Skills", "Projects", "Contact"]
)

# ---------------------------------------------------------------------------
# TAB 1: ABOUT
# ---------------------------------------------------------------------------
with tab_about:
    left, right = st.columns([1, 2], gap="large")
    with left:
        if os.path.exists("photo.jpg"):
            st.image("photo.jpg", caption=NAME, use_container_width=True)
        else:
            st.markdown(
                f"""
                <div style="aspect-ratio: 4/5; border-radius: var(--radius); display: flex; 
                     flex-direction: column; align-items: center; justify-content: center;
                     background: {SURFACE}; border: 1px solid {BORDER_COLOR};">
                    <div style="font-weight: 700; font-size: 1.1rem; color: {TEXT_MAIN};">{NAME}</div>
                    <div style="font-size: 0.85rem; color: {TEXT_MUTED};">Software Developer</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    with right:
        section("About Me", "Academic foundation and development focus")
        st.write(
            f"I am a third-year Computer Science student focused on developing robust full-stack applications "
            f"and mobile software. I value clean code structure, vertical slice architecture, and practical "
            f"solutions for developer tooling and community accessibility."
        )
        st.markdown(
            f"""
- **Program & Year:** {PROGRAM}, {YEAR}
- **Section:** {SECTION}
- **Location:** Cebu City, Philippines
- **Core Stacks:** Django, Python, JavaScript, Android (Java/Kotlin), Streamlit
- **Code Repositories:** [GitHub]({GITHUB_URL}) • [LeetCode]({LEETCODE_URL})
"""
        )
        if show_fun:
            with st.expander("Fun Facts"):
                st.write("- Enjoys dissecting 2D game asset architectures and sprite animations.")
                st.write("- Actively practices competitive programming and algorithmic puzzles.")
                st.write("- Works best with a clean terminal and structured documentation.")

# ---------------------------------------------------------------------------
# TAB 2: AUTOBIOGRAPHY
# ---------------------------------------------------------------------------
with tab_auto:
    col_bio, col_interests = st.columns(2, gap="large")
    with col_bio:
        section("Background", "Academic and programming journey")
        st.write(
            "My path in computer science started with building simple automation scripts and exploring "
            "how software can streamline real-world tasks. Over the years, this evolved into structured "
            "software development encompassing web platforms, mobile utilities, and algorithmic design."
        )
        section("Education")
        st.table(
            pd.DataFrame(
                {
                    "Level": ["Primary", "Junior & Senior High", "College"],
                    "Institution": ["Basic Education", "Science & Technology Track", "BS Computer Science"],
                    "Period": ["2011 - 2017", "2017 - 2023", "2023 - Present"],
                }
            )
        )
    with col_interests:
        section("Interests", "Fields and activities I pursue")
        interests = st.multiselect(
            "Interests",
            [
                "Full-Stack Web Development",
                "Mobile Development",
                "Algorithms & Problem Solving",
                "Game Tooling & Asset Pipelines",
                "UI/UX Accessibility",
            ],
            default=["Full-Stack Web Development", "Algorithms & Problem Solving", "Game Tooling & Asset Pipelines"],
            label_visibility="collapsed",
        )
        if interests:
            st.markdown("".join(f'<span class="pill">{item}</span>' for item in interests), unsafe_allow_html=True)

        section("Key Milestones")
        milestones = pd.DataFrame(
            {
                "Year": [2021, 2023, 2024, 2025],
                "Milestone": [
                    "Began programming with Python and basic web concepts",
                    "Enrolled in BS Computer Science program",
                    "Engineered Android accessibility tools and full-stack projects",
                    "Developed PixelShelf vertical slicing architecture and advanced pipelines",
                ],
            }
        )
        max_year = st.slider("Filter milestones up to year:", 2021, 2025, 2025)
        st.table(milestones[milestones["Year"] <= max_year])

# ---------------------------------------------------------------------------
# TAB 3: SKILLS
# ---------------------------------------------------------------------------
with tab_skills:
    section("Skills & Technologies", "Self-assessed competency and years of experience")
    f_col1, f_col2 = st.columns([1, 2], gap="large")
    with f_col1:
        cat_filter = st.multiselect(
            "Filter Category",
            sorted(skills["Category"].unique()),
            default=list(skills["Category"].unique()),
        )
        min_lvl = st.slider("Minimum Competency (1-10)", 1, 10, 5)
        sort_choice = st.selectbox("Sort Skills By", ["Level (1-10)", "Years", "Skill"])

    filtered_skills = skills[
        skills["Category"].isin(cat_filter) & (skills["Level (1-10)"] >= min_lvl)
    ].sort_values(sort_choice, ascending=(sort_choice == "Skill"))

    with f_col2:
        if filtered_skills.empty:
            st.warning("No skills match the current filter selection.")
        else:
            st.table(filtered_skills)

    if not filtered_skills.empty:
        c_chart, c_progress = st.columns(2, gap="large")
        with c_chart:
            st.markdown("#### Competency Breakdown")
            bar_df = filtered_skills.rename(columns={"Level (1-10)": "Level"})
            bar = (
                alt.Chart(bar_df)
                .mark_bar(
                    color=ACCENT,
                    cornerRadiusTopLeft=4,
                    cornerRadiusTopRight=4,
                )
                .encode(
                    x=alt.X(
                        "Skill:N",
                        sort=None,
                        title=None,
                        scale=alt.Scale(paddingInner=0.25, paddingOuter=0.15),
                        axis=alt.Axis(
                            labelAngle=-30,
                            labelLimit=120,
                            labelPadding=6,
                        ),
                    ),
                    y=alt.Y("Level:Q", scale=alt.Scale(domain=[0, 10]), title="Level"),
                    tooltip=["Skill", "Category", "Level", "Years"],
                )
                .properties(height=300)
            )
            st.altair_chart(themed(bar), use_container_width=True, theme=None)
        with c_progress:
            st.markdown("#### Primary Strengths")
            for _, row in filtered_skills.head(4).iterrows():
                st.write(f"**{row['Skill']}** ({row['Category']})")
                st.progress(int(row["Level (1-10)"]) * 10)

    section("Growth Trajectory", "Skill progression over the current academic year")
    months = pd.date_range("2024-01-01", periods=12, freq="MS")
    progress_data = pd.DataFrame(
        {
            "Full-Stack Development": np.linspace(2, 8.5, 12),
            "Algorithmic Problem Solving": np.linspace(1, 8.0, 12),
        },
        index=months,
    )
    line_df = progress_data.reset_index().melt("index", var_name="Track", value_name="Level")
    line = (
        alt.Chart(line_df)
        .mark_line(strokeWidth=3)
        .encode(
            x=alt.X("index:T", title=None, axis=alt.Axis(format="%b")),
            y=alt.Y("Level:Q", scale=alt.Scale(domain=[0, 10])),
            color=alt.Color("Track:N", scale=alt.Scale(range=[ACCENT, "#3B82F6"]), title=None),
            tooltip=["Track", "Level"],
        )
        .properties(height=300)
    )
    st.altair_chart(themed(line), use_container_width=True, theme=None)

# ---------------------------------------------------------------------------
# TAB 4: PROJECTS
# ---------------------------------------------------------------------------
with tab_projects:
    section("Featured Projects", "Open-source work, tools, and applications")
    search_tool = st.text_input("Filter by technology or keyword:", placeholder="e.g. Django, Android, Canvas...")

    active_projects = {
        k: p for k, p in PROJECTS.items()
        if not search_tool
        or any(search_tool.lower() in t.lower() for t in p["tools"])
        or search_tool.lower() in p["title"].lower()
    }

    if not active_projects:
        st.info("No projects match your filter.")
    else:
        p_cols = st.columns(3, gap="medium")
        for idx, (p_id, p_info) in enumerate(active_projects.items()):
            target_col = p_cols[idx % 3]
            with target_col:
                with st.container(key=f"card_{p_id}"):
                    tool_pills = "".join(f'<span class="pill">{tool}</span>' for tool in p_info["tools"])
                    st.markdown(
                        f"""
                        <div class="card-title">{p_info['title']}</div>
                        <div class="card-role">{p_info['role']}</div>
                        <div style="margin: 0.4rem 0;">{tool_pills}</div>
                        <div class="card-body">{p_info['outcome']}</div>
                        """,
                        unsafe_allow_html=True,
                    )
                    b_col1, b_col2 = st.columns(2)
                    with b_col1:
                        st.link_button("View Repository", p_info["link"], use_container_width=True)
                    with b_col2:
                        if st.button(f"Like ({st.session_state.likes[p_id]})", key=f"btn_like_{p_id}", use_container_width=True):
                            st.session_state.likes[p_id] += 1
                            st.rerun()

# ---------------------------------------------------------------------------
# TAB 5: CONTACT
# ---------------------------------------------------------------------------
with tab_contact:
    section("Contact", "Send a message or reach out for collaboration")
    form_left, info_right = st.columns([2, 1], gap="large")

    with form_left:
        with st.form("contact_form", clear_on_submit=True):
            user_name = st.text_input("Name", placeholder="Your name")
            user_email = st.text_input("Email", placeholder="your.email@example.com")
            inquiry_topic = st.selectbox(
                "Topic",
                [
                    "Project Collaboration",
                    "Technical Discussion",
                    "General Inquiry",
                ],
            )
            site_rating = st.slider("Portfolio evaluation", 1, 5, 5)
            user_msg = st.text_area("Message", placeholder="Write your message here...", height=120)
            consent = st.checkbox("I agree to be contacted back at the email provided.")
            send_btn = st.form_submit_button("Send Message")

        if send_btn:
            if not user_name.strip() or not user_msg.strip() or not user_email.strip():
                st.error("Please fill in your name, email, and message.")
            else:
                st.session_state.messages.append(
                    {
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "Name": user_name,
                        "Email": user_email,
                        "Topic": inquiry_topic,
                        "Rating": f"{site_rating} / 5",
                    }
                )
                st.success(f"Thank you, {user_name}. Your message has been sent.")

    with info_right:
        st.markdown(
            f"""
### Details

- **GitHub:** [colynpacaldo]({GITHUB_URL})
- **LeetCode:** [ColynS]({LEETCODE_URL})
- **Location:** Cebu City, Philippines
- **Status:** Open to internships and development collaborations
"""
        )
        if st.session_state.messages:
            st.markdown("---")
            st.caption("Submitted Messages (Session)")
            st.table(pd.DataFrame(st.session_state.messages))

# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    f"""
    <div class="footer">
      © {datetime.now().year} {NAME} • {SECTION} • Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)