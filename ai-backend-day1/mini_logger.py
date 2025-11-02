# mini_logger.py
from datetime import datetime
from typing import Optional

class MiniLogger:
    def __init__(self, name: str, level: str = "INFO"):
        self.name = name
        self.level = level

    def _log(self, level: str, msg: str):
        ts = datetime.utcnow().isoformat()
        print(f"{ts} [{level}] {self.name}: {msg}")

    def info(self, msg: str):
        if self.level in ("INFO", "DEBUG"):
            self._log("INFO", msg)

    def debug(self, msg: str):
        if self.level == "DEBUG":
            self._log("DEBUG", msg)

    def error(self, msg: str):
        self._log("ERROR", msg)
