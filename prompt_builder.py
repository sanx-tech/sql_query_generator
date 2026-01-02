DB_SCHEMA = """
Database: company_db

Table: employees
Columns:
- emp_id (INT)
- name (VARCHAR)
- department (VARCHAR)
- salary (INT)
- joining_date (DATE)
"""
def build_prompt(user_question):
    prompt = f"""
You are an expert SQL developer.

Convert the following English question into a valid MySQL SQL query.

Rules:
- Use only the given database schema
- Do not assume any extra tables or columns
- Return ONLY the SQL query, nothing else

{DB_SCHEMA}

User Question:
{user_question}
"""
    return prompt
if __name__ == "__main__":
    question = "Find average salary of each department"
    prompt = build_prompt(question)
    print(prompt)
