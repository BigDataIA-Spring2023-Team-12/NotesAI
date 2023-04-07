import openai
import os
from decouple import config

openai.api_key = config("OPENAI_API_KEY")

def summarize_text(input_text):
    """
    Summarizes the given input text using GPT-3.5 via the OpenAI API.

    Args:
        input_text (str): The text to be summarized.

    Returns:
        str: The summarized text.
    """
    prompt = (f"summarize array using points in markdown language:\n\n{input_text}\n\n"
              f"Summary:")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    summarized_text = response.choices[0].text.strip()

    return summarized_text
