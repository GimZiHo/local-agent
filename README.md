# Local Agent

로컬 LLM을 이용해 AI Agent의 기본 구조를 직접 학습하고 구현하는 프로젝트입니다.

Windows 11에서 Ollama로 `qwen3.5:9b`를 실행하고, WSL의 Python에서 Ollama API를 호출합니다.

새 대화방에서 학습을 이어갈 때는 [CLAUDE.md](CLAUDE.md)의 규칙을 따릅니다.

## 현재 구조

```text
사용자
  ↓
Python Application
  ↓
Ollama API (http://172.31.16.1:11434)
  ↓
Qwen3.5:9b
```

Memory는 별도로 관리합니다.

```text
사용자 대화 → Memory 정보 추출 → memory.json 저장
  → 다음 대화의 System Prompt에 전달 → Qwen 추론
```

## 파일 구조

```text
local-agent/
├── CLAUDE.md           # 학습 진행 지침 (새 세션 시작 시 참고)
├── docs/               # 개념별 학습 문서
├── llm.py              # 메인 대화 루프
├── memory.py           # 장기 Memory 저장/병합
├── memory_extract.py   # 대화에서 기억할 정보 추출
├── memory.json         # 실제 기억 데이터 (git 제외)
└── .gitignore
```

## 학습 기록

| # | 주제 | 문서 |
|---|------|------|
| 01 | Ollama 로컬 LLM을 Python에서 호출하기 | [docs/01-ollama-python.md](docs/01-ollama-python.md) |
| 02 | 대화 Context와 System Prompt | [docs/02-context-system-prompt.md](docs/02-context-system-prompt.md) |
| 03 | JSON 기반 장기 Memory와 정보 추출 | [docs/03-long-term-memory.md](docs/03-long-term-memory.md) |
| 04 | Tool Calling 왕복 흐름 (get_current_time) | [docs/04-tool-calling.md](docs/04-tool-calling.md) |
| 05 | 여러 Tool 등록과 실행 분기 (list_files) | [docs/05-multi-tool.md](docs/05-multi-tool.md) |
| 06 | Agent Loop (반복 Tool 호출) | [docs/06-agent-loop.md](docs/06-agent-loop.md) |

## 다음 학습 주제

파일을 읽는 `read_file()` Tool을 추가하고, Agent Loop에서 파일 탐색 → 읽기를 연결합니다.
