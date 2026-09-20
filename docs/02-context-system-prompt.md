# 02. 대화 Context와 System Prompt

## 배운 것
- LLM은 **상태가 없다(stateless)**. 이전 대화를 기억하는 게 아니라, 매번 전체 대화를 다시 보내주는 것이다.
- 그래서 `messages` 리스트에 user/assistant 메시지를 계속 쌓아서 통째로 보낸다.
- `system` 역할 메시지는 맨 앞에 두며, 모델의 역할과 규칙을 지정한다.

## 왜 필요한가
- Context가 없으면 "아까 말한 그거"가 통하지 않는다.
- System Prompt로 말투, 역할, 참고할 배경 정보를 고정할 수 있다. Agent의 성격은 대부분 여기서 결정된다.

## 코드 핵심
```python
messages = [{"role": "system", "content": "너는 사용자와 대화하는 AI 비서다."}]

while True:
    question = input("You > ")
    messages.append({"role": "user", "content": question})

    stream = client.chat(model="qwen3.5:9b", messages=messages, stream=True)

    answer = ""
    for chunk in stream:
        answer += chunk.message.content

    # 모델의 답변도 다시 넣어야 다음 턴에서 기억된다
    messages.append({"role": "assistant", "content": answer})
```

## 막혔던 점 / 해결
- assistant 응답을 `messages`에 다시 넣지 않으면, 모델은 자기가 한 말을 모른다.
- 대화가 길어질수록 매번 보내는 토큰이 늘어난다 → 나중에 요약/압축이 필요해지는 이유.

## 다음
- 프로그램을 껐다 켜도 남는 장기 기억(Memory).
