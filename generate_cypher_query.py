import ollama

def generate_response(user_prompt:str):
    # Use the generate function for a one-off prompt
    
    # print(result['response'])

    prompt = f"""You are a Neo4j Cypher expert.

    Your task is to generate a Cypher query that INSERTS knowledge into a Neo4j database.

    STRICT RULES:

    1. Output ONLY valid Cypher.
    2. Do NOT include explanations.
    3. Do NOT use markdown.
    4. Use MERGE instead of CREATE.
    5. Use ONLY the schema provided below.

    The prompt is {user_prompt}

    """

    result = ollama.generate(model='gpt-oss:20b-cloud', prompt=prompt)

    return result['response']