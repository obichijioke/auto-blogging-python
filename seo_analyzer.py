import textstat
from bs4 import BeautifulSoup

def analyze_seo(content, keyword):
    # Analyze keyword density
    keyword_density = content.lower().count(keyword.lower()) / len(content.split()) * 100

    # Analyze readability
    readability_score = textstat.flesch_reading_ease(content)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Extract meta description and headings
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_description['content'] if meta_description else ''
    headings = [heading.get_text() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]

    # Suggest improvements
    suggestions = []
    if keyword_density < 1:
        suggestions.append("Increase the keyword density.")
    if readability_score < 60:
        suggestions.append("Improve readability for better user engagement.")
    if not meta_description:
        suggestions.append("Add a meta description.")
    if not headings:
        suggestions.append("Add appropriate headings and subheadings.")

    return {
        "keyword_density": keyword_density,
        "readability_score": readability_score,
        "meta_description": meta_description,
        "headings": headings,
        "suggestions": suggestions
    }

def optimize_content(content, keyword):
    # Example optimization: Add meta description and headings
    optimized_content = f"<meta name='description' content='This article is about {keyword}.'>\n"
    optimized_content += f"<h1>{keyword}</h1>\n"
    optimized_content += content

    return optimized_content
