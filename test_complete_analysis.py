from resume_parser import extract_pdf
from text_cleaner import clean_text

from skill_extractor import load_skill_dictionary
from skill_extractor import extract_skills

from skill_gap_analyzer import load_job_roles
from skill_gap_analyzer import get_required_skills
from skill_gap_analyzer import find_missing_skills

from roadmap_generator import generate_roadmap


# ==========================================
# FILE PATHS
# ==========================================

resume_path = "sample_resumes/Resume.pdf"
skill_path = "data/skill_dictionary.csv"
job_path = "data/job_roles.csv"


# ==========================================
# RESUME PROCESSING
# ==========================================

resume_text = extract_pdf(resume_path)

cleaned_text = clean_text(resume_text)


# ==========================================
# SKILL EXTRACTION
# ==========================================

skills = load_skill_dictionary(skill_path)

resume_skills = extract_skills(
    cleaned_text,
    skills
)


# ==========================================
# LOAD JOB ROLES
# ==========================================

job_roles = load_job_roles(job_path)


# ==========================================
# SELECT ROLE
# ==========================================

selected_role = "Machine Learning Engineer"


# ==========================================
# REQUIRED SKILLS
# ==========================================

required_skills = get_required_skills(
    job_roles,
    selected_role
)


# ==========================================
# FIND MISSING SKILLS
# ==========================================

missing_skills = find_missing_skills(
    resume_skills,
    required_skills
)


# ==========================================
# GENERATE ROADMAP
# ==========================================

roadmap = generate_roadmap(missing_skills)


# ==========================================
# DISPLAY EVERYTHING
# ==========================================

print("\n========================================")
print("       COMPLETE RESUME ANALYSIS")
print("========================================")

print("\nJob Role:")
print(selected_role)


print("\nResume Skills:")

for skill in resume_skills:
    print("-", skill)


print("\nRequired Skills:")

for skill in required_skills:
    print("-", skill)


print("\nMissing Skills:")

if missing_skills:

    for skill in missing_skills:
        print("-", skill)

else:

    print("No missing skills found.")


print("\n4-WEEK LEARNING ROADMAP:")

if "Result" in roadmap:

    print(roadmap["Result"])

else:

    for week, skills in roadmap.items():

        print(f"\nWeek {week}")

        for skill in skills:
            print("-", skill)