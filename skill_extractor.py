import pandas as pd


def load_skill_dictionary(file_path):
    """
    Load skills from skill_dictionary.csv
    """
    df = pd.read_csv(file_path)

    skills = df["Skill"].dropna().tolist()

    return skills


def extract_skills(cleaned_text, skills):

    found_skills = []

    for skill in skills:

        if skill.lower() in cleaned_text:

            found_skills.append(skill)

    return sorted(found_skills)