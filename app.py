import streamlit as st
import pandas as pd

from resume_parser import extract_pdf
from text_cleaner import clean_text

from skill_extractor import (
    load_skill_dictionary,
    extract_skills
)

from job_matcher import match_jobs

from skill_gap_analyzer import (
    load_job_roles,
    get_required_skills,
    find_missing_skills
)

from roadmap_generator import generate_roadmap


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("📄 AI Resume Analyzer & Job Recommendation System")

st.write(
    "Upload your resume to extract skills, recommend suitable "
    "job roles, identify skill gaps, and generate a learning roadmap."
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Project Modules")

st.sidebar.write("✅ Resume Parsing")
st.sidebar.write("✅ Text Cleaning")
st.sidebar.write("✅ Skill Extraction")
st.sidebar.write("✅ Job Matching")
st.sidebar.write("✅ Skill Gap Analysis")
st.sidebar.write("✅ Learning Roadmap")


# =========================================================
# RESUME UPLOAD
# =========================================================

st.header("1️⃣ Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your engineering resume",
    type=["pdf"]
)


# =========================================================
# MAIN APPLICATION
# =========================================================

if uploaded_file is not None:

    # -----------------------------------------------------
    # SAVE UPLOADED FILE
    # -----------------------------------------------------

    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully! ✅")


    # -----------------------------------------------------
    # RESUME PARSING
    # -----------------------------------------------------

    try:

        resume_text = extract_pdf(
            "uploaded_resume.pdf"
        )

    except Exception as e:

        st.error(
            f"Error while reading the resume: {e}"
        )

        st.stop()


    if not resume_text.strip():

        st.error(
            "No text could be extracted from this PDF. "
            "Please upload a text-based PDF."
        )

        st.stop()


    # -----------------------------------------------------
    # TEXT CLEANING
    # -----------------------------------------------------

    cleaned_text = clean_text(
        resume_text
    )


    # -----------------------------------------------------
    # SKILL EXTRACTION
    # -----------------------------------------------------

    try:

        skill_dictionary = load_skill_dictionary(
            "data/skill_dictionary.csv"
        )

        resume_skills = extract_skills(
            cleaned_text,
            skill_dictionary
        )

    except Exception as e:

        st.error(
            f"Error while extracting skills: {e}"
        )

        st.stop()


    # =====================================================
    # EXTRACTED RESUME INFORMATION
    # =====================================================

    st.header("2️⃣ Extracted Resume Information")

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("📋 Resume Text")

        with st.expander("View Extracted Resume Text"):

            st.write(resume_text)


    with col2:

        st.subheader("🛠️ Skills Detected")

        if resume_skills:

            for skill in resume_skills:

                st.write(f"• {skill}")

        else:

            st.warning(
                "No skills detected. "
                "Check your skill_dictionary.csv."
            )


    # =====================================================
    # JOB MATCHING
    # =====================================================

    st.header("3️⃣ Job Recommendations")

    try:

        job_results = match_jobs(
            cleaned_text,
            "data/job_roles.csv"
        )

    except Exception as e:

        st.error(
            f"Error while matching jobs: {e}"
        )

        st.stop()


    # -----------------------------------------------------
    # TOP 5 JOBS
    # -----------------------------------------------------

    top_jobs = job_results.head(5).copy()


    # -----------------------------------------------------
    # MATCH SCORE COLUMN
    # -----------------------------------------------------

    if "Match Score" in top_jobs.columns:

        top_jobs["Match Score"] = (
            top_jobs["Match Score"].round(2)
        )


    # -----------------------------------------------------
    # DISPLAY JOB TABLE
    # -----------------------------------------------------

    st.subheader("🎯 Recommended Job Roles")

    st.dataframe(
        top_jobs[
            ["Role", "Match Score"]
        ],
        use_container_width=True
    )


    # =====================================================
    # JOB MATCHING CHART
    # =====================================================

    st.subheader("📊 Job Match Scores")

    chart_data = top_jobs[
        ["Role", "Match Score"]
    ].copy()

    chart_data = chart_data.set_index(
        "Role"
    )

    st.bar_chart(
        chart_data
    )


    # =====================================================
    # BEST JOB ROLE
    # =====================================================

    best_role = top_jobs.iloc[0]["Role"]

    best_score = top_jobs.iloc[0]["Match Score"]


    st.success(
        f"🎯 Best Recommended Role: **{best_role}** "
        f"with a match score of **{best_score}%**"
    )


    # =====================================================
    # SKILL GAP ANALYSIS
    # =====================================================

    st.header("4️⃣ Skill Gap Analysis")


    try:

        job_roles = load_job_roles(
            "data/job_roles.csv"
        )

    except Exception as e:

        st.error(
            f"Error loading job roles: {e}"
        )

        st.stop()


    # -----------------------------------------------------
    # ROLE SELECTION
    # -----------------------------------------------------

    role_list = job_roles["Role"].tolist()


    if best_role in role_list:

        default_index = role_list.index(
            best_role
        )

    else:

        default_index = 0


    selected_role = st.selectbox(
        "Select a job role:",
        role_list,
        index=default_index
    )


    # -----------------------------------------------------
    # REQUIRED SKILLS
    # -----------------------------------------------------

    required_skills = get_required_skills(
        job_roles,
        selected_role
    )


    # -----------------------------------------------------
    # MISSING SKILLS
    # -----------------------------------------------------

    missing_skills = find_missing_skills(
        resume_skills,
        required_skills
    )


    # =====================================================
    # SKILL COVERAGE
    # =====================================================

    if len(required_skills) > 0:

        skill_coverage = (
            (
                len(required_skills)
                - len(missing_skills)
            )
            / len(required_skills)
        ) * 100

    else:

        skill_coverage = 0


    # =====================================================
    # REQUIRED VS MISSING SKILLS
    # =====================================================

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("✅ Required Skills")

        if required_skills:

            for skill in required_skills:

                st.write(f"• {skill}")

        else:

            st.warning(
                "No required skills found for this role."
            )


    with col2:

        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:

                st.write(f"• {skill}")

        else:

            st.success(
                "You have all the required skills! 🎉"
            )


    # =====================================================
    # SKILL COVERAGE METRIC
    # =====================================================

    st.metric(
        "📈 Skill Coverage",
        f"{skill_coverage:.1f}%"
    )


    # =====================================================
    # SKILL GAP CHART
    # =====================================================

    st.subheader("📊 Skill Gap Overview")


    skill_summary = pd.DataFrame(
        {
            "Category": [
                "Skills You Have",
                "Missing Skills"
            ],
            "Count": [
                len(resume_skills),
                len(missing_skills)
            ]
        }
    )


    st.bar_chart(
        skill_summary.set_index(
            "Category"
        )
    )


    # =====================================================
    # LEARNING ROADMAP
    # =====================================================

    st.header("5️⃣ Personalized Learning Roadmap")


    roadmap = generate_roadmap(
        missing_skills
    )


    if "Result" in roadmap:

        st.success(
            roadmap["Result"]
        )

    else:

        for week, skills in roadmap.items():

            with st.expander(
                f"📚 Week {week}"
            ):

                for skill in skills:

                    st.write(
                        f"• Learn **{skill}**"
                    )


    # =====================================================
    # SUMMARY
    # =====================================================

    st.header("6️⃣ Resume Analysis Summary")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Skills Detected",
            len(resume_skills)
        )


    with col2:

        st.metric(
            "Best Match",
            f"{best_score}%"
        )


    with col3:

        st.metric(
            "Skill Gaps",
            len(missing_skills)
        )


    with col4:

        st.metric(
            "Skill Coverage",
            f"{skill_coverage:.1f}%"
        )


    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    st.header("7️⃣ Download Analysis")


    analysis_text = f"""
AI RESUME ANALYZER
==================

Recommended Job Role:
{best_role}

Match Score:
{best_score}%

Skills Detected:
{", ".join(resume_skills)}

Required Skills:
{", ".join(required_skills)}

Missing Skills:
{", ".join(missing_skills)}

Skill Coverage:
{skill_coverage:.1f}%

LEARNING ROADMAP
================
"""


    if "Result" in roadmap:

        analysis_text += (
            "\n" + roadmap["Result"]
        )

    else:

        for week, skills in roadmap.items():

            analysis_text += (
                f"\nWeek {week}:\n"
            )

            for skill in skills:

                analysis_text += (
                    f"- Learn {skill}\n"
                )


    st.download_button(
        label="📥 Download Analysis Report",
        data=analysis_text,
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )


else:

    # =====================================================
    # INITIAL SCREEN
    # =====================================================

    st.info(
        "👆 Upload a PDF resume above to begin analysis."
    )