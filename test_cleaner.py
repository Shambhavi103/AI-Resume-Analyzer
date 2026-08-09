from resume_parser import extract_pdf
from text_cleaner import clean_text

# Change this if your resume has a different name
file_path = "sample_resumes/Resume.pdf"

# Extract text
resume_text = extract_pdf(file_path)

# Clean text
cleaned_text = clean_text(resume_text)

print("===== ORIGINAL TEXT =====\n")
print(resume_text)

print("\n===== CLEANED TEXT =====\n")
print(cleaned_text)