import os
import openai
from dotenv import load_dotenv
import base64

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Instantiate the OpenAI client
client = openai.OpenAI(api_key=api_key)

def generate_content(keyword, word_count=500):
    # Define the prompt for content generation
    prompt = f"Write a well-structured article about '{keyword}' with appropriate headings and subheadings. The article should be informative and engaging, with a minimum of {word_count} words."

    # Generate text using OpenAI's Chat Completion API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=word_count * 5,  # Approximate 5 tokens per word
        temperature=0.7,  # Adjust creativity level
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract the generated text
    content = response.choices[0].message.content.strip()

    return content

def generate_blog_topics(keyword, num_topics=5):
    # Define the prompt for generating blog topics
    prompt = f"Generate {num_topics} engaging blog article topics related to '{keyword}'."

    # Generate topics using OpenAI's Chat Completion API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,  # Adjust based on the expected length of topics
        temperature=0.7,  # Adjust creativity level
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract the generated topics
    topics = response.choices[0].message.content.strip().split('\n')

    return topics

def generate_image(prompt, size="1024x1024", format="url"):
    """
    Generate an image based on the given prompt using DALL-E.
    
    :param prompt: A text description of the desired image
    :param size: Size of the image (default "1024x1024")
    :param format: Return format, either "url" or "b64_json" (default "url")
    :return: URL or base64 encoded string of the generated image
    """
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality="standard",
            n=1,
            response_format=format
        )

        if format == "url":
            return response.data[0].url
        elif format == "b64_json":
            return response.data[0].b64_json
        else:
            raise ValueError("Invalid format specified. Use 'url' or 'b64_json'.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Optional: Helper function to save base64 image
def save_base64_image(b64_string, filename):
    """
    Save a base64 encoded image to a file.
    
    :param b64_string: Base64 encoded image string
    :param filename: Name of the file to save the image
    """
    with open(filename, "wb") as image_file:
        image_file.write(base64.b64decode(b64_string))
