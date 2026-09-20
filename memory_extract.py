import json
from ollama import Client

client = Client(host="http://172.31.16.1:11434")


def extract_memory(text: str) -> dict:
    response = client.chat(
        model="qwen3.5:9b",
        messages=[
            {
                "role": "user",
                "content": (
                    "다음 문장에서 장기적으로 기억할 만한 사용자 정보를 추출해. "
                    "반드시 JSON으로만 답해. "
                    '형식은 {"name": "", "technologies": []} 이다.\n\n'
                    f"문장: {text}"
                ),
            }
        ],
        think=False,
        format="json",
    )

    return json.loads(response.message.content)


if __name__ == "__main__":
    memory = extract_memory("나는 Kotlin도 공부하고 있어.")
    print(memory)