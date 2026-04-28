# AI News Summarizer

An AI-powered pipeline that fetches latest news articles, extracts key insights using an LLM, and delivers a concise summary via email.

## 🚀 Overview
This project automates the process of staying updated with news by:
- Fetching articles from a news API  
- Cleaning and structuring the data  
- Generating a summarized view using an LLM  
- Sending the summary via email  

It demonstrates real-world backend concepts like API integration, prompt engineering, modular code design, and automation.

---

## 🛠 Tech Stack
- Python  
- Requests (API calls)  
- LangChain (LLM integration)  
- SMTP (email delivery)  
- dotenv (environment variable management)  

---

## 📂 Project Structure
```
.
├── main.py                # Orchestrates the full pipeline
├── news_fetch.py         # Fetches and processes news data
├── llm_prompt.py         # Contains prompt template
├── send_email_script.py  # Handles email sending
├── .env                  # Environment variables (not committed)
├── .gitignore
├── pyproject.toml
└── README.md             # Project documentation
```
---

## ⚙️ How It Works
1. Fetch news articles from API  
2. Clean and combine article data  
3. Pass structured input to LLM  
4. Generate concise summary  
5. Send summary via email  

---

## 🔑 Environment Variables
Create a .env file and add:

NEWS_API_KEY=your_news_api_key LLM_API_KEY=your_llm_api_key GMAIL_SEND_USER_NAME=your_email GMAIL_APP_PASSWORD=your_app_password GMAIL_RECEIVE_USER_NAME=receiver_email

---

## ▶️ Running the Project
bash uv run main.py 
(or use python main.py depending on your setup)

---

## ⚠️ Current Limitations
- News API free plan may return delayed data  
- No retry mechanism for API failures (yet)  
- Basic logging using print statements  
- Topic is currently hardcoded  

---

## 🔄 Future Improvements
- Add retry logic for API calls  
- Introduce logging instead of print  
- Support dynamic topics (user input)  
- Add scheduling (cron / cloud deployment)  
- Improve error handling and monitoring  

---

## 🧠 Key Learnings
- Building end-to-end data pipelines  
- Working with external APIs  
- Prompt design for LLMs  
- Modularizing Python code  
- Handling real-world edge cases  

---

## 📌 Notes
- .env is excluded from version control for security  
- .idea/ and virtual environments are ignored  

---

## 📄 License
This project is for learning and experimentation purpose