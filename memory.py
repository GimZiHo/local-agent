import json


MEMORY_FILE = "memory.json"


def load_memory() -> dict:
    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(memory: dict) -> None:
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, ensure_ascii=False, indent=2)

def merge_memory(memory: dict, new_memory: dict) -> dict:
    if new_memory.get("name"):
        memory["name"] = new_memory["name"]

    if new_memory.get("technologies"):
        memory["technologies"] = list(
            dict.fromkeys(
                memory.get("technologies", [])
                + new_memory["technologies"]
            )
        )

    return memory