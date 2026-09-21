from ollama import Client

from tools import (
    GET_CURRENT_TIME_TOOL,
    LIST_FILES_TOOL,
    TOOL_FUNCTIONS,
)


client = Client(host="http://172.31.16.1:11434")

TOOLS = [
    GET_CURRENT_TIME_TOOL,
    LIST_FILES_TOOL,
]

def run_agent(question: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "너는 Tool을 사용할 수 있는 AI Agent다. "
                "현재 작업 디렉터리가 프로젝트 루트다. "
                "사용자가 '현재 프로젝트', '프로젝트', '현재 디렉터리'라고 말하면 "
                "list_files의 path에는 반드시 '.'을 사용하라. "
                "'/'를 사용하지 마라. "
                "사용자의 요청에 Tool이 필요한 경우 반드시 Tool을 사용하라. "
                "여러 작업을 요청했다면 필요한 Tool을 모두 실행하라. "
                "Tool 결과를 추측하거나 placeholder를 만들지 마라. "
                "Tool이 반환한 값을 사실 그대로 사용하라."
            ),
        },
        {
            "role": "user",
            "content": question,
        },
    ]

    max_steps = 5

    for step in range(max_steps):

        response = client.chat(
            model="qwen3.5:9b",
            messages=messages,
            tools=TOOLS,
            think=False,
        )

        if response.message.tool_calls:
            messages.append(response.message)

            for tool_call in response.message.tool_calls:
                tool_name = tool_call.function.name
                arguments = tool_call.function.arguments

                tool_function = TOOL_FUNCTIONS[tool_name]
                result = tool_function(**arguments)

                print("Tool 실행:", tool_name)
                print("Tool 결과:", result)

                messages.append(
                    {
                        "role": "tool",
                        "tool_name": tool_name,
                        "content": str(result),
                    }
                )

            continue

        return response.message.content

    else:
        return "Agent가 최대 실행 횟수에 도달했습니다."

if __name__ == "__main__":
    answer = run_agent(
        "현재 프로젝트의 파일 목록을 보여주고, 지금 시간도 알려줘."
    )

    print("최종 답변:", answer)