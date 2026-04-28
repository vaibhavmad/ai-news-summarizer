import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from send_email_script import send_email
from news_fetch import get_news
from llm_prompt import get_llm_prompt

load_dotenv()
article_text = get_news()
llm_prompt = get_llm_prompt()
final_llm_prompt = llm_prompt + '\n\n' +  article_text
print(final_llm_prompt)

message = "Subject: Today's iPhone News\n\n"

LLM_API_KEY = os.getenv('LLM_API_KEY')
llm_model = init_chat_model(model='gpt-5-mini', model_provider='openai', api_key=LLM_API_KEY)
llm_response = llm_model.invoke(final_llm_prompt)

message += llm_response.content + '\n'
message = message.encode('utf-8')
send_email(message)