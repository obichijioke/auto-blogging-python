import markdown

def convert_markdown_to_html(markdown_content):
    """
    Convert Markdown content to HTML.

    Args:
        markdown_content (str): The Markdown content to convert.

    Returns:
        str: The converted HTML content.
    """
    html_content = markdown.markdown(markdown_content)
    return html_content