# 06. Agent Loop

## 배운 것
- Tool 호출이 없는 응답이 나올 때까지 `chat → Tool 실행 → 결과 추가`를 반복한다.
- 한 응답에 `tool_calls`가 여러 개일 수 있어 for문으로 모두 실행한다.
- `max_steps`로 무한 루프를 막는다.

## 왜 필요한가
- "파일 목록 + 현재 시간"처럼 여러 Tool이 필요한 요청을 한 번에 처리하려면 반복이 필요하다.

## 코드 핵심
```python
for step in range(max_steps):
    response = client.chat(model=..., messages=messages, tools=TOOLS, think=False)
    if response.message.tool_calls:
        messages.append(response.message)
        for tool_call in response.message.tool_calls:
            result = TOOL_FUNCTIONS[tool_call.function.name](**tool_call.function.arguments)
            messages.append({"role": "tool", "tool_name": tool_call.function.name, "content": str(result)})
        continue
    return response.message.content
```

## 막혔던 점 / 해결
- 모델이 Tool 결과를 추측하거나 하나만 실행 → System Prompt에 "모든 Tool 실행, 결과 추측 금지" 명시.

## 다음
- 파일 내용을 읽는 `read_file()` Tool 추가.
