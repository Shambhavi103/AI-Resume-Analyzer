def generate_roadmap(missing_skills):

    roadmap = {}

    total_skills = len(missing_skills)

    if total_skills == 0:
        return {
            "Result": "No major skill gaps found. You already have the required skills."
        }

    # Divide missing skills across 4 weeks
    for index, skill in enumerate(missing_skills):

        week = (index % 4) + 1

        if week not in roadmap:
            roadmap[week] = []

        roadmap[week].append(skill)

    return roadmap