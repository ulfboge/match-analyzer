## 📄 `README.md` – färdig att använda

````markdown
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

---

## 🚀 Kom igång

### 1. Klona projektet

```bash
git clone https://github.com/<ditt-användarnamn>/match-analyzer.git
cd match-analyzer
````

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

Skapa filen `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "din-openai-nyckel"
RAPIDAPI_KEY = "din-rapidapi-api-football-nyckel"
```

---

## ▶️ Starta appen

```bash
streamlit run match_analysis_app.py
```

Appen körs nu lokalt på: [http://localhost:8501](http://localhost:8501)

---

## 📁 Projektstruktur

```
match-analyzer/
├── .streamlit/         # API-nycklar
├── assets/             # Logotyper, grafik
├── utils/              # Datahämtning och PDF-export
├── match_analysis_app.py
├── requirements.txt
├── start_app.bat
└── README.md
```

---

## 📄 Licens

MIT – du får använda, modifiera och sprida fritt.

---

## 💬 Feedback & utveckling

Vill du bidra eller komma med förbättringsförslag? Skicka ett pull request eller mejla [johan@kombagis.se](mailto:johan@kombagis.se).

```

---

Vill du att jag även:
- Skapar en `LICENSE`-fil (MIT)?
- Gör en demo-PDF som exempel?
- Förbereder en deployment till [Streamlit Cloud](https://share.streamlit.io)?
```
