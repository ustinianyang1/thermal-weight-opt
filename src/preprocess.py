import pandas as pd
from pathlib import Path
from .logger import logger
from .config import MATERIALS_DATA, DATA_DIR
from .utils import load_data

class DataPreprocessor:
    def __init__(self, input_file=MATERIALS_DATA):
        self.input_file = Path(input_file)
        self.output_file = DATA_DIR / 'processed' / 'cleaned_materials.csv'
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

    def handle_outliers(self, df):
        """异常值处理逻辑（暂留空）"""
        return df

    def clean_data(self, df):
        """执行数据清洗逻辑"""
        logger.info("开始数据清洗")
        
        # 1. 处理缺失值
        if df.isnull().any().any():
            logger.warning(f"发现缺失值，正在剔除。剩余行数: {len(df.dropna())}")
            df = df.dropna()

        # 2. 异常值处理占位
        df = self.handle_outliers(df)

        # 3. 类型转换：强制数值化
        cols = df.columns.drop('Quality') if 'Quality' in df.columns else df.columns
        df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
        
        return df.dropna()

    def process(self):
        """主处理流程：存在则跳过，不存在则清洗"""
        if self.output_file.exists():
            logger.info(f"直接加载已存在的清洗数据: {self.output_file}")
            return pd.read_csv(self.output_file)

        logger.info("未发现清洗数据，启动预处理流程...")
        data = load_data(self.input_file)
        cleaned_data = self.clean_data(data)
        
        cleaned_data.to_csv(self.output_file, index=False)
        logger.info(f"清洗完成并保存至: {self.output_file}")
        
        return cleaned_data

if __name__ == "__main__":
    DataPreprocessor().process()