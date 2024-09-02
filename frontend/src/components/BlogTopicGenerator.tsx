import React, { useState } from "react";

const BlogTopicGenerator: React.FC = () => {
  const [keyword, setKeyword] = useState("");
  const [numTopics, setNumTopics] = useState(5);
  const [topics, setTopics] = useState<string[]>([]);

  const generateTopics = async () => {
    const response = await fetch(
      `http://localhost:5000/generate_blog_topics?keyword=${encodeURIComponent(
        keyword
      )}&num_topics=${numTopics}`
    );
    const data = await response.json();
    setTopics(data.blog_topics);
  };

  return (
    <div>
      <h2>Blog Topic Generator</h2>
      <input
        type="text"
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
        placeholder="Enter keyword"
      />
      <input
        type="number"
        value={numTopics}
        onChange={(e) => setNumTopics(parseInt(e.target.value))}
        min="1"
        max="10"
      />
      <button onClick={generateTopics}>Generate Topics</button>
      {topics.length > 0 && (
        <div className="results">
          <h3>Generated Topics:</h3>
          <ul>
            {topics.map((topic, index) => (
              <li key={index}>{topic}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default BlogTopicGenerator;
