from resume_parser import extract_pdf
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary
from skill_extractor import extract_skills


# Resume path
resume_path = "sample_resumes/Resume.pdf"

# Skill dictionary path
skill_path = "data/skill_dictionary.csv"

# Extract resume text
resume_text = extract_pdf(resume_path)

# Clean text
cleaned_text = clean_text(resume_text)

# Load skills
skills = load_skill_dictionary(skill_path)

# Extract matching skills
found_skills = extract_skills(cleaned_text, skills)

print("\n===== SKILLS FOUND =====\n")

for skill in found_skills:
    print(skill)