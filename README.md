---
title: AI SQL Feedback Agent
emoji: 🤖
colorFrom: indigo
colorTo: purple
sdk: gradio
app_file: app_sql.py
python_version: "3.13.5"
---

# 🤖 AI SQL Feedback Agent

[![Gradio App](https://img.shields.io/badge/Gradio-App-ff7c00)](https://YOUR-GRADIO-SPACE-LINK-HERE)
[![LangChain](https://img.shields.io/badge/LangChain-v0.1-green)](https://www.langchain.com/)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3100/)

This project is a Generative AI application that acts as an "AI SQL Coach." It uses LangChain and a Large Language Model (LLM) to provide expert, nuanced feedback on a user's SQL queries, helping them learn *why* their solution is right or wrong.

This app was built to demonstrate proficiency in Generative AI, prompt engineering, and LLM orchestration with LangChain.

## 🚀 The Problem

Most online coding platforms (like LeetCode or Prachub) only tell you if your SQL query is "Accepted" or "Wrong Answer." This is a poor learning experience. Users don't know if their query was *almost* right, inefficient, or just badly formatted.

Getting expert feedback is expensive and not scalable.

## ✨ Features

This agent solves the problem by providing instant, structured feedback based on three criteria:

1.  **Correctness:** Does the query actually solve the given problem?
2.  **Efficiency:** Is the query optimal? Does it use an inefficient `SUBQUERY` when a `JOIN` is better? Does it use `WHERE` instead of `ON` in a join?
3.  **Readability:** Is the query well-formatted? Does it use clear aliases?

## 🛠️ Tech Stack

* **AI:** Generative AI (GPT-4o-mini via OpenAI API)
* **Orchestration:** LangChain (PromptTemplates, LLMChains)
* **App:** Gradio (for the web interface)
* **Core:** Python

## 💻 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/abduldatawork/sql-coach-app.git
    cd sql-coach-app
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment:**
    * Create a file named `.env` in the root directory.
    * Add your OpenAI API key to this file:
        ```text
        OPENAI_API_KEY="sk-..."
        ```

4.  **Run the Gradio app:**
    ```bash
    gradio app_sql.py
    ```
    (Or `python app.py`)
