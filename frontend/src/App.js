import React, { useState } from "react";
import axios from "axios";
import "./styles/styles.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const analyzeSentiment = async () => {
    if (!text.trim()) {
      setResult("Please enter some text.");
      return;
    }

    try {
      const response = await axios.post("http://localhost:5000/analyze", {
        text: text,
      });
      setResult(response.data.sentiment || "No sentiment detected.");
    } catch (error) {
      console.error("Error analyzing sentiment:", error);
      setResult("An error occurred. Please try again.");
    }
  };

  return (
    <div className="container">
      <h1>DC Sentiment Analysis Tool (AI-powered)</h1>
      <textarea
        rows="5"
        placeholder="Enter text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={analyzeSentiment}>Analyze Sentiment</button>
      {result && <div className="result">Sentiment: {result}</div>}
    </div>
  );
}

export default App;
