import matplotlib.pyplot as plt
import numpy as np
import os
from .logger import logger

# 设置中文字体，解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

class Visualizer:
    def __init__(self, output_dir='visualize'):
        """
        可视化工具初始化
        
        Args:
            output_dir: 可视化结果输出目录
        """
        self.output_dir = output_dir
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
    
    def plot_feature_importance(self, feature_importance, feature_names, filename='feature_importance.png'):
        """
        绘制特征重要性图
        
        Args:
            feature_importance: 特征重要性数组
            feature_names: 特征名称列表
            filename: 输出文件名
        """
        try:
            logger.info("开始绘制特征重要性图")
            
            # 创建图形
            plt.figure(figsize=(12, 8))
            
            # 排序特征重要性
            sorted_indices = np.argsort(feature_importance)
            sorted_importance = feature_importance[sorted_indices]
            sorted_features = [feature_names[i] for i in sorted_indices]
            
            # 绘制水平条形图
            plt.barh(range(len(sorted_importance)), sorted_importance, align='center')
            plt.yticks(range(len(sorted_importance)), sorted_features, fontsize=10)
            plt.xlabel('重要性', fontsize=12)
            plt.ylabel('特征', fontsize=12)
            plt.title('随机森林模型特征重要性', fontsize=14, fontweight='bold')
            plt.tight_layout()
            
            # 保存图形
            output_path = os.path.join(self.output_dir, filename)
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            logger.info(f"特征重要性图已保存到: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"绘制特征重要性图失败: {str(e)}")
            raise
    
    def plot_evaluation_metrics(self, metrics, filename='evaluation_metrics.png'):
        """
        绘制评估指标图
        
        Args:
            metrics: 评估指标字典
            filename: 输出文件名
        """
        try:
            logger.info("开始绘制评估指标图")
            
            # 创建图形
            plt.figure(figsize=(10, 6))
            
            metric_names = list(metrics.keys())
            metric_values = list(metrics.values())
            
            # 绘制条形图
            plt.bar(metric_names, metric_values, color=['blue', 'green', 'orange'])
            plt.xlabel('评估指标', fontsize=12)
            plt.ylabel('值', fontsize=12)
            plt.title('模型评估指标', fontsize=14, fontweight='bold')
            
            # 在条形上添加数值
            for i, v in enumerate(metric_values):
                plt.text(i, v + 0.01, f'{v:.4f}', ha='center', fontsize=10)
            
            plt.tight_layout()
            
            # 保存图形
            output_path = os.path.join(self.output_dir, filename)
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            logger.info(f"评估指标图已保存到: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"绘制评估指标图失败: {str(e)}")
            raise

# 创建全局可视化实例
visualizer = Visualizer()
