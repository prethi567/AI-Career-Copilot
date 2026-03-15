import streamlit as st
from resume_parser import extract_resume_text
from similarity_model import calculate_similarity
from skill_extractor import extract_skills
from roadmap_generator import generate_roadmap

st.set_page_config(page_title="CareerPilot AI", page_icon="🚀", layout="wide")

# Responsive CSS
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

body {
background: linear-gradient(135deg,#eef2ff,#fdf2f8);
}

.big-title{
font-size: clamp(36px,6vw,70px);
font-weight:900;
text-align:center;
background: linear-gradient(90deg,#4f46e5,#9333ea,#ec4899);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
margin-bottom:10px;
text-shadow: 2px 2px 10px rgba(0,0,0,0.15);
}


.subtitle{
text-align:center;
font-size: clamp(16px,2.5vw,22px);
color:#475569;
margin-bottom:40px;
}


.skill-box{
background:#eef2ff;
padding:10px 15px;
border-radius:10px;
display:inline-block;
margin:5px;
color:#1e3a8a;
font-weight:600;
font-size: clamp(12px,1.5vw,16px);
}

.roadmap{
background:#f8fafc;
padding:15px;
border-radius:10px;
margin-bottom:12px;
color:#111827;
font-size: clamp(14px,2vw,18px);
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="big-title">🚀 CareerPilot AI</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Analyze your resume, discover skill gaps, and build your AI career roadmap</div>',
unsafe_allow_html=True
)

# Upload Section
# Upload Section
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf","docx","png","jpg","jpeg"]
    )

with col2:
    job_description = st.text_area("💼 Paste Job Description")

st.markdown('</div>', unsafe_allow_html=True)


# Analyze Button
if st.button("✨ Analyze Resume"):

    if resume_file and job_description:

        resume_text = extract_resume_text(resume_file)

        score = calculate_similarity(resume_text, job_description)

        skills = extract_skills(resume_text)

        roadmap = generate_roadmap(skills)

        # Skills Section
        st.markdown("## 🧠 Detected Skills")

        skill_html = ""

        for skill in skills:
            skill_html += f'<span class="skill-box">{skill}</span>'

        st.markdown(skill_html, unsafe_allow_html=True)

        # Resume Score
        st.markdown("## 📊 Resume Match Score")

        st.progress(int(score))

        st.success(f"Your resume matches **{score:.2f}%** with the job description")

        # Roadmap
        st.markdown("## 🗺️ Your Career Roadmap")

        for step in roadmap:

            st.markdown(
                f"""
                <div class="roadmap">
                ✅ {step['title']}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(f"📚 [Study Resource]({step['link']})")

    else:
        st.warning("Please upload resume and enter job description.")
