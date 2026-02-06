import matplotlib.pyplot as plt
import numpy as np
import os
from .config import VIS_DIR
from .logger import logger

# 中文显示配置
plt.rcParams.update({'font.sans-serif': ['SimHei'], 'axes.unicode_minus': False})

def _save_and_close(name):
    # 保存图表到指定目录
    os.makedirs(VIS_DIR, exist_ok=True)
    path = VIS_DIR / name
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    logger.info(f"可视化文件已生成: {path}")

def plot_importance(importances, names):
    # 绘制特征重要性排序图
    indices = np.argsort(importances)
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(indices)), importances[indices], align='center')
    plt.yticks(range(len(indices)), [names[i] for i in indices])
    plt.title('RF 特征重要性分析')
    _save_and_close('feature_importance.png')

def plot_metrics(metrics):
    # 绘制模型评估指标柱状图
    plt.figure(figsize=(8, 5))
    keys, values = list(metrics.keys()), list(metrics.values())
    plt.bar(keys, values, color=['skyblue', 'orange', 'green'])
    for i, v in enumerate(values):
        plt.text(i, v, f'{v:.4f}', ha='center', va='bottom')
    plt.title('模型综合性能指标')
    _save_and_close('evaluation_metrics.png')