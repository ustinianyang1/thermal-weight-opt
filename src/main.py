from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np
from .logger import logger
from .config import FEATURE_COLS, TARGET_COL, MODEL_PARAMS, TRAIN_PARAMS, GRID_SEARCH_PARAMS, SEARCH_PARAMS
from .utils import load_data, set_seed
from .preprocess import DataPreprocessor
from .visualize import visualizer

def main():
    """
    主函数：材料性能预测
    """
    try:
        logger.info("=== 材料性能预测程序启动 ===")
        
        # 设置随机种子
        set_seed(TRAIN_PARAMS['random_state'])
        
        # 数据清洗
        logger.info("=== 数据清洗 ===")
        preprocessor = DataPreprocessor()
        data = preprocessor.process()
        
        # 显示数据前几行
        logger.info("数据前5行：")
        logger.info(data.head().to_string())
        
        # 准备特征和目标
        X = data[FEATURE_COLS]
        y = data[TARGET_COL]
        logger.info(f"特征列: {FEATURE_COLS}")
        logger.info(f"目标列: {TARGET_COL}")
        
        # 分割训练测试集
        logger.info(f"分割训练测试集，测试集比例: {TRAIN_PARAMS['test_size']}")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=TRAIN_PARAMS['test_size'], 
            random_state=TRAIN_PARAMS['random_state']
        )
        logger.info(f"训练集大小: {X_train.shape[0]}, 测试集大小: {X_test.shape[0]}")
        
        # 自动调优
        logger.info("=== 模型自动调优 ===")
        logger.info(f"网格搜索参数: {GRID_SEARCH_PARAMS}")
        logger.info(f"搜索配置: {SEARCH_PARAMS}")
        
        grid_search = GridSearchCV(
            estimator=RandomForestRegressor(random_state=TRAIN_PARAMS['random_state']),
            param_grid=GRID_SEARCH_PARAMS,
            **SEARCH_PARAMS
        )
        
        grid_search.fit(X_train, y_train)
        
        # 获取最佳模型和参数
        best_model = grid_search.best_estimator_
        best_params = grid_search.best_params_
        logger.info(f"最佳参数: {best_params}")
        logger.info(f"最佳交叉验证分数: {grid_search.best_score_:.4f}")
        
        # 评估模型
        logger.info("=== 模型评估 ===")
        y_pred = best_model.predict(X_test)
        
        # 计算评估指标
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        
        logger.info(f"R2 (决定系数): {r2:.4f}")
        logger.info(f"MAE (平均绝对误差): {mae:.4f} MPa")
        logger.info(f"RMSE (均方根误差): {rmse:.4f} MPa")
        
        # 特征重要性分析
        logger.info("=== 特征重要性分析 ===")
        feature_importance = best_model.feature_importances_
        feature_importance_dict = dict(zip(FEATURE_COLS, feature_importance))
        logger.info(f"特征重要性: {feature_importance_dict}")
        
        # 可视化特征重要性
        visualizer.plot_feature_importance(feature_importance, FEATURE_COLS)
        
        # 绘制评估指标
        metrics = {
            'R2': r2,
            'MAE': mae,
            'RMSE': rmse
        }
        visualizer.plot_evaluation_metrics(metrics)
        
        # 预测新数据
        logger.info("=== 新材料性能预测 ===")
        new_material = pd.DataFrame({
            "P(W)": [160],
            "V(mm/s)": [600],
            "H(um)": [100],
            "T(um)": [30],
            "Density(%)": [97],
            "Hardness(HRA)": [56],
            "E(MPa)": [16377],
            "UTS(MPa)": [565],
            "EL(%)": [30]
        })
        logger.info(f"新材料参数: {new_material.to_dict('records')[0]}")
        
        prediction = best_model.predict(new_material)
        logger.info(f"预测结果: {prediction[0]:.2f} MPa")
        
        logger.info("=== 程序执行完成 ===")
        
    except Exception as e:
        logger.error(f"程序执行失败: {str(e)}")
        raise

if __name__ == "__main__":
    main()
