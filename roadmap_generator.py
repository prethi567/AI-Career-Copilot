def generate_roadmap(skills):

    roadmap = []

    # Convert skills to lowercase for safer checking
    skills = [skill.lower() for skill in skills]

    if "python" in skills:
        roadmap.append({
            "title": "Learn Advanced Python and OOP Concepts",
            "link": "https://www.w3schools.com/python/"
        })

        roadmap.append({
            "title": "Practice Data Structures using Python",
            "link": "https://www.geeksforgeeks.org/data-structures/"
        })

    if "sql" in skills:
        roadmap.append({
            "title": "Practice Advanced SQL Queries",
            "link": "https://www.w3schools.com/sql/"
        })

    if "data analysis" in skills:
        roadmap.append({
            "title": "Learn Pandas and NumPy",
            "link": "https://www.geeksforgeeks.org/python-pandas/"
        })

    # Always recommend ML learning
    roadmap.append({
        "title": "Learn Machine Learning Fundamentals",
        "link": "https://www.geeksforgeeks.org/machine-learning/"
    })

    roadmap.append({
        "title": "Build AI Projects for Portfolio",
        "link": "https://www.kaggle.com/learn"
    })

    roadmap.append({
        "title": "Practice Coding Interviews",
        "link": "https://leetcode.com"
    })

    return roadmap
