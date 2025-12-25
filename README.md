# Regret-oh-Meter

**Ever wondered how chaotic your day really was?** The Regret-o-Meter is an AI-powered app that analyzes your text, social media snippets, or daily confessions, and gives you a **Regret Score**, highlights your **Top Regrets**, and delivers a **cheeky, sarcastic roast** of your choices.

Think of it as a **daily chaos evaluator**—because life is messy, and now you can quantify it.

---

## Features

* **Regret Scoring:** AI-powered scoring of your text based on sentiment, self-blame, sarcasm, and emojis.
* **Top Regret Highlight:** The line you’ll regret the most (or laugh at later).
* **Cheeky Comments:** Snarky, sarcastic messages about your chaos level.
* **Visual Meter:** Color-coded meter showing your daily chaos (green → smooth, yellow → risky, red → legendary chaos).
* **Emoji & Sarcasm Detection:** Extra points for 🙄😂😭 and phrases like “great idea” or “oops.”

---

## Tech Stack

* **Backend:** Python + FastAPI
* **AI:** Hugging Face Transformers for sentiment analysis
* **Frontend:** React + Axios for communication with the backend
* **Optional Storage:** JSON or SQLite for trend tracking

---

## Installation

1. **Clone the repo:**

```bash
git clone <your-repo-url>
cd regret-o-meter
```

2. **Setup Backend:**

```bash
python -m venv venv
# activate the environment
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install fastapi uvicorn transformers torch
```

3. **Run Backend:**

```bash
uvicorn main:app --reload
```

4. **Setup Frontend:**

```bash
cd regret-o-meter-frontend
npm install
npm start
```

5. Open `http://localhost:3000` and paste your chaotic text to see the Regret-o-Meter in action.

---

## Example Text

```
Forgot to submit my assignment 😩
Sent a risky text to my ex 🙄
Ate pizza at 3 AM 😂
Totally missed the meeting because I overslept
Bought 5 useless gadgets at midnight 😭
```

* Expect a **high regret score**, a highlighted **top regret**, and a **sarcastic comment**.

---

## Future Upgrades

* Track **daily/weekly regret trends**
* Animate the meter with **flames, tears, or confetti**
* **Top 3 regrets** instead of just one
* Export **shareable chaos reports**
* Optional **voice mode** for sarcastic readings

---
**Note:** I handled all the **ML/AI magic** behind the Regret-o-Meter, while the frontend, styling, and dashboard were whipped up by AI. This is just a **fun project on a chilly December afternoon**—not professional, just me playing around with chaos and code.

## License

MIT License – because chaos should be free.


