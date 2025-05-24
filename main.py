from inspect_ai import eval
from src.task import biolab_blackmail

if __name__ == "__main__":
    # Evaluate the biolab blackmail task using different models
    models = [
        "openrouter/qwen/qwen3-235b-a22b",
        "openrouter/openai/gpt-4o-2024-11-20",
        "openrouter/google/gemini-flash-1.5",
        "openrouter/meta-llama/llama-3.1-70b-instruct",
        "openrouter/openai/gpt-4.1",
        "openrouter/deepseek/deepseek-chat-v3-0324",
        "openrouter/deepseek/deepseek-r1",
        "openrouter/anthropic/claude-3.5-haiku",
        "openrouter/anthropic/claude-3.7-sonnet",
        "openrouter/anthropic/claude-3.7-sonnet:thinking",
        "openrouter/google/gemini-2.5-pro-exp-03-25",
        "openrouter/google/gemini-2.5-flash-preview",
        "openrouter/google/gemini-2.5-flash-preview:thinking",
        "openrouter/openai/o4-mini-high",
        "openrouter/openai/o4-mini",
        "openrouter/openai/gpt-4.1-nano",
        "openrouter/openai/o1",
        "openrouter/openai/o1-preview",
        "openrouter/google/gemini-2.5-flash-preview",
        "openrouter/google/gemini-2.5-pro-preview",
        "openrouter/anthropic/claude-3.7-sonnet",
        "openrouter/google/gemini-2.0-flash-lite-001",
        "openrouter/deepseek/deepseek-r1-distill-qwen-32b",
        "openrouter/qwen/qwen-2.5-72b-instruct"
    ]
    
    eval(biolab_blackmail(), model=models[0])