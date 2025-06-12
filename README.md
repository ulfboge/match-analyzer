
# ⚽ Match Analyzer – AI-driven matchanalys från stryktipsrader

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-blue?logo=streamlit)](https://streamlit.io/)
[![OpenAI Powered](https://img.shields.io/badge/Powered%20by-OpenAI-ffb400?logo=openai)](https://platform.openai.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🎯 Vad är Match Analyzer?

**Match Analyzer** är en AI-assistent som automatiskt analyserar fotbollsmatcher baserat på en enkel textinput (t.ex. från Stryktipset). Appen använder OpenAI:s språkmodell och API-Football för att generera:

- 🔥 Lagform (senaste matcher)
- 🚑 Skador och avstängningar
- 📊 Tabellplacering
- 🧠 Matchanalys (förväntad bild av matchen)
- 📌 Automatisk ligainformation per lag

---

## 🔍 Demo

🖥️ **Webbdemo:** *(kommer snart)*  
🚀 Du kan deploya appen själv till [Streamlit Cloud](https://share.streamlit.io) och köra den direkt i webbläsaren.

### 📸 Skärmbild
![Demo](assets/demo_screenshot.png)

> Lägg en skärmdump i `assets/`-mappen med filnamnet `demo_screenshot.png`

---

## 🚀 Kom igång

### 1. Klona projektet

```bash
git clone https://github.com/<ditt-användarnamn>/match-analyzer.git
cd match-analyzer
```

### 2. Skapa och aktivera en virtuell miljö

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
```

### 3. Installera beroenden

```bash
pip install -r requirements.txt
```

### 4. Lägg till API-nycklar

Skapa `.streamlit/secrets.toml` och fyll i:

```toml
OPENAI_API_KEY = "din-openai-nyckel"
RAPIDAPI_KEY = "din-rapidapi-api-football-nyckel"
```

---

## ▶️ Starta appen

```bash
streamlit run match_analysis_app.py
```

---

## 📁 Projektstruktur

```
match-analyzer/
├── .streamlit/
├── assets/
├── utils/
│   └── fetch_data.py
├── match_analysis_app.py
├── requirements.txt
└── README.md
```

---

## 📄 Licens

MIT – du får använda, modifiera och sprida fritt.

---

## 💬 Feedback & utveckling

Skicka gärna pull requests eller mejla [johan@kombagis.se](mailto:johan@kombagis.se).
