import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from .config import *
from .logger import logger
from .utils import set_seed
from .preprocess import DataPreprocessor
from .visualize import plot_importance, plot_metrics

def main():
    try:
        logger.info("=== 流程启动 ===")
        set_seed(TRAIN_CONF['random_state'])

        # 1. 数据预处理
        data = DataPreprocessor().process()
        X, y = data[FEATURES], data[TARGET]
        X_train, X_test, y_train, y_test = train_test_split(X, y, **TRAIN_CONF)

        # 2. 超参数调优
        logger.info("执行 GridSearchCV 自动调优...")
        grid = GridSearchCV(
            RandomForestRegressor(random_state=TRAIN_CONF['random_state']),
            PARAM_GRID,
            **CV_CONF
        )
        grid.fit(X_train, y_train)
        model = grid.best_estimator_
        logger.info(f"最佳参数选择: {grid.best_params_}")

        # 3. 性能评估
        y_pred = model.predict(X_test)
        metrics = {
            'R2': r2_score(y_test, y_pred),
            'MAE': mean_absolute_error(y_test, y_pred),
            'RMSE': np.sqrt(mean_squared_error(y_test, y_pred))
        }
        for k, v in metrics.items(): logger.info(f"{k}: {v:.4f}")

        # 4. 可视化分析
        plot_importance(model.feature_importances_, FEATURES)
        plot_metrics(metrics)

        # 5. 新材料预测
        new_sample = pd.DataFrame([NEW_MATERIAL_INPUT], columns=FEATURES)
        res = model.predict(new_sample)[0]
        
        logger.info(f"新材料预测 YS 结果: {res:.2f} MPa")
        logger.info("=== 任务已完成 ===")

    except Exception as e:
        logger.error(f"运行失败: {e}")

if __name__ == "__main__":
    main()