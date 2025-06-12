import streamlit as st
import openai
import requests

# --- SETTINGS ---
openai.api_key = st.secrets.get("OPENAI_API_KEY")  # Lägg din API-nyckel i .streamlit/secrets.toml

# --- APP UI ---
st.title("Matchanalys med ChatGPT")
st.markdown("Skriv in dina matcher (t.ex. från en stryktipsrad):")

match_input = st.text_area("Matcher", "1. Arsenal - Liverpool\n2. Real Madrid - Valencia")
generate = st.button("Skapa analyser")

# --- HELPER FUNKTION FÖR PROMPT ---
def build_prompt(match_list):
    base = (
        "Du är en fotbollsexpert. Analysera varje match med:\n"
        "1. Senaste form (5 matcher)\n"
        "2. Skador och avstängningar\n"
        "3. Tabelläge (om relevant)\n"
        "4. Matchbild och sannolik utgång\n\n"
    )
    for match in match_list:
        base += f"Match: {match}\n"
    return base

# --- GÖR ANROP TILL OPENAI ---
def generate_analysis(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Du är en sportanalytiker som skriver tydliga matchanalyser."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

# --- HUVUDLOGIK ---
if generate and match_input.strip():
    match_list = [line.split(". ", 1)[-1] for line in match_input.strip().split("\n") if "-" in line]
    prompt = build_prompt(match_list)
    with st.spinner("Genererar analyser..."):
        output = generate_analysis(prompt)
    st.markdown("---")
    st.subheader("Analys")
    st.markdown(output)
else:
    if generate:
        st.warning("Du måste mata in minst en match.")
