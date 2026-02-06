from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from .logger import logger
from .config import FEATURE_COLS, TARGET_COL, MODEL_PARAMS, TRAIN_PARAMS
from .utils import load_data, set_seed

def main():
    """
    主函数：材料性能预测
    """
    try:
        logger.info("=== 材料性能预测程序启动 ===")
        
        # 设置随机种子
        set_seed(TRAIN_PARAMS['random_state'])
        
        # 加载数据
        data = load_data()
        
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
        
        # 训练模型
        logger.info(f"训练随机森林模型，参数: {MODEL_PARAMS}")
        model = RandomForestRegressor(
            n_estimators=MODEL_PARAMS['n_estimators'],
            random_state=MODEL_PARAMS['random_state']
        )
        model.fit(X_train, y_train)
        logger.info("模型训练完成")
        
        # 评估模型
        score = model.score(X_test, y_test)
        logger.info(f"模型准确度: {score:.2%}")
        
        # 预测新数据
        logger.info("预测新材料性能")
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
        
        prediction = model.predict(new_material)
        logger.info(f"预测结果: {prediction[0]:.2f} MPa")
        
        logger.info("=== 程序执行完成 ===")
        
    except Exception as e:
        logger.error(f"程序执行失败: {str(e)}")
        raise

if __name__ == "__main__":
    main()
