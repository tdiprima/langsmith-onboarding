# LangSmith Onboarding - Polly Files

## List of Notebooks and Their Purposes

1. **`polly_langchain.ipynb`**
   - **Purpose**: This notebook sets up a basic question-answering chain for a parrot named Polly. It uses the LangChain framework to integrate a retrieval function (`fake_db_retrieval`) that reads facts from a file (`polly_facts.txt`), a prompt template defining Polly’s behavior, and an OpenAI language model (`gpt-4o-mini`). The chain is tested with a single question: "What sport are you the best at?". It also includes LangSmith tracing setup for monitoring.
   - **Key Features**: Basic chain setup (`prompt | llm`), file-based fact retrieval, and an example invocation.

2. **`polly_traceable.ipynb`**
   - **Purpose**: This notebook builds on `polly_langchain.ipynb` by enhancing the chain with a traceable retrieval step (`fake_db_retrieval_step`) using LangSmith’s `@traceable` decorator. It maintains the same prompt and model setup but structures the chain as `fake_db_retrieval_step | prompt | llm`. It tests the chain with two questions: "What sport are you the best at?" and "What's your favorite sport?". The focus is on improving observability with LangSmith tracing.
   - **Key Features**: Adds traceability to the retrieval step, runs multiple test questions.

3. **`polly_prompt_hub.ipynb`**
   - **Purpose**: This notebook simplifies the setup by pulling a pre-defined prompt (`polly-prompt-1`) from the LangChain hub instead of defining it inline. It uses the same traceable retrieval step and model as `polly_traceable.ipynb`, testing the chain with the question "What do you like to eat?". The purpose appears to be experimenting with external prompt management.
   - **Key Features**: Uses a hub-pulled prompt, otherwise similar to `polly_traceable.ipynb`.

4. **`polly_experiment.ipynb`**
   - **Purpose**: This notebook extends the functionality of the previous ones by adding an evaluation step. It defines the same chain as `polly_traceable.ipynb` (with an inline prompt), tests it with "Do you like animals?", and introduces an evaluation function (`did_polly_respond`) to check if Polly responds. It uses LangSmith’s `evaluate` to run the chain against a dataset (`polly-ground-truth-qa`) and assess performance.
   - **Key Features**: Adds evaluation logic, integrates with a ground truth dataset.

## Should They Be Run in a Particular Order?

- **No strict order is required**, as each notebook (`polly_langchain.ipynb`, `polly_traceable.ipynb`, `polly_prompt_hub.ipynb`, `polly_experiment.ipynb`) is self-contained and can run independently, assuming the necessary dependencies (e.g., `polly_facts.txt`, `.env` file with API keys, and required Python packages) are in place. However, there’s a logical progression in complexity and functionality that suggests a conceptual order for understanding or development purposes:
  1. **`polly_langchain.ipynb`**: Start here to establish the basic chain and understand the core functionality.
  2. **`polly_traceable.ipynb`**: Move to this to see how tracing enhances observability.
  3. **`polly_prompt_hub.ipynb`**: Explore this next to see how external prompts can be integrated.
  4. **`polly_experiment.ipynb`**: Finish with this to add evaluation and assess the chain’s performance.

- **Dependencies and Assumptions**:
  - All notebooks assume access to `polly_facts.txt` and a `.env` file with a `LANGCHAIN_API_KEY` (and possibly an OpenAI API key for `ChatOpenAI`).
  - `polly_prompt_hub.ipynb` requires a prompt named `polly-prompt-1` to exist in the LangChain hub.
  - `polly_experiment.ipynb` requires a dataset named `polly-ground-truth-qa` in LangSmith for evaluation.
