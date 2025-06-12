import streamlit as st
from openai import OpenAI
from utils.fetch_data import get_match_stats
from utils.pdf_export import export_analysis_to_pdf

# Initiera OpenAI-klienten
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Generera analys med nya OpenAI API
def generate_analysis(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Du är en sportanalytiker som skriver tydliga matchanalyser."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="Match Analyzer", page_icon="⚽")
st.title("⚽ Match Analyzer")
st.markdown("Mata in dina matcher (t.ex. från en Stryktipsrad):")

input_text = st.text_area("Matchlista", height=200, placeholder="Exempel:
1. Arsenal - Liverpool
2. AIK - Hammarby")

if st.button("Analysera"):
    matches = [line.split('.', 1)[1].strip() for line in input_text.strip().splitlines() if '-' in line]
    stats = get_match_stats(matches)

    prompt = ""
    for m in stats:
        prompt += f"""
Analysera matchen mellan {m['teams']}:
- Form för hemmalag: {m['home_form']}
- Form för bortalag: {m['away_form']}
- Tabellposition: {m['table']}
- Skador: {m['injuries']}
"""

    output = generate_analysis(prompt)
    st.markdown("### 📊 Analys")
    st.write(output)

    if st.button("Exportera till PDF"):
        filepath = export_analysis_to_pdf(output)
        with open(filepath, "rb") as f:
            st.download_button("Ladda ner PDF", f, file_name="matchanalys.pdf")
