from transformers import pipeline

print("Loading model...")
sql_generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)
print("Model loaded ✅")


def generate_sql(user_question):
    prompt = f"""
You are an expert MySQL developer.

Database table:
employees(id, name, department, salary)

Rules:
- Generate ONLY valid MySQL SQL
- Use exact column names only
- If department is mentioned, use WHERE
- Support multiple conditions using AND / OR
- Support ORDER BY, LIMIT, COUNT, AVG, MAX
- Do NOT explain anything

Examples:

Question: Show all employees
SQL: SELECT * FROM employees;

Question: Show employees in IT department
SQL: SELECT * FROM employees WHERE department = 'IT';

Question: Show employees in IT department with salary greater than 50000
SQL: SELECT * FROM employees WHERE department = 'IT' AND salary > 50000;

Question: Show top 5 highest paid employees
SQL: SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

Question: Count employees in HR department
SQL: SELECT COUNT(*) FROM employees WHERE department = 'HR';

Now generate SQL for:
Question: {user_question}
SQL:
"""

    response = sql_generator(
        prompt,
        max_length=150,
        do_sample=False
    )

    sql = response[0]["generated_text"].strip()

    # -------- Post-validation (accuracy control) --------
    q = user_question.lower()

    if "department" in q and "where" not in sql.lower():
        if "it" in q:
            sql = "SELECT * FROM employees WHERE department = 'IT';"
        elif "hr" in q:
            sql = "SELECT * FROM employees WHERE department = 'HR';"

    if "count" in q and "count" not in sql.lower():
        sql = "SELECT COUNT(*) FROM employees;"

    return sql


# -------- Run --------
if __name__ == "__main__":
    question = input("User Question: ")
    sql_query = generate_sql(question)

    print("\nGenerated SQL ✅")
    print(sql_query)
