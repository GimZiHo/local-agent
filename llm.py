import json
from ollama import Client
from memory_extract import extract_memory
from memory import load_memory, save_memory, merge_memory

memory = load_memory()

print("Memory:", memory)

client = Client(host="http://172.31.16.1:11434")

def build_system_prompt(memory: dict) -> str:
    memory_text = json.dumps(memory, ensure_ascii=False)

    return (
        "너는 사용자와 대화하는 AI 비서다. "
        "아래는 사용자에 대해 장기적으로 저장된 정보다. "
        f"{memory_text} "
        "이 정보를 참고해서 사용자의 질문에 답하라. "
        "user 역할의 메시지는 사용자가 한 말이고, "
        "assistant 역할의 메시지는 네가 한 말이다."
    )

memory_text = json.dumps(memory, ensure_ascii=False)
messages = [
    {
        "role": "system",
        "content": build_system_prompt(memory),
    }
]

while True:
    question = input("You > ")

    if question == "exit":
        break

    new_memory = extract_memory(question)
    print("추출된 Memory:", new_memory)

    memory = merge_memory(memory, new_memory)

    save_memory(memory)

    messages[0]["content"] = build_system_prompt(memory)

    messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    print(messages)

    stream = client.chat(
        model="qwen3.5:9b",
        messages=messages,
        think=False,
        stream=True,
    )

    print("Qwen > ", end="", flush=True)

    answer = ""

    for chunk in stream:
        text = chunk.message.content
        answer += text
        print(text, end="", flush=True)

    print()

    messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )