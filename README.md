# 📊 Match Analyzer App

En Streamlit-applikation som analyserar fotbollsmatcher utifrån en enkel matchlista, t.ex. från en stryktipsrad. Appen använder API-Football (via RapidAPI) för att hämta aktuell statistik och GPT-4 via OpenAI för att generera naturliga matchanalyser.

---

## 🚀 Funktioner

* 📝 Inmatning av matchlista i formatet `Hemmalag - Bortalag`
* 📈 Hämtar form och tabellplacering via API-Football
* 🧠 Genererar AI-baserad analys med OpenAI GPT-4
* 📄 Exportera analysen som PDF

---

## 🔧 Installation

### 1. Klona repo

```bash
git clone https://github.com/ditt-användarnamn/match-analyzer.git
cd match-analyzer
```

### 2. Skapa virtuell miljö (valfritt men rekommenderat)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Installera beroenden

```bash
pip install -r requirements.txt
```

---

## 🔑 API-nycklar

Skapa filen `.streamlit/secrets.toml` och fyll i:

```toml
OPENAI_API_KEY = "din-openai-api-nyckel"
RAPIDAPI_KEY = "din-rapidapi-nyckel"
```

👉 Skaffa nycklar från:

* [OpenAI](https://platform.openai.com/account/api-keys)
* [API-Football (RapidAPI)](https://rapidapi.com/api-sports/api/api-football)

---

## ▶️ Starta appen

```bash
streamlit run match_analysis_app.py
```

Eller dubbelklicka på `start_app.bat` (Windows).

Appen körs på: `http://localhost:8501`

---

## 📁 Filstruktur

```bash
match-analyzer/
├── match_analysis_app.py        # Streamlit-huvudfil
├── utils/
│   ├── fetch_data.py           # Hämtar statistik från API-Football
│   └── pdf_export.py           # Exporterar PDF
├── .streamlit/
│   └── secrets.toml            # API-nycklar
├── start_app.bat               # Startscript för Windows
├── requirements.txt            # Python-paket
└── README.md                   # Dokumentation
```

---

## 🧠 Framtida förbättringar

* Automatisk ligatolkning
* Live odds-integration
* Stöd för skadedata via API

---

## 🧑‍💻 Skapad av

[**Johan Karlsson** – Komba GIS AB](https://www.linkedin.com/in/kombagis)
