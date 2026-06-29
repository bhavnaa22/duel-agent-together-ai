# 🤺 Together AI Duel Simulator

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Together AI](https://img.shields.io/badge/Together%20AI-6C63FF?style=for-the-badge)
![LLaMA](https://img.shields.io/badge/LLaMA%203-8B-orange?style=for-the-badge)

**Minimal, clean duel simulator — pick two AI personas, set the turns, watch the sparks fly.**

</div>

---

## 🎯 What is This?

The leanest version of the duel agent concept. A clean Streamlit app where you define two AI personas and a turn count, and LLaMA 3 (via Together AI) generates a back-and-forth debate/conversation between them. Great for quickly prototyping agent interaction patterns.

## ✨ Features

- 🎭 **Any persona** — type anything: "Sarcastic chef", "Overconfident CEO", "Sleep-deprived PhD student"
- 🔢 **Adjustable turns** — 1 to 10 rounds of conversation
- ⚡ **Instant results** — no waiting, no streaming delay
- 🪶 **Minimal codebase** — two files, easy to hack and extend

## 🚀 Quickstart

```bash
git clone https://github.com/bhavnaa22/duel-agent-together-ai
cd duel-agent-together-ai
pip install -r requirements.txt
streamlit run app.py
```

Add your Together AI key to `helper.py`:
```python
TOGETHER_API_KEY = "your_key_here"
```

## 📁 Files

```
duel-agent-together-ai/
├── app.py          # Streamlit UI
├── helper.py       # Together AI API wrapper + simulate_duel()
├── requirements.txt
└── README.md
```

## 💡 Example

| Setting | Value |
|---------|-------|
| Agent 1 | `Philosopher` |
| Agent 2 | `Comedian` |
| Turns | `5` |
| Result | 5 rounds of existential comedy |

## 🔧 Tech Stack

| Component | Technology |
|-----------|-----------|
| UI | Streamlit |
| LLM | LLaMA 3 (8B) via Together AI |
| Language | Python 3.10+ |
