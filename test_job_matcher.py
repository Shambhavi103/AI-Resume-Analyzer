from resume_parser import extract_pdf
from text_cleaner import clean_text
from job_matcher import match_jobs

# Resume path
resume_path = "sample_resumes/Resume.pdf"

# Job dataset path
job_path = "data/job_roles.csv"

# Extract resume
resume_text = extract_pdf(resume_path)

# Clean resume
cleaned_text = clean_text(resume_text)

# Match jobs
results = match_jobs(cleaned_text, job_path)

print("\n===== TOP JOB RECOMMENDATIONS =====\n")

print(results[["Role", "Match Score"]])