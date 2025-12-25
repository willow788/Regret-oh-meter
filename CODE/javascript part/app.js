import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    if (!text) return;
    try {
      const response = await axios.post('http://127.0.0.1:8000/analyze', { text });
      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert("Backend not running or something went wrong.");
    }
  };

  const getMeterStyle = (score) => {
    if (score > 60) return { background: 'red', width: `${score}%` };
    if (score > 30) return { background: 'yellow', width: `${score}%` };
    return { background: 'green', width: `${score}%` };
  };

  return (
    <div className="App">
      <h1>Regret-o-Meter</h1>
      <textarea
        placeholder="Paste your daily chaos here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={8}
        cols={50}
      />
      <br />
      <button onClick={handleAnalyze}>Analyze</button>

      {result && (
        <div className="results">
          <h2>Regret Score: {result.regret_score}</h2>
          <div className="meter">
            <div className="fill" style={getMeterStyle(result.regret_score)}></div>
          </div>
          <h3>Top Regret:</h3>
          <p>{result.top_regret.line}</p>
          <h3>Comment:</h3>
          <p>{result.comment}</p>
        </div>
      )}
    </div>
  );
}

export default App;
