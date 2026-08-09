from roadmap_generator import generate_roadmap


# Example missing skills
missing_skills = [
    "TensorFlow",
    "Docker",
    "MLflow",
    "AWS"
]


roadmap = generate_roadmap(missing_skills)


print("\n================================")
print("       4-WEEK LEARNING ROADMAP")
print("================================")


if "Result" in roadmap:

    print("\n" + roadmap["Result"])

else:

    for week, skills in roadmap.items():

        print(f"\nWeek {week}")

        for skill in skills:
            print("-", skill)