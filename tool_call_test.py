from ollama import Client
from tools import (
    GET_CURRENT_TIME_TOOL,
    LIST_FILES_TOOL,
    TOOL_FUNCTIONS,
)

client = Client(host="http://172.31.16.1:11434")

messages = [
    {
        "role": "system",
        "content": (
            "현재 작업 디렉터리가 프로젝트 루트다. "
            "사용자가 현재 프로젝트 또는 현재 디렉터리를 말하면 "
            "경로로 '.'을 사용하라."
        ),
    },
    {
        "role": "user",
        "content": "지금 몇 시야?",
    },
]

response = client.chat(
    model="qwen3.5:9b",
    messages=messages,
    tools=[
        GET_CURRENT_TIME_TOOL,
        LIST_FILES_TOOL,
    ],
    think=False,
)

print(response.message)

tool_call = response.message.tool_calls[0]

tool_name = tool_call.function.name
arguments = tool_call.function.arguments

tool_function = TOOL_FUNCTIONS[tool_name]

result = tool_function(**arguments)

print("Tool 실행 결과:", result)

messages.append(response.message)

messages.append(
    {
        "role": "tool",
        "tool_name": tool_name,
        "content": str(result),
    }
)

final_response = client.chat(
    model="qwen3.5:9b",
    messages=messages,
    tools=[
        GET_CURRENT_TIME_TOOL,
        LIST_FILES_TOOL,
    ],
    think=False,
)

print("최종 답변:", final_response.message.content)