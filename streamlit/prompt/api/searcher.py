import os

import openai
from transformers import AutoTokenizer
from sentence_transformers import SentenceTransformer
import os
openai.api_key = os.environ["OPENAI_API_KEY"]


def query_response(text, query):
    # Load SBERT model and tokenizer
    model_name = 'sentence-transformers/bert-base-nli-mean-tokens'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    sbert_model = SentenceTransformer(model_name)

    # Encode text and query into embeddings
    text_embeddings = sbert_model.encode([text])
    query_embeddings = sbert_model.encode([query])

    # Use the top result as context for OpenAI's chat API
    k = 5  # number of results to retrieve
    sims = text_embeddings @ query_embeddings.T
    idx = sims.argmax()
    context = text.split('.')[idx] + '.'

    # Call OpenAI's chat API to generate response
    prompt = f"{context}\nUser: {query}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    ).choices[0].text.strip()

    return response