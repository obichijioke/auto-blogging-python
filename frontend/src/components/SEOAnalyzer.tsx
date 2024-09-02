import React, { useState } from "react";

const SEOAnalyzer: React.FC = () => {
  const [content, setContent] = useState("");
  const [keyword, setKeyword] = useState("");
  const [results, setResults] = useState<any>(null);

  const analyzeSEO = async () => {
    const response = await fetch("http://localhost:5000/analyze_seo", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content, keyword }),
    });
    const data = await response.json();
    setResults(data);
  };

  return (
    <div>
      <h2>SEO Analyzer</h2>
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
      <button onClick={analyzeSEO}>Analyze SEO</button>
      {results && (
        <div className="results">
          <h3>Results:</h3>
          <pre>{JSON.stringify(results, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default SEOAnalyzer;
