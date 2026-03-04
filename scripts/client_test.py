import os
import argparse
import yaml
from openai import OpenAI

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", "-p", default="qwen2.5-3b-instruct-q8_0", help="Profile to use for testing")
    args = parser.parse_args()

    profile_path = f"profiles/{args.profile}.yaml"
    if not os.path.exists(profile_path):
        print(f"Profile {profile_path} not found. Using defaults.")
        api_base = "http://localhost:11434/v1"
        api_key = "ollama"
        model_name = "qwen2.5-3b-instruct-q8_0"
    else:
        with open(profile_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
            api_base = config.get("api_base", "http://localhost:11434/v1")
            api_key = config.get("api_key", "ollama")
            model_name = config.get("model_name", "qwen2.5-3b-instruct-q8_0")

    client = OpenAI(
        base_url=api_base,
        api_key=api_key
    )

    print(f"[*] Testing model: {model_name} at {api_base}")

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "너는 유능한 AI 어시스턴트야."},
                {"role": "user", "content": "안녕! 오늘 날씨 어때?"}
            ]
        )
        print("\n[Response]:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"\n[!] Error during request: {e}")

if __name__ == "__main__":
    main()
