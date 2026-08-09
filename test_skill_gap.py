from resume_parser import extract_pdf
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary
from skill_extractor import extract_skills

from skill_gap_analyzer import load_job_roles
from skill_gap_analyzer import get_required_skills
from skill_gap_analyzer import find_missing_skills


# --------------------------------
# FILE PATHS
# --------------------------------

resume_path = "sample_resumes/Resume.pdf"
skill_path = "data/skill_dictionary.csv"
job_path = "data/job_roles.csv"


# --------------------------------
# STEP 1: EXTRACT RESUME TEXT
# --------------------------------

resume_text = extract_pdf(resume_path)


# --------------------------------
# STEP 2: CLEAN RESUME TEXT
# --------------------------------

cleaned_text = clean_text(resume_text)


# --------------------------------
# STEP 3: EXTRACT RESUME SKILLS
# --------------------------------

skills = load_skill_dictionary(skill_path)

resume_skills = extract_skills(
    cleaned_text,
    skills
)


# --------------------------------
# STEP 4: LOAD JOB ROLES
# --------------------------------

job_roles = load_job_roles(job_path)


# --------------------------------
# STEP 5: SELECT A JOB ROLE
# --------------------------------

selected_role = "Machine Learning Engineer"


# --------------------------------
# STEP 6: GET REQUIRED SKILLS
# --------------------------------

required_skills = get_required_skills(
    job_roles,
    selected_role
)


# --------------------------------
# STEP 7: FIND MISSING SKILLS
# --------------------------------

missing_skills = find_missing_skills(
    resume_skills,
    required_skills
)


# --------------------------------
# DISPLAY RESULTS
# --------------------------------

print("\n================================")
print("       SKILL GAP ANALYSIS")
print("================================")

print("\nSelected Job Role:")
print(selected_role)

print("\nSkills Found in Resume:")
for skill in resume_skills:
    print("-", skill)

print("\nRequired Skills:")
for skill in required_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)