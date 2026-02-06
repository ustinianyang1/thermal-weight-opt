import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, name=__name__, log_dir='logs'):
        self.name = name
        self.log_dir = log_dir
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # 确保日志目录存在
        os.makedirs(log_dir, exist_ok=True)
        
        # 生成日志文件名（包含日期）
        today = datetime.now().strftime('%Y-%m-%d')
        log_file = os.path.join(log_dir, f'{today}.log')
        
        # 清除现有处理器
        if self.logger.handlers:
            for handler in self.logger.handlers:
                self.logger.removeHandler(handler)
        
        # 创建文件处理器
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # 定义日志格式（只包含三种前缀）
        formatter = logging.Formatter('%(message)s')
        
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message):
        """记录信息级别的日志"""
        self.logger.info(f"[INFO] {message}")
    
    def warning(self, message):
        """记录警告级别的日志"""
        self.logger.warning(f"[WARNING] {message}")
    
    def error(self, message):
        """记录错误级别的日志"""
        self.logger.error(f"[ERROR] {message}")

# 创建全局日志实例
logger = Logger()

# 日志分级标准和使用示例
"""
日志分级标准：
1. [INFO]：记录正常运行信息，如程序启动、数据加载、模型训练进度等
2. [WARNING]：记录可能的问题，如参数异常、数据格式警告等
3. [ERROR]：记录严重错误，如文件不存在、模型训练失败等

使用示例：
from logger import logger

logger.info("程序启动")
logger.warning("参数值超出推荐范围")
logger.error("文件读取失败")
"""
