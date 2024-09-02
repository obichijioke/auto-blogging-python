import React, { useState } from "react";

const ContentOptimizer: React.FC = () => {
  const [content, setContent] = useState("");
  const [keyword, setKeyword] = useState("");
  const [optimizedContent, setOptimizedContent] = useState("");

  const optimizeContent = async () => {
    const response = await fetch("http://localhost:5000/optimize_content", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content, keyword }),
    });
    const data = await response.json();
    setOptimizedContent(data.optimized_content);
  };

  return (
    <div>
      <h2>Content Optimizer</h2>
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Enter your content here"
      />
      <input
        type="text"
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
        placeholder="Enter keyword"
      />
      <button onClick={optimizeContent}>Optimize Content</button>
      {optimizedContent && (
        <div className="results">
          <h3>Optimized Content:</h3>
          <p>{optimizedContent}</p>
        </div>
      )}
    </div>
  );
};

export default ContentOptimizer;
