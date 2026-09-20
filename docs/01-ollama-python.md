# 01. Ollama 로컬 LLM을 Python에서 호출하기

## 배운 것
- Ollama는 로컬에서 LLM을 띄우고 HTTP API(기본 11434 포트)로 노출해주는 런타임이다.
- `ollama` 파이썬 패키지의 `Client`로 그 API를 호출한다.
- `stream=True`로 두면 토큰이 생성되는 대로 조각(chunk) 단위로 받는다.

## 왜 필요한가
- API 키나 요금 없이, 내 노트북 안에서 Agent를 실험할 수 있다.
- Windows에서 Ollama가 돌고 코드는 WSL에 있으므로, localhost가 아니라 **Windows 호스트 IP**를 지정해야 한다.

## 코드 핵심
```python
from ollama import Client

client = Client(host="http://172.31.16.1:11434")

stream = client.chat(
    model="qwen3.5:9b",
    messages=[{"role": "user", "content": "안녕"}],
    think=False,    # 추론(thinking) 출력 끄기
    stream=True,
)

for chunk in stream:
    print(chunk.message.content, end="", flush=True)
```

## 막혔던 점 / 해결
- WSL에서 `localhost:11434`로는 연결되지 않는다. WSL 입장에서 Windows는 별도 호스트라서 호스트 IP(`172.31.16.1`)를 써야 한다.
- 이 IP는 재부팅 시 바뀔 수 있다. 안 되면 `ip route`의 default gateway를 확인한다.
- 스트리밍 출력은 `flush=True`가 없으면 버퍼에 쌓여 한 번에 나온다.

## 다음
- 여러 번의 질문을 하나의 대화로 이어지게 만드는 Context 유지.
