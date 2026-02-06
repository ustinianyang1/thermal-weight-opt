import pathlib

# 路径配置
ROOT = pathlib.Path(__file__).parent.parent
DATA_DIR = ROOT / 'data'
RAW_DATA = DATA_DIR / 'raw' / 'materials.csv'
PROCESSED_DATA = DATA_DIR / 'processed' / 'cleaned_materials.csv'
LOG_DIR, VIS_DIR = ROOT / 'logs', ROOT / 'visualize'

# 训练与随机种子
TRAIN_CONF = {
    'test_size': 0.2,
    'random_state': 42
}

# 随机森林调优范围
PARAM_GRID = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 交叉验证配置
CV_CONF = {
    'cv': 5,
    'n_jobs': -1,
    'verbose': 0
}

# 字段定义
FEATURES = ["P(W)", "V(mm/s)", "H(um)", "T(um)", "Density(%)", "Hardness(HRA)", "E(MPa)", "UTS(MPa)", "EL(%)"]
TARGET = "YS(MPa)"

# 新材料预测输入参数
NEW_MATERIAL_INPUT = [160, 600, 100, 30, 97, 56, 16377, 565, 30]