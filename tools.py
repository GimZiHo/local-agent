from datetime import datetime


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


if __name__ == "__main__":
    print(get_current_time())