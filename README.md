# ⚽ Match Analyzer – AI-driven matchanalys från stryktipsrader

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-blue?logo=streamlit)](https://streamlit.io/)
[![OpenAI Powered](https://img.shields.io/badge/Powered%20by-OpenAI-ffb400?logo=openai)](https://platform.openai.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

---

## 🎯 Vad är Match Analyzer?

**Match Analyzer** är en AI-assistent som automatiskt analyserar fotbollsmatcher baserat på en enkel textinput (t.ex. från Stryktipset). Appen använder OpenAI:s språkmodell och API-Football för att generera:

- 🔥 Lagform (senaste matcher)
- 🚑 Skador och avstängningar
- 📊 Tabellplacering
- 🧠 Matchanalys (förväntad bild av matchen)

---

## 🔍 Demo

Vill du se hur appen fungerar?

🖥️ **Webbdemo:** *(kommer snart)*  
🚀 Du kan deploya appen själv till [Streamlit Cloud](https://share.streamlit.io) och köra den direkt i webbläsaren.

### 📸 Skärmbild
Här är ett exempel på en inmatning i appen och hur analysen genereras:

![Demo](assets/demo_screenshot.png)

> Lägg en skärmdump i `assets/`-mappen med filnamnet `demo_screenshot.png`

---

### 📤 Alternativ: Skapa din egen demo med Streamlit Cloud
1. Gå till [https://share.streamlit.io](https://share.streamlit.io)
2. Logga in med GitHub
3. Välj ditt repo: `match-analyzer`
4. Ange fil: `match_analysis_app.py`
5. Appen körs nu online!

---

## 🚀 Kom igång

### 1. Klona projektet

```bash
git clone https://github.com/ulfboge/match-analyzer.git
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
