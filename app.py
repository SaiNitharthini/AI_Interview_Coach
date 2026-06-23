import streamlit as st
import os
import re

from modules.dashboard import extract_scores
from modules.question_generator import generate_questions
from modules.evaluator import evaluate_answer
from modules.resume_parser import (
    extract_text,
    extract_skills
)

st.set_page_config(
    page_title="AI Interview Preparation Coach",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Interview Preparation Coach")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

os.makedirs("uploads", exist_ok=True)

if uploaded_file is not None:

    # Save Uploaded Resume
    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume Saved Successfully!")
    st.write("File Name:", uploaded_file.name)

    # Extract Resume Text
    resume_text = extract_text(file_path)

    st.write("Length:", len(resume_text))

    st.subheader("📄 Resume Content")

    st.text_area(
        "Extracted Text",
        resume_text,
        height=300
    )

    # Extract Skills
    skills = extract_skills(resume_text)

    st.subheader("🛠️ Detected Skills")

    cols = st.columns(3)

    for i, skill in enumerate(skills):
        cols[i % 3].success(skill)

    st.divider()

    # Generate Questions
    if st.button("🎯 Generate Interview Questions"):

        with st.spinner("Generating Questions..."):

            questions = generate_questions(
                resume_text,
                skills
            )

            st.session_state["questions"] = questions

    # Display Generated Questions
    if "questions" in st.session_state:

        st.subheader("📋 Generated Interview Questions")

        st.write(st.session_state["questions"])

    st.divider()

    # Mock Interview Section
    st.header("🎤 Mock Interview")

    selected_question = ""

    if "questions" in st.session_state:

        questions_text = st.session_state["questions"]

        question_list = []

        for line in questions_text.split("\n"):

            line = line.strip()

            if re.match(r"^\d+\.", line):
                question_list.append(line)

        if question_list:

            selected_question = st.selectbox(
                "Select Interview Question",
                question_list
            )

            st.info(
                f"Selected Question:\n\n{selected_question}"
            )

    question = selected_question

    answer = st.text_area(
        "Your Answer",
        height=200,
        placeholder="Type your interview answer here..."
    )

    # Evaluate Answer
    if st.button("✅ Evaluate Answer"):

        if not question:

            st.warning(
                "Please generate and select a question first."
            )

        elif not answer.strip():

            st.warning(
                "Please enter your answer."
            )

        else:

            with st.spinner("Evaluating Answer..."):

                result = evaluate_answer(
                    question,
                    answer
                )

                st.session_state["evaluation"] = result

    # Show Evaluation Result
    if "evaluation" in st.session_state:

        result = st.session_state["evaluation"]

        st.divider()

        st.subheader("📊 Evaluation Result")

        st.write(result)

        # Dashboard
        scores = extract_scores(result)

        accuracy = scores["accuracy"]
        completeness = scores["completeness"]
        communication = scores["communication"]

        overall_score = (
            accuracy +
            completeness +
            communication
        ) / 3

        st.divider()

        st.header("📈 Performance Dashboard")

        st.metric(
            "Overall Score",
            f"{overall_score:.1f}/10"
        )

        st.write("Technical Accuracy")
        st.progress(accuracy / 10)

        st.write("Completeness")
        st.progress(completeness / 10)

        st.write("Communication")
        st.progress(communication / 10)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Accuracy",
            f"{accuracy}/10"
        )

        col2.metric(
            "Completeness",
            f"{completeness}/10"
        )

        col3.metric(
            "Communication",
            f"{communication}/10"
        )