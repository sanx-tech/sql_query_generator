LLM-Based SQL Query Generator
📌 Project Overview

The LLM-Based SQL Query Generator converts natural language questions into accurate MySQL queries using a Large Language Model (LLM).
This project improves query accuracy using prompt engineering, few-shot learning, and rule-based validation.

Example:

User Input: Show employees in IT department with salary greater than 50000
Generated SQL:
SELECT * FROM employees WHERE department = 'IT' AND salary > 50000;

🎯 Key Features

Converts English → SQL

Supports multiple SQL commands

WHERE

AND / OR

ORDER BY

LIMIT

COUNT / AVG / MAX

Uses local LLM (FLAN-T5) – no paid API required

Reduces hallucinations

Schema-aware SQL generation

Interview & resume ready project

🛠️ Tech Stack

Python 3.9

Hugging Face Transformers

FLAN-T5 (google/flan-t5-base)

MySQL (optional for execution)

📂 Project Structure
sql_query_generator/
│
├── llm_sql_generator.py     # Main application file
├── README.md                # Project documentation

⚙️ Installation & Setup
1️⃣ Install Dependencies
pip install transformers torch sentencepiece

▶️ How to Run
python llm_sql_generator.py


Enter your question when prompted.

🧪 Sample Inputs & Outputs
Example 1

Input

Show all employees


Output

SELECT * FROM employees;

Example 2

Input

Show employees in IT department


Output

SELECT * FROM employees WHERE department = 'IT';

Example 3

Input

Show top 5 highest paid employees


Output

SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

🔍 How It Works (Workflow)

User enters a natural language question

Prompt provides:

Table schema

Rules

Example queries

LLM identifies intent + conditions

SQL query is generated

Post-validation fixes missing clauses

Final SQL is displayed

🧠 Concepts Used

Large Language Models (LLM)

Prompt Engineering

Few-shot Learning

Intent Detection

Entity Extraction

Hallucination Reduction

Rule-based Validation

❗ Limitations

Works best for single-table queries

JOIN queries need extension

SQL execution not enabled by default

🚀 Future Enhancements

Add JOIN query support

Execute SQL directly in MySQL

Build Streamlit UI

Add user authentication

Add SQL injection protection

📌 Resume Description (Ready to Use)

Built an LLM-based SQL Query Generator that converts natural language queries into accurate MySQL commands using prompt engineering, few-shot learning, and rule-based validation to reduce hallucinations.

👤 Author

Santhosh
BE – Electronics and Communication Engineering
Aspiring Data Scientist / AI Engineer