
import streamlit as st
from openai import OpenAI
import os
from utils.fetch_data import get_league_by_team

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Match Analyzer", layout="centered")
st.title("⚽ Match Analyzer – AI-assistent för fotbollsanalys")

input_text = st.text_area(
    "Matchlista", 
    height=200, 
    placeholder="Exempel:\nIlves - KuPS\nMariehamn - VPS"
)

def generate_analysis(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Du är en sportjournalist som analyserar matcher med statistik, form, skador och tabell."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if input_text:
    teams = []
    for line in input_text.splitlines():
        if "-" in line:
            home, away = [t.strip() for t in line.split("-")]
            teams.extend([home, away])

    with st.expander("🔍 Ligainfo (upplockat automatiskt från RapidAPI)"):
        for team in teams:
            liga = get_league_by_team(team)
            if "error" in liga:
                st.warning(f"{team}: {liga['error']}")
            else:
                st.info(f"{team} spelar i {liga['name']} ({liga['country']}, {liga['season']})")

    if st.button("🔎 Analysera matcher"):
        with st.spinner("Analyserar..."):
            output = generate_analysis(input_text)
            st.subheader("🧠 AI-genererad matchanalys")
            st.markdown(output)
