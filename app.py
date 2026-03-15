import streamlit as st
from resume_parser import extract_resume_text
from similarity_model import calculate_similarity
from skill_extractor import extract_skills
from roadmap_generator import generate_roadmap

st.set_page_config(page_title="AI Career Copilot", page_icon="🚀", layout="wide")

# ------------------- CSS -------------------

st.markdown("""
<style>

body {
background: linear-gradient(120deg,#e0f2fe,#fce7f3);
}

.title{
font-size:60px;
font-weight:900;
text-align:center;
color:#0f172a;
margin-bottom:10px;
}

.subtitle{
text-align:center;
font-size:22px;
color:#334155;
margin-bottom:30px;
}

.skill-box{
background:#2563eb;
color:white;
padding:8px 14px;
border-radius:8px;
display:inline-block;
margin:5px;
font-weight:600;
}

.missing-box{
background:#ef4444;
color:white;
padding:8px 14px;
border-radius:8px;
display:inline-block;
margin:5px;
font-weight:600;
}

.roadmap{
background:#ffffffaa;
padding:15px;
border-radius:10px;
margin-bottom:10px;
font-size:18px;
}

a{
color:#2563eb;
font-weight:600;
text-decoration:none;
}

</style>
""", unsafe_allow_html=True)

# ------------------- TITLE -------------------

st.markdown('<div class="title">🚀 AI Career Copilot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload your resume and get AI powered career insights</div>', unsafe_allow_html=True)

# ------------------- INPUT -------------------

resume_file = st.file_uploader(
"📄 Upload Resume",
type=["pdf","docx","png","jpg","jpeg"]
)

job_description = st.text_area("💼 Paste Job Description")

# ------------------- ANALYZE -------------------

if st.button("✨ Analyze Resume"):

    if resume_file and job_description:

        resume_text = extract_resume_text(resume_file)

        score = calculate_similarity(resume_text, job_description)

        skills = extract_skills(resume_text)

        job_skills = extract_skills(job_description)

        roadmap = generate_roadmap(skills)

        # ------------------- DETECTED SKILLS -------------------

        st.markdown("## 🧠 Detected Skills")

        skill_html = ""

        for skill in skills:
            skill_html += f'<span class="skill-box">{skill}</span>'

        st.markdown(skill_html, unsafe_allow_html=True)

        # ------------------- MATCH SCORE -------------------

        st.markdown("## 📊 Resume Match Score")

        st.progress(int(score))

        st.success(f"Your resume matches **{score:.2f}%** with the job description")

        # ------------------- MISSING SKILLS -------------------

        st.markdown("## ❌ Missing Skills")

        missing_skills = []

        for skill in job_skills:
            if skill not in skills:
                missing_skills.append(skill)

        if missing_skills:

            missing_html = ""

            for skill in missing_skills:
                missing_html += f'<span class="missing-box">{skill}</span>'

            st.markdown(missing_html, unsafe_allow_html=True)

        else:
            st.success("Your resume already contains most required skills 🎉")

        # ------------------- SUGGESTIONS -------------------

        st.markdown("## 💡 Resume Improvement Suggestions")

        suggestions = []

        if len(skills) < 5:
            suggestions.append("Add more technical skills related to the job.")

        if missing_skills:
            suggestions.append("Try learning the missing skills listed above.")

        suggestions.append("Add measurable achievements in your projects.")
        suggestions.append("Mention tools and technologies used.")

        for tip in suggestions:
            st.write("✔", tip)

        # ------------------- ROADMAP -------------------

        st.markdown("## 🗺️ Learning Roadmap")

        for step in roadmap:

            st.markdown(
                f"""
                <div class="roadmap">
                ✅ {step['title']} <br>
                📚 <a href="{step['link']}" target="_blank">Study Resource</a>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.warning("Please upload resume and enter job description.")
