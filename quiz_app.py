import streamlit as st


st.title("Quiz on Units")

st.markdown("""
Welcome! This quiz has **10 questions**:
- First 5 are about **Fundamental Units**  
- Next 5 are about **Symbols of Derived Units**

Answer all and see your score & grade! 
""")

questions = [
    {"Q": "The unit used by British to measure height", "dimension": "L", "answer": "feet"},
    {"Q": "A unit used to measure atomic radius", "dimension": "L", "answer": "picometer"},
    {"Q": "Usually weights (weight-plate, dumbbells, etc.) in gym are measured in ____ unit.",  "dimension": "M", "answer": "kilogram"},
    {"Q": "The unit that appears most on a stopwatch", "dimension": "T", "answer": "second"},
    {"Q": "Unit to measure molar mass of elements or compounds", "dimension": "M", "answer": "gram"},
    {"Q": "SI unit used to measure speed of moving vehicle", "dimension": "LT^-1", "answer": "m/s"},
    {"Q": "This SI unit is used to measure a piece of land", "dimension": "L^2", "answer": "m^2"},
    {"Q": "This unit is used to represent momentum of an object", "dimension": "MLT^-1", "answer": "kg.m/s"},
    {"Q": "SI unit to measure force per unit area", "dimension": "ML^-1T^-2", "answer": "Pa"},
    {"Q": "This unit is used to measure frequency.", "dimension": "T^-1", "answer": "Hz"}
]

user_answers = []
score = 0

st.markdown("---")
st.subheader("Answer the following questions:")

for i, q in enumerate(questions):
    ans = st.text_input(f"Q{i+1}: {q['Q']} (Dimension: {q['dimension']})", key=f"q{i}")
    user_answers.append(ans.strip().lower())


if st.button("Submit Quiz"):
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"].lower():
            score += 1

    st.markdown(f"### Your Score: {score}/{len(questions)}")

    if score == 10:
        st.success(" You got **A+** grade in this game!")
    elif score >= 7:
        st.success(" You got **A** grade in this game!")
    elif score >= 5:
        st.info(" You got **B** grade in this game.")
    else:
        st.warning(" You need to work a little harder.")

    st.balloons()
