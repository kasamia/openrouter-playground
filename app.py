import os
import sys

import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o")


def main():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("请先设置 OPENROUTER_API_KEY 环境变量。", file=sys.stderr)
        sys.exit(1)

    prompt = " ".join(sys.argv[1:]).strip() or "你好！请用一句话介绍你自己。"
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/kasamia/openrouter-playground",
            "X-Title": "OpenRouter Playground",
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    print(data["choices"][0]["message"]["content"])


if __name__ == "__main__":
    main()
