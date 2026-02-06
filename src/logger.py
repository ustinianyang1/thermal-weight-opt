import logging
import os
from datetime import datetime
from .config import LOG_DIR

class SimpleLogger:
    def __init__(self):
        # 确保日志目录存在
        os.makedirs(LOG_DIR, exist_ok=True)
        log_file = LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.log"
        
        # 配置基础日志格式
        logging.basicConfig(
            level=logging.INFO,
            format='%(message)s',
            handlers=[logging.FileHandler(log_file, encoding='utf-8'), logging.StreamHandler()]
        )
        self.log = logging.getLogger("MPPS")

    def info(self, msg): self.log.info(f"[INFO] {msg}")
    def warning(self, msg): self.log.warning(f"[WARNING] {msg}")
    def error(self, msg): self.log.error(f"[ERROR] {msg}")

logger = SimpleLogger()