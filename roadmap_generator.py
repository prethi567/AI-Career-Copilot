def generate_roadmap(skills):

    roadmap = []

    if "Python" in skills:
        roadmap.append({
            "title": "Learn Advanced Python and OOP Concepts",
            "link": "https://www.w3schools.com/python/"
        })

        roadmap.append({
            "title": "Practice Data Structures using Python",
            "link": "https://www.geeksforgeeks.org/data-structures/"
        })

    if "SQL" in skills:
        roadmap.append({
            "title": "Practice Advanced SQL Queries",
            "link": "https://www.w3schools.com/sql/"
        })

    if "Data Analysis" in skills:
        roadmap.append({
            "title": "Learn Pandas and NumPy",
            "link": "https://www.geeksforgeeks.org/python-pandas/"
        })

    roadmap.append({
        "title": "Learn Machine Learning",
        "link": "https://www.geeksforgeeks.org/machine-learning/"
    })

    roadmap.append({
        "title": "Build AI Projects",
        "link": "https://www.kaggle.com/learn"
    })

    return roadmap