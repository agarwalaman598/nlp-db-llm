from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

with open("../models/prompt.txt") as f:
    SYSTEM_PROMPT = f.read()

def generate_sql(question):
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question + "\nReturn ONLY SQL query."}
        ],
        temperature=0,
        max_tokens=200
    )

    sql = completion.choices[0].message.content.strip()

    # remove markdown if model returns ```sql
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql

