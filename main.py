from inspect_ai import eval
from src.task import biolab_blackmail

if __name__ == "__main__":
    # Evaluate the biolab blackmail task using different models
    models = [
        "openrouter/deepseek/deepseek-chat-v3-0324",
        "openrouter/google/gemini-2.0-flash-lite-001",
        "openrouter/google/gemini-2.5-pro-exp-03-25:free",
        "openrouter/deepseek/deepseek-r1-distill-qwen-32b",
        "openrouter/qwen/qwen-2.5-72b-instruct"
    ]
    
    eval(biolab_blackmail(), model=models[-1])