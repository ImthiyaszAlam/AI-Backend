# api_caller_async.py
import asyncio
from typing import Optional
import httpx
from mini_logger import MiniLogger

logger = MiniLogger("api_caller", level="DEBUG")

async def fetch(url: str, timeout: int = 10, retries: int = 2) -> Optional[dict]:
    backoff = 0.5
    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(1, retries + 2):
            try:
                logger.debug(f"Attempt {attempt} GET {url}")
                resp = await client.get(url)
                resp.raise_for_status()
                logger.info(f"Success {url} [{resp.status_code}]")
                return resp.json()
            except (httpx.HTTPStatusError, httpx.RequestError) as e:
                logger.error(f"Request failed (attempt {attempt}): {e}")
                if attempt <= retries:
                    await asyncio.sleep(backoff)
                    backoff *= 2
                else:
                    logger.error("Max retries reached.")
                    return None

# quick runner
if __name__ == "__main__":
    url = "https://httpbin.org/get"
    result = asyncio.run(fetch(url))
    print(result)
