import pandas as pd
from .config import MATERIALS_DATA
from .logger import logger

def load_data(file_path=MATERIALS_DATA):
    """
    加载材料数据
    
    Args:
        file_path: 数据文件路径
    
    Returns:
        pd.DataFrame: 加载的数据
    """
    try:
        logger.info(f"加载数据文件: {file_path}")
        data = pd.read_csv(file_path)
        logger.info(f"成功加载 {data.shape[0]} 行数据")
        return data
    except Exception as e:
        logger.error(f"数据加载失败: {str(e)}")
        raise

def set_seed(seed=42):
    """
    设置随机种子
    
    Args:
        seed: 随机种子值
    """
    import numpy as np
    import random
    np.random.seed(seed)
    random.seed(seed)
    logger.info(f"设置随机种子: {seed}")
