# 04. Tool Calling 왕복 흐름

## 배운 것
- LLM은 Tool을 직접 실행하지 않는다. "어떤 Tool을 어떤 인자로 쓸지"만 판단한다.
- 실제 실행은 Python이 하고, 결과를 `role: tool` 메시지로 다시 LLM에 넘긴다.
- 흐름: 사용자 → LLM(tool_calls) → Python 실행 → tool 결과 → LLM 최종 답변

## 왜 필요한가
- LLM은 현재 시각처럼 모델 밖의 정보를 알 수 없다. Tool로 외부 세계와 연결해야 Agent가 된다.

## 코드 핵심
```python
response = client.chat(model=..., messages=messages, tools=[GET_CURRENT_TIME_TOOL], think=False)
tool_call = response.message.tool_calls[0]

if tool_call.function.name == "get_current_time":
    result = get_current_time()
    messages.append(response.message)  # tool_calls가 담긴 assistant 메시지
    messages.append({"role": "tool", "tool_name": "get_current_time", "content": result})
    final = client.chat(model=..., messages=messages, tools=[GET_CURRENT_TIME_TOOL], think=False)
```

- Tool 정의(`tools.py`)는 JSON Schema 형태: name / description / parameters.

## 다음
- `read_file()` Tool 추가, 여러 Tool 중 선택 및 반복 호출(Agent Loop).
