import os
import pathlib

# 项目根目录
PROJECT_ROOT = pathlib.Path(__file__).parent.parent

# 数据路径
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
MATERIALS_DATA = RAW_DATA_DIR / 'materials.csv'

# 日志路径
LOG_DIR = PROJECT_ROOT / 'logs'

# 模型参数
MODEL_PARAMS = {
    'n_estimators': 100,
    'max_depth': None,
    'min_samples_split': 2,
    'min_samples_leaf': 1,
    'random_state': 42
}

# 网格搜索参数
GRID_SEARCH_PARAMS = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 随机搜索参数
RANDOMIZED_SEARCH_PARAMS = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 搜索参数
SEARCH_PARAMS = {
    'cv': 5,
    'n_jobs': -1,
    'verbose': 1
}

# 训练参数
TRAIN_PARAMS = {
    'test_size': 0.2,
    'random_state': 42
}

# 特征列
FEATURE_COLS = [
    "P(W)",
    "V(mm/s)",
    "H(um)",
    "T(um)",
    "Density(%)",
    "Hardness(HRA)",
    "E(MPa)",
    "UTS(MPa)",
    "EL(%)"
]

# 目标列
TARGET_COL = "YS(MPa)"
