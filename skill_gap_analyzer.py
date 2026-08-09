import pandas as pd


def load_job_roles(file_path):
    """
    Load job roles and required skills from CSV.
    """
    return pd.read_csv(file_path)


def get_required_skills(job_roles, role):
    """
    Get the skills required for a particular job role.
    """

    selected_role = job_roles[
        job_roles["Role"].str.lower() == role.lower()
    ]

    if selected_role.empty:
        return []

    skills_text = selected_role.iloc[0]["Skills"]

    required_skills = [
        skill.strip()
        for skill in skills_text.split(",")
    ]

    return required_skills


def find_missing_skills(resume_skills, required_skills):
    """
    Compare resume skills with required job skills.
    """

    resume_skills_lower = {
        skill.lower().strip()
        for skill in resume_skills
    }

    missing_skills = []

    for skill in required_skills:

        if skill.lower().strip() not in resume_skills_lower:
            missing_skills.append(skill)

    return missing_skills