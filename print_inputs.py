from langsmith import traceable

# Pretend this is your fake_db_retrieval_step
@traceable(run_type="retriever")
def fake_db_retrieval_step(question):
    with open('polly_facts.txt', 'r') as file:
        polly_facts = file.read()
    result = {"question": question, "facts": polly_facts}
    print("After fake_db_retrieval_step:", result)  # 🖨️ Checkpoint 1
    return result

# Let's assume this is your prompt (simplified as a template)
prompt_template = "Question: {question}\nFacts: {facts}\nAnswer based on facts."
@traceable(run_type="prompt")
def prompt_step(input_dict):
    formatted_prompt = prompt_template.format(**input_dict)
    print("After prompt, before LLM:", formatted_prompt)  # 🖨️ Checkpoint 2
    return formatted_prompt

# Dummy LLM step (replace with your actual LLM call)
@traceable(run_type="llm")
def llm_step(prompt_text):
    print("LLM received:", prompt_text)  # 🖨️ Checkpoint 3
    return "Fake LLM response: Yes, Polly is awesome."

# Build and run the chain
chain = fake_db_retrieval_step | prompt_step | llm_step
question = "Is Polly cool?"
response = chain.invoke(question)
print("Final response:", response)
