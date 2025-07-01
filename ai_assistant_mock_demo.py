import streamlit as st

st.set_page_config(page_title="AI Assistant for EHR", layout="wide")

# Sidebar
st.sidebar.title("Select Patient Record")
patient = st.sidebar.selectbox("Choose a synthetic patient:", ["John Doe (65M)", "Jane Smith (58F)"])

st.title("🧠 AI Assistant (EHR-integrated)")

st.markdown("Ask a question about the patient record:")

# Sample input
user_question = st.text_input("e.g. Has the patient had an angiogram?")

# Predefined mock responses
responses = {
    "Has the patient had an angiogram?": {
        "answer": "Yes — the patient had an angiogram on 2025-05-10.",
        "source": "Cardiology report, May 10, 2025"
    },
    "What is the patient's baseline creatinine?": {
        "answer": "The patient’s baseline creatinine is approximately 1.2 mg/dL.",
        "source": "Lab result, October 14, 2023"
    },
    "What did cardiology recommend?": {
        "answer": "Cardiology recommended continuing dual antiplatelet therapy and repeating the echocardiogram in 3 months.",
        "source": "Cardiology note, May 11, 2025"
    },
    "What medications is the patient on?": {
        "answer": "The patient is on atorvastatin, clopidogrel, and PRN morphine.",
        "source": "MAR & Admission Orders, May 10–12, 2025"
    }
}

# Display mock response
if user_question:
    response = responses.get(user_question.strip(), {
        "answer": "I'm sorry, I don't have a mock answer for that question.",
        "source": "N/A"
    })
    st.subheader("🔍 Answer:")
    st.markdown(f"**{response['answer']}**")
    st.caption(f"📄 Source: {response['source']}")

# Generate Report
if st.button("Generate Head-to-Toe Report"):
    st.subheader("🩺 Head-to-Toe Summary:")
    st.markdown("""
- **Cardiovascular**: Prior MI (2018), stent placed, echo normal (2022).
- **Renal**: CKD Stage 3. Baseline Cr ~1.2 mg/dL.
- **Respiratory**: No active pulmonary issues documented.
- **GI**: No known bleeding. No recent colonoscopy noted.
- **Medications**: Atorvastatin, Clopidogrel, Morphine PRN.
- **Procedures**: Stent (2018), Angiogram (2025-05-10).
    """)
