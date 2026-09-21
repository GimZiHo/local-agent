# 05. 여러 Tool 등록과 실행 분기

## 배운 것
- Tool이 늘어나면 `if name == ...` 대신 `TOOL_FUNCTIONS` 딕셔너리로 이름 → 함수를 매핑한다.
- 모델이 준 `arguments`(dict)를 `tool_function(**arguments)`로 그대로 넘겨 실행한다.
- 모델은 경로 같은 인자를 추측하므로 System Prompt로 기준(`.`)을 알려줘야 한다.

## 왜 필요한가
- Tool을 추가해도 실행 코드를 고치지 않고 딕셔너리에 한 줄만 추가하면 된다.

## 코드 핵심
```python
TOOL_FUNCTIONS = {
    "get_current_time": get_current_time,
    "list_files": list_files,
}

tool_function = TOOL_FUNCTIONS[tool_name]
result = tool_function(**arguments)
```

## 막혔던 점 / 해결
- 모델이 "현재 프로젝트"를 `/`로 해석 → System Prompt에 "경로는 '.' 사용" 명시.

## 다음
- Tool 호출을 한 번이 아니라 반복하는 Agent Loop.
