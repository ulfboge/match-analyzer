import streamlit as st
from openai import OpenAI
from utils.fetch_data import get_match_stats
from utils.pdf_export import export_analysis_to_pdf

# --- SETTINGS ---
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

# --- APP UI ---
st.title("Matchanalys med ChatGPT")
st.markdown("Skriv in dina matcher (t.ex. från en stryktipsrad):")

match_input = st.text_area("Matcher", "1. Arsenal - Liverpool\n2. Real Madrid - Valencia")
generate = st.button("Skapa analyser")

# --- HELPER FUNKTION FÖR PROMPT ---
def build_prompt(match_data):
    base = (
        "Du är en fotbollsexpert. Analysera varje match med:\n"
        "1. Senaste form (5 matcher)\n"
        "2. Skador och avstängningar\n"
        "3. Tabelläge (om relevant)\n"
        "4. Matchbild och sannolik utgång\n\n"
    )
    for match in match_data:
        base += f"Match: {match['teams']}\n"
        base += f"Form hemmalag: {match['home_form']}\n"
        base += f"Form bortalag: {match['away_form']}\n"
        base += f"Tabellplacering: {match['table']}\n"
        base += f"Skador: {match['injuries']}\n\n"
    return base

# --- GÖR ANROP TILL OPENAI ---
def generate_analysis(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Du är en sportanalytiker som skriver tydliga matchanalyser."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# --- HUVUDLOGIK ---
if generate and match_input.strip():
    match_list = [line.split(". ", 1)[-1] for line in match_input.strip().split("\n") if "-" in line]
    with st.spinner("Hämtar statistik..."):
        match_data = get_match_stats(match_list)
    prompt = build_prompt(match_data)
    with st.spinner("Genererar analyser..."):
        output = generate_analysis(prompt)
    st.markdown("---")
    st.subheader("Analys")
    st.markdown(output)

    if st.button("Exportera till PDF"):
        filepath = export_analysis_to_pdf(output)
        with open(filepath, "rb") as f:
            st.download_button("Ladda ner PDF", f, file_name="matchanalys.pdf")
else:
    if generate:
        st.warning("Du måste mata in minst en match.")