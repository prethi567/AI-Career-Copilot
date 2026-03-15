import pandas as pd

def extract_skills(text):

    skills = pd.read_csv("dataset/skills.csv", header=None)
    skills_list = skills[0].tolist()

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
