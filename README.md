# Langchain_Project

# 🍴 Restaurant Name & Menu Generator  

A **Streamlit web app** built with **LangChain** that generates creative **restaurant names** and **menu items** using **Large Language Models (LLMs)**.  

---

## 🚀 Features  

- Generate unique **restaurant names** based on cuisine, theme, or style.  
- Create **menu items** with descriptions tailored to the restaurant concept.  
- Interactive **Streamlit UI** for seamless user experience.  
- Powered by **LangChain + OpenAI LLMs**.  

---

## 🏗️ Architecture  

```mermaid
flowchart TD
    User[👨‍🍳 User Input] -->|Cuisine, Theme| Streamlit[🖥️ Streamlit App]
    Streamlit --> LangChain[🔗 LangChain Framework]
    LangChain --> OpenAI[🤖 LLM API]
    OpenAI --> Streamlit
    Streamlit --> Output[📜 Restaurant Name & Menu]