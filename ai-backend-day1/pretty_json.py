# pretty_json.py
import json
import sys
from typing import Any
from mini_logger import MiniLogger

logger = MiniLogger("pretty_json")

def pretty_print_json(data: Any, indent: int = 2) -> str:
    try:
        return json.dumps(data, indent=indent, ensure_ascii=False, sort_keys=True)
    except (TypeError, ValueError) as e:
        logger.error(f"Failed to serialize JSON: {e}")
        raise

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python pretty_json.py path/to/file.json")
        sys.exit(2)

    path = sys.argv[1]
    raw = read_file(path)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {path}: {e}")
        sys.exit(1)

    print(pretty_print_json(parsed, indent=2))

if __name__ == "__main__":
    main()
