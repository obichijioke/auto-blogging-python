from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this import
from seo_analyzer import analyze_seo, optimize_content
from content_generator import generate_content, generate_blog_topics
from markdown_converter import convert_markdown_to_html

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes

@app.route('/analyze_seo', methods=['POST'])
def analyze_seo_route():
    data = request.json
    content = data.get('content')
    keyword = data.get('keyword')
    
    html_content = convert_markdown_to_html(content)
    seo_results = analyze_seo(html_content, keyword)
    return jsonify(seo_results)

@app.route('/optimize_content', methods=['POST'])
def optimize_content_route():
    data = request.json
    content = data.get('content')
    keyword = data.get('keyword')
    
    html_content = convert_markdown_to_html(content)
    optimized_content = optimize_content(html_content, keyword)
    return jsonify({'optimized_content': optimized_content})

@app.route('/generate_blog_topics', methods=['GET'])
def generate_blog_topics_route():
    keyword = request.args.get('keyword')
    num_topics = int(request.args.get('num_topics', 5))
    
    blog_topics = generate_blog_topics(keyword, num_topics=num_topics)
    return jsonify({'blog_topics': blog_topics})

@app.route('/generate_content', methods=['POST'])
def generate_content_route():
    data = request.json
    keyword = data.get('keyword')
    
    generated_content = generate_content(keyword)
    return jsonify({'generated_content': generated_content})

if __name__ == '__main__':
    app.run(debug=True)

# The following code is now handled by the Flask routes above
# with open('content.txt', 'r') as file:
#     content = file.read()
# 
# keyword = "dog walking"
# 
# html_content = convert_markdown_to_html(content)
# 
# seo_results = analyze_seo(html_content, keyword)
# print(seo_results)
# optimized_content = optimize_content(html_content, keyword)
# print(optimized_content)