import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import requests
from send_email_script import send_email


load_dotenv()
# steps:
# * Choose news source (API or RSS for AI-related news)
# * Fetch articles (with timeout + basic validation)
# * Add retry mechanism (handle temporary failures)
# * Clean + filter data (remove nulls, trim text, avoid duplicates)
# * Set up OpenAI model (keep model configurable)
# * Design prompt (clear instructions for summarization)
# * Generate summaries
# * Handle non-text responses / edge cases
# * Format output (clean email body, readable structure)
# * Send email (SMTP setup)
# * Validate email success / failure
# * Store secrets in .env
# * Add error handling (try/except with meaningful messages)
# * Add basic logging (even simple print logs)
# * Test locally (different scenarios: no news, API fail, etc.)
# * Deploy (PythonAnywhere or similar)
# * Schedule daily run
# * Push to GitHub (without .env)

# topic_is = input('Enter the topic')
API_KEY = os.getenv('NEWS_API_KEY')
url = ("https://gnews.io/api/v4/search?"
    "q=iphone"
    f"&lang=en&apikey={API_KEY}"
       )
response = requests.get(url)
data = response.json()
articles = data['articles']
article_list = []
for index, article in enumerate(articles):
    article_title = f"{index + 1}. {article['title']}"
    article_description = article['description']
    complete_article = article_title + '\n' + article_description + '\n\n'
    article_list.append(complete_article)

article_text = ''
for article in article_list:
    article_text += article + '\n'

message = "Subject: Today's iPhone News\n\n"
llm_prompt = f"""
You are an AI news assistant.
You will be given a list of news articles. Each article contains a title and a short description.
Your task:
1. Identify the most important themes or developments across all articles.
2. Combine related news into a single coherent summary.
Output format:
- Paragraph 1: Most important / latest developments (high priority news)
- Paragraph 2: Other relevant updates (secondary news)
Rules:
- Do NOT repeat the same news
- Do NOT list articles individually
- Do NOT add any information not present in the input
- Keep it concise and readable
Articles: {article_text}
"""
LLM_API_KEY = os.getenv('LLM_API_KEY')
llm_model = init_chat_model(model='gpt-5-mini', model_provider='openai', api_key=LLM_API_KEY)
llm_response = llm_model.invoke(llm_prompt)
# print(llm_response.content)

message += llm_response.content + '\n'
message = message.encode('utf-8')
send_email(message)