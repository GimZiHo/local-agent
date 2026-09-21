import os
from datetime import datetime


def list_files(path: str) -> list[str]:
    return os.listdir(path)

def get_current_time() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


GET_CURRENT_TIME_TOOL = {
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "현재 날짜와 시간을 반환한다.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
}

LIST_FILES_TOOL = {
    "type": "function",
    "function": {
        "name": "list_files",
        "description": "지정한 경로의 파일과 디렉터리 목록을 반환한다.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "조회할 디렉터리 경로"
                }
            },
            "required": ["path"]
        }
    }
}

TOOL_FUNCTIONS = {
    "get_current_time": get_current_time,
    "list_files": list_files,
}

if __name__ == "__main__":
    print(get_current_time())
    print(list_files("."))