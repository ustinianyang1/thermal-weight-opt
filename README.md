# 材料性能预测系统

## 项目简介
本项目基于随机森林回归模型，预测材料的屈服强度（YS），通过输入材料的工艺参数和其他性能指标，实现快速准确的性能预测。

## 项目结构

```
thermal-weight-opt/
├── src/                    # 源代码
│   ├── __init__.py
│   ├── logger.py           # 日志管理模块
│   ├── config.py           # 全局配置
│   ├── utils.py            # 工具函数
│   └── main.py             # 主脚本
├── logs/                   # 日志目录
│   └── YYYY-MM-DD.log      # 日志文件（按日期命名）
├── data/                   # 数据目录
│   └── raw/                # 原始数据
│       └── materials.csv   # 材料数据
├── requirements.txt        # 依赖包
└── README.md               # 项目文档
```

## 安装指南

1. **克隆项目**
   ```bash
   git clone <项目地址>
   cd thermal-weight-opt
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

## 使用说明

### 运行预测

```bash
python -m src.main
```

### 自定义预测

修改 `src/main.py` 中的 `new_material` 变量，输入新材料的参数：

```python
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
```

## 日志系统

项目实现了完善的日志系统：

- **日志级别**：[INFO]、[WARNING]、[ERROR]
- **日志输出**：同时输出到终端和日志文件
- **日志文件**：存储在 `logs/` 目录，按日期命名
- **使用示例**：
  ```python
  from src.logger import logger
  
  logger.info("信息日志")
  logger.warning("警告日志")
  logger.error("错误日志")
  ```

## 配置说明

项目配置存储在 `src/config.py` 文件中：

- **数据路径**：管理数据文件位置
- **模型参数**：设置随机森林模型参数
- **训练参数**：设置训练测试集分割参数
- **特征列**：定义用于预测的特征

## 示例运行结果

```
[INFO] === 材料性能预测程序启动 ===
[INFO] 设置随机种子: 42
[INFO] 加载数据文件: D:\python\thermal-weight-opt\data\raw\materials.csv
[INFO] 成功加载 64 行数据
[INFO] 数据前5行：
[INFO]    Sample number  P(W)  V(mm/s)  H(um)  T(um)  Density(%) Quality  Hardness(HRA)       E(MPa)     YS(MPa)    UTS(MPa)      EL(%)
0              1   150      500     80     30       100.0   Holes      54.000000  15251.66667  487.320000  573.933333  29.150810
1              2   150      500    100     30       100.0   Holes      55.000000  15886.70000  490.003333  570.760000  30.310123
2              3   150      500    120     30       100.0   Dense      55.833333  15878.63333  491.380000  564.610000  27.881814
3              4   150      700     80     30       100.0   Dense      54.333333  15495.50000  486.030000  562.196667  32.464308
4              5   150      700    100     30       100.0   Holes      55.233333  16377.36667  494.186667  567.560000  31.225947
[INFO] 特征列: ['P(W)', 'V(mm/s)', 'H(um)', 'T(um)', 'Density(%)', 'Hardness(HRA)', 'E(MPa)', 'UTS(MPa)', 'EL(%)']
[INFO] 目标列: YS(MPa)
[INFO] 分割训练测试集，测试集比例: 0.2
[INFO] 训练集大小: 51, 测试集大小: 13
[INFO] 训练随机森林模型，参数: {'n_estimators': 100, 'random_state': 42}
[INFO] 模型训练完成
[INFO] 模型准确度: 56.70%
[INFO] 预测新材料性能
[INFO] 新材料参数: {'P(W)': 160, 'V(mm/s)': 600, 'H(um)': 100, 'T(um)': 30, 'Density(%)': 97, 'Hardness(HRA)': 56, 'E(MPa)': 16377, 'UTS(MPa)': 565, 'EL(%)': 30}
[INFO] 预测结果: 493.55 MPa
[INFO] === 程序执行完成 ===
```

## 许可证

本项目采用 MIT 许可证。
