import React, { useState } from "react";
import SEOAnalyzer from "./components/SEOAnalyzer";
import ContentOptimizer from "./components/ContentOptimizer";
import BlogTopicGenerator from "./components/BlogTopicGenerator";
import ContentGenerator from "./components/ContentGenerator";
import "./style.css";

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState("seo");

  return (
    <div className="app">
      <h1>SEO & Content Tool</h1>
      <div className="tabs">
        <button
          onClick={() => setActiveTab("seo")}
          className={activeTab === "seo" ? "active" : ""}
        >
          SEO Analyzer
        </button>
        <button
          onClick={() => setActiveTab("optimize")}
          className={activeTab === "optimize" ? "active" : ""}
        >
          Content Optimizer
        </button>
        <button
          onClick={() => setActiveTab("topics")}
          className={activeTab === "topics" ? "active" : ""}
        >
          Blog Topic Generator
        </button>
        <button
          onClick={() => setActiveTab("content")}
          className={activeTab === "content" ? "active" : ""}
        >
          Content Generator
        </button>
      </div>
      <div className="content">
        {activeTab === "seo" && <SEOAnalyzer />}
        {activeTab === "optimize" && <ContentOptimizer />}
        {activeTab === "topics" && <BlogTopicGenerator />}
        {activeTab === "content" && <ContentGenerator />}
      </div>
    </div>
  );
};

export default App;
