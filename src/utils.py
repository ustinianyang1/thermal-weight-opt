import pandas as pd
import numpy as np
import random
from .logger import logger

def load_data(path):
    # 加载 CSV 数据
    try:
        df = pd.read_csv(path)
        logger.info(f"成功读取数据: {path}")
        return df
    except Exception as e:
        logger.error(f"数据加载异常: {e}"); raise

def set_seed(seed=42):
    # 固定随机种子
    np.random.seed(seed)
    random.seed(seed)
    logger.info(f"系统种子已设为: {seed}")