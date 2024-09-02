import React, { useState } from "react";

const ContentGenerator: React.FC = () => {
  const [keyword, setKeyword] = useState("");
  const [generatedContent, setGeneratedContent] = useState("");

  const generateContent = async () => {
    const response = await fetch("http://localhost:5000/generate_content", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ keyword }),
    });
    const data = await response.json();
    setGeneratedContent(data.generated_content);
  };

  return (
    <div>
      <h2>Content Generator</h2>
      <input
        type="text"
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
        placeholder="Enter keyword"
      />
      <button onClick={generateContent}>Generate Content</button>
      {generatedContent && (
        <div className="results">
          <h3>Generated Content:</h3>
          <p>{generatedContent}</p>
        </div>
      )}
    </div>
  );
};

export default ContentGenerator;
