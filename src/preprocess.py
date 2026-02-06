import pandas as pd
from .logger import logger
from .config import RAW_DATA, PROCESSED_DATA
from .utils import load_data

class DataPreprocessor:
    def handle_outliers(self, df):
        # 异常值处理占位
        return df

    def process(self):
        # 检查缓存文件
        if PROCESSED_DATA.exists():
            logger.info("发现缓存，跳过预处理")
            return pd.read_csv(PROCESSED_DATA)

        logger.info("执行数据清洗...")
        df = load_data(RAW_DATA)
        
        # 删除缺失值
        if df.isnull().any().any():
            df = df.dropna()
        
        # 异常值占位处理
        df = self.handle_outliers(df)
        
        # 强制特征列数值化并保存
        num_cols = df.columns.drop('Quality') if 'Quality' in df.columns else df.columns
        df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')
        df = df.dropna()

        PROCESSED_DATA.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(PROCESSED_DATA, index=False)
        return df