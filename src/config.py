import os

LLM_API_URL = os.getenv(
    "LLM_API_URL",
    "https://llm-internal.softex:9001/v1"
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "qwen3.5:9b-q4_K_M"
)