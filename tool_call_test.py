from ollama import Client
from tools import GET_CURRENT_TIME_TOOL, get_current_time


client = Client(host="http://172.31.16.1:11434")

messages = [
    {
        "role": "user",
        "content": "지금 몇 시야?",
    }
]

response = client.chat(
    model="qwen3.5:9b",
    messages=messages,
    tools=[GET_CURRENT_TIME_TOOL],
    think=False,
)

print(response.message)

tool_call = response.message.tool_calls[0]

if tool_call.function.name == "get_current_time":
    result = get_current_time()
    print("Tool 실행 결과:", result)

    messages.append(response.message)

    messages.append(
        {
            "role": "tool",
            "tool_name": "get_current_time",
            "content": result,
        }
    )

    final_response = client.chat(
        model="qwen3.5:9b",
        messages=messages,
        tools=[GET_CURRENT_TIME_TOOL],
        think=False,
    )

    print("최종 답변:", final_response.message.content)