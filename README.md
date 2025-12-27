# 🎭 Regret-o-Meter

<div align="center">




![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat-square&logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

**Ever wondered how chaotic your day really was? **

Paste your chaos, get your regret score, top regrets, and a sarcastic roast. Pure fun, not serious. 

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack)

</div>

---

## 🎪 What is This?

The **Regret-o-Meter** is an AI-powered app that analyzes your text, social media snippets, or daily confessions, and gives you: 

- 📊 **Regret Score** (0-100+) based on sentiment, self-blame, sarcasm, and emojis
- 🎯 **Top Regret Highlight** - The line you'll regret the most (or laugh at later)
- 💬 **Cheeky Comments** - Snarky, sarcastic feedback about your chaos level
- 🌈 **Visual Meter** - Color-coded chaos indicator (green → smooth, yellow → risky, red → LEGENDARY)

Think of it as a **daily chaos evaluator**—because life is messy, and now you can *quantify* it.  😅

---

## ✨ Features

### 🤖 AI-Powered Analysis
- **Sentiment Detection** - Identifies negative keywords and emotional patterns
- **Self-Blame Recognition** - Catches phrases like "I should have" or "It's my fault"
- **Sarcasm Detection** - Extra points for phrases like "great idea 🙄" or "yeah right"
- **Emoji Scoring** - Because 😭 deserves more regret points than 🙄

### 🎨 Visual Experience
- **Glitchy Retro UI** - Complete with rainbow gradients and animated effects
- **Dynamic Meter** - Color changes based on your chaos level
- **Animated Feedback** - Pulsing, rotating, glitching text effects
- **Responsive Design** - Works on desktop and mobile

### 📈 Smart Scoring System

| Category | Examples | Score |
|----------|----------|-------|
| **Negative Keywords** | bad, terrible, disaster, regret | +300 |
| **Self-Blame** | oops, shouldn't, forgot, ugh | +200 |
| **Sarcasm** | great idea, yeah right, totally | +150-250 |
| **Self-Critical Words** | stupid, idiot, lazy, foolish | +200 |
| **Emojis** | 😭 (+4), 😢 (+3), 🙄 (+1) | +1-4 |

---

## 🎬 Demo

### Example Input: 
```
Forgot to submit my assignment 😩
Sent a risky text to my ex 🙄
Ate pizza at 3 AM 😂
Totally missed the meeting because I overslept
Bought 5 useless gadgets at midnight 😭
```

### Expected Output:
```
Regret Score: 87/100

🎯 Top Regret: 
"Sent a risky text to my ex 🙄"

💬 Comment: 
"Legendary chaos.  You've peaked.  Frame this moment.  🏆"
```

---

## 🚀 Installation

### Prerequisites

- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **Node.js 14+** - [Download here](https://nodejs.org/)
- **npm** or **yarn**

### Step 1: Clone the Repository

```bash
git clone https://github.com/willow788/Regret-oh-meter.git
cd Regret-oh-meter
```

### Step 2: Setup Backend (Python + FastAPI)

```bash
# Navigate to backend directory
cd CODE/python\ code

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows: 
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn transformers torch pydantic
```

### Step 3: Run Backend Server

```bash
# Make sure you're in CODE/python code directory
uvicorn main:app --reload
```

The backend will start at `http://127.0.0.1:8000` 🚀

### Step 4: Setup Frontend (React)

Open a **new terminal** window: 

```bash
# Navigate to frontend directory (create if doesn't exist)
mkdir -p regret-o-meter-frontend
cd regret-o-meter-frontend

# Initialize React app (if not already done)
npx create-react-app . 

# Copy the frontend files
# Copy CODE/javascript part/app.js to src/App.js
# Copy CODE/styling css/app.css to src/App.css

# Install axios
npm install axios

# Start development server
npm start
```

The frontend will open at `http://localhost:3000` 🎨

---

## 📖 Usage

### Quick Start

1. **Start the backend** (in one terminal):
   ```bash
   cd CODE/python\ code
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   uvicorn main:app --reload
   ```

2. **Start the frontend** (in another terminal):
   ```bash
   cd regret-o-meter-frontend
   npm start
   ```

3. **Open your browser** to `http://localhost:3000`

4. **Paste your chaotic text** in the textarea

5. **Click "Analyze"** and watch the magic happen!  ✨

### Example Texts to Try

#### Low Chaos (Score: 10-30)
```
Had a productive day
Finished all my tasks on time
Feeling good about my decisions
```

#### Medium Chaos (Score: 40-60)
```
Should have started earlier 😅
Forgot to reply to an email
Made a small mistake at work
```

#### LEGENDARY Chaos (Score: 80-100+)
```
Sent a work email to the wrong person 😭
Totally missed my deadline because Netflix
Bought something I definitely can't afford 💸
Argued with someone I shouldn't have 😤
Ate an entire pizza at 2 AM and regret everything 🙄
```

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for Python
- **Pydantic** - Data validation using Python type annotations
- **Python 3.8+** - Core programming language
- **CORS Middleware** - Cross-Origin Resource Sharing support

### Frontend
- **React 18+** - UI library for building interactive interfaces
- **Axios** - Promise-based HTTP client
- **CSS3** - Advanced animations and styling
- **Google Fonts** - Bangers, Creepster, Rubik Glitch

### AI/ML (Planned Enhancement)
- **Hugging Face Transformers** - For advanced sentiment analysis
- **PyTorch** - Deep learning framework

### Optional Storage (Future)
- **JSON** - Simple file-based storage
- **SQLite** - Lightweight database for trend tracking

---

## 📂 Project Structure

```
Regret-oh-meter/
├── CODE/
│   ├── python code/
│   │   └── main.py              # FastAPI backend server
│   ├── javascript part/
│   │   └── app.js               # React frontend component
│   └── styling css/
│       └── app.css              # Glitchy retro styling
├── demonstration!/              # Demo screenshots/videos
├── LICENSE                      # MIT License
└── README.md                    # You are here! 
```

---

## 🎨 UI Features

### Animations
- **Glitch Effect** - Cyberpunk-style text distortion
- **Rainbow Gradient** - Animated background transitions
- **Pulse Animation** - Breathing effect on key elements
- **Shake Effect** - Emoji decorations that vibrate
- **Rotating Icons** - (Planned) Spinning indicators

### Color Coding

| Score Range | Color | Meaning |
|-------------|-------|---------|
| 0-30 | 🟢 Green | "Smooth sailing" |
| 31-60 | 🟡 Yellow | "Risky territory" |
| 61-100+ | 🔴 Red | "LEGENDARY chaos" |

---

## 🎯 How It Works

### Scoring Algorithm

1. **Text Splitting** - Input divided into individual lines
2. **Pattern Matching** - Each line analyzed for: 
   - Negative keywords (bad, terrible, disaster)
   - Self-blame phrases (I should have, It's my fault)
   - Sarcasm indicators (great idea, yeah right)
   - Emotional emojis (😭😩😤)
3. **Score Calculation** - Points accumulated based on matches
4. **Aggregation** - Average score calculated across all lines
5. **Top Regret** - Line with highest individual score identified
6. **Comment Generation** - Sarcastic feedback based on total score

### Comment System

```python
if average_score > 80:
    "Legendary chaos. You've peaked. Frame this moment. 🏆"
elif average_score > 50:
    "Yikes. That's a lot of regret fuel. ☕"
elif average_score > 30:
    "Not terrible, but not great either. Room for improvement. 📉"
else:
    "You're basically a zen master.  Teach us your ways. 🧘"
```

---

## 🔮 Future Upgrades

### Planned Features

- [ ] **Weekly Regret Trends** - Track your chaos over time
- [ ] **Top 3 Regrets** - Highlight multiple chaotic moments
- [ ] **Animated Meter** - Add flames 🔥, tears 💧, or confetti 🎉
- [ ] **Shareable Reports** - Export as image or PDF
- [ ] **Voice Mode** - Sarcastic text-to-speech readings
- [ ] **Historical Comparison** - "This week vs last week"
- [ ] **Regret Categories** - Social, work, health, financial
- [ ] **AI Enhancement** - Use Hugging Face models for better sentiment
- [ ] **Dark/Light Mode** - Theme switching
- [ ] **Mobile App** - React Native version

### Advanced AI Features (v2.0)

- **Contextual Understanding** - GPT integration for deeper analysis
- **Emotion Detection** - Identify shame, guilt, frustration separately
- **Personalized Feedback** - Learn your patterns over time
- **Regret Prediction** - "This message might cause regret"
- **Comparative Analysis** - "Your chaos is 37% above average"

---

## 🤝 Contributing

Contributions are **absolutely welcome**! This is a fun project, so let's keep it lighthearted. 

### How to Contribute

1. **Fork** the repository
2. **Create a branch**:  `git checkout -b feat/amazing-roast`
3. **Make your changes** (add funnier comments, better scoring, new animations)
4. **Commit**: `git commit -m 'Add even more sarcasm'`
5. **Push**: `git push origin feat/amazing-roast`
6. **Open a Pull Request**

### Contribution Ideas

- 💬 **Add more sarcastic comments** - The funnier, the better
- 🎨 **Improve UI/UX** - Make it even more chaotic
- 🧠 **Enhance AI** - Better sentiment detection
- 📊 **Add features** - Implement the roadmap items
- 🐛 **Fix bugs** - Because chaos needs boundaries
- 📚 **Documentation** - Help others understand the chaos

---

## 🐛 Known Issues

- **Backend not running** - Make sure FastAPI server is active on port 8000
- **CORS errors** - Middleware is configured; check if both servers are running
- **Styling issues** - Ensure `App.css` is properly imported
- **No results** - Check browser console for errors

**Troubleshooting:**
```bash
# Check if backend is running
curl http://127.0.0.1:8000/docs

# Check if frontend is connected
# Open browser DevTools → Network tab → Look for POST to /analyze
```

---

## 📜 License

This project is licensed under the **MIT License** - because chaos should be free. 

You are free to:
- ✅ Use for personal projects
- ✅ Modify and distribute
- ✅ Use commercially (if you dare)
- ✅ Make it even more chaotic

Just include the license and have fun! 🎉

---

## 👨‍💻 Author

**willow788**

*"I handled all the ML/AI magic behind the Regret-o-Meter, while the frontend, styling, and dashboard were whipped up by AI. This is just a fun project on a chilly December afternoon—don't take it too seriously!"*

---

## 🙏 Acknowledgements

- **FastAPI** - For making Python backends fun again
- **React** - For component-based chaos
- **Hugging Face** - For transformer models (future integration)
- **Google Fonts** - For glitchy typography
- **Coffee** ☕ - For powering late-night coding sessions
- **My Ex** - For inspiring the "risky text" example 😂
- **Chatgpt** - For the Frontend and integrating backend

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/willow788/Regret-oh-meter?style=social)
![GitHub forks](https://img.shields.io/github/forks/willow788/Regret-oh-meter?style=social)

---

## 💡 Disclaimer

**This is a FUN PROJECT. ** 

- ❌ Not medical advice
- ❌ Not therapy
- ❌ Not a real regret assessment tool
- ✅ Pure entertainment
- ✅ For laughs
- ✅ To quantify your chaos

If you're experiencing serious regret or emotional distress, please talk to a professional. This app just roasts you.  😊

---

<div align="center">

### 🎭 Ready to Measure Your Chaos? 🎭

**[Get Started](#-installation)** • **[View Demo](#-demo)** • **[Contribute](#-contributing)**

Made with 💥 and regret in December 2025

</div>

---

## 🎪 FAQ

**Q: Is this serious?**  
A: Absolutely not.  It's 100% chaos theater. 

**Q: Will it actually help me?**  
A: Help you laugh at yourself? Yes.  Help you make better decisions? Probably not.

**Q: Can I use this for my texts before sending?**  
A: Sure! But if the regret score is high, maybe...  don't send?  Just a thought.  🙄

**Q: Why does it roast me so hard?**  
A: Because you pasted chaos and expected sympathy. The algorithm shows no mercy.

**Q: Can I customize the comments?**  
A: Yes! Edit `main.py` and add your own sarcastic masterpieces.

**Q: Does it store my data?**  
A:  Currently, no. Everything is processed in real-time and forgotten immediately.

---

<div align="center">

**⚡ If this made you laugh (or cry), give it a star!  ⭐**

[⬆ Back to Top](#-regret-o-meter)

</div>
