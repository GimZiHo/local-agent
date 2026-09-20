# 03. JSON 기반 장기 Memory와 정보 추출

## 배운 것
- Context(단기 기억)는 프로그램을 끄면 사라진다. 파일에 저장해야 **장기 기억**이 된다.
- 대화 전체를 저장하는 게 아니라, LLM에게 "기억할 만한 정보"만 JSON으로 뽑게 시킨다.
- `format="json"`을 주면 모델이 JSON 형식으로만 답하도록 강제할 수 있다.
- 추출된 정보는 기존 memory와 **병합(merge)** 한 뒤, 다음 턴의 System Prompt에 넣는다.

## 왜 필요한가
- 매번 "내 이름은 ~야"를 다시 말하지 않아도 된다.
- Agent가 사용자를 아는 상태로 시작한다. RAG나 벡터 DB로 가기 전의 가장 단순한 형태의 기억이다.

## 코드 핵심
```python
# 1) 추출: LLM을 파서처럼 사용한다
response = client.chat(
    model="qwen3.5:9b",
    messages=[{"role": "user", "content":
        '다음 문장에서 기억할 사용자 정보를 추출해. JSON으로만 답해. '
        '형식은 {"name": "", "technologies": []} 이다.\n\n문장: ' + text}],
    format="json",
)
new_memory = json.loads(response.message.content)

# 2) 병합: 리스트는 중복 제거하며 누적
memory["technologies"] = list(dict.fromkeys(
    memory.get("technologies", []) + new_memory["technologies"]
))

# 3) 주입: System Prompt에 현재 memory를 문자열로 넣는다
system = f"아래는 사용자 정보다. {json.dumps(memory, ensure_ascii=False)}"
```

## 막혔던 점 / 해결
- 프롬프트만으로는 JSON이 깨질 때가 있다 → `format="json"` 옵션으로 해결.
- `memory.json`은 개인 정보이므로 `.gitignore`에 넣는다.

## 다음
- Tool Calling. 첫 번째 툴로 파일을 읽는 `read_file()`부터 시작한다.
