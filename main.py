from seo_analyzer import analyze_seo, optimize_content
from content_generator import generate_content, generate_blog_topics
from markdown_converter import convert_markdown_to_html

# Read content from text file
with open('content.txt', 'r') as file:
    content = file.read()

keyword = "dog walking"

# Convert Markdown content to HTML
html_content = convert_markdown_to_html(content)

seo_results = analyze_seo(html_content, keyword)
print(seo_results)
optimized_content = optimize_content(html_content, keyword)
print(optimized_content)

# Generate blog topics
# blog_topics = generate_blog_topics(keyword, num_topics=5)
# print("Blog Topics:")
# for topic in blog_topics:
#     print(f"- {topic}")

# Example usage
# keyword = "dog walking"
# generated_content = generate_content(keyword)
# print(generated_content)