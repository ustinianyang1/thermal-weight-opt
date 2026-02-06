# 材料性能预测系统

## 项目简介

本项目基于随机森林回归模型，预测材料的屈服强度（YS），通过输入材料的工艺参数和其他性能指标，实现快速准确的性能预测。

## 项目结构

```text
thermal-weight-opt/
├── src/                    # 源代码
│   ├── __init__.py
│   ├── logger.py           # 日志管理模块
│   ├── config.py           # 全局配置
│   ├── utils.py            # 工具函数
│   ├── main.py             # 统一入口
│   ├── preprocess.py       # 数据清洗模块
│   └── visualize.py        # 可视化模块
├── logs/                   # 日志目录
│   └── YYYY-MM-DD.log      # 日志文件
├── data/                   # 数据目录
│   ├── raw/                # 原始数据
│   │   └── materials.csv
│   └── processed/          # 处理后的数据
│       └── cleaned_materials.csv
├── visualize/              # 可视化结果
│   ├── feature_importance.png
│   └── evaluation_metrics.png
├── requirements.txt        # 依赖包
├── README.md               # 项目文档
├── .gitignore              # Git 忽略文件
└── .gitattributes          # Git 属性配置

```

## 安装指南

1. **克隆项目**
```bash
git clone <项目地址>
cd thermal-weight-opt

```

2. **安装 Git LFS** (如果未安装)
```bash
# Windows
git lfs install

# macOS
brew install git-lfs
git lfs install

# Linux
sudo apt-get install git-lfs
git lfs install

```

3. **拉取数据文件**
```bash
git lfs pull

```

4. **安装依赖**
```bash
pip install -r requirements.txt

```

## 使用说明

### 运行预测

```bash
python -m src.main

```

### 自定义预测参数

修改 `src/config.py` 中的 `NEW_MATERIAL_INPUT` 变量，输入新材料的参数：

```python
NEW_MATERIAL_INPUT = [160, 600, 100, 30, 97, 56, 16377, 565, 30]

```

---

## 核心功能特性

### 1. 数据预处理与清洗

* **模块**：`src/preprocess.py`
* **功能**：自动检测和处理缺失值，进行数据类型检查转换，并将结果保存至 `data/processed/`。
* **优化**：如果发现清洗后的数据，会跳过清洗流程，直接加载清洗后的数据，提高运行效率。

### 2. 模型评估指标

* **评估标准**：
* **R2（决定系数）**：评估模型解释方差的能力。
* **MAE（平均绝对误差）**：评估预测值与真实值的平均绝对差异。
* **RMSE（均方根误差）**：评估预测值与真实值的均方根差异。

### 3. 特征重要性分析

* **模块**：`src/visualize.py`
* **功能**：提取随机森林特征重要性，生成可视化图表并保存至 `visualize/` 目录。

### 4. 模型自动调优

* **实现**：使用 `GridSearchCV` 进行网格搜索。
* **参数范围**：涵盖 `n_estimators`、`max_depth`、`min_samples_split`、`min_samples_leaf` 等关键超参数。
* **输出**：自动选择最佳参数组合，并在日志中输出。

### 5. 大文件管理 (Git LFS)

* **配置**：`*.csv` 文件使用 Git LFS 管理，确保仓库轻量化，提高克隆和推送速度。
* **说明**：由于数据文件较大，当前未上传到远程仓库，需要使用 `git lfs pull` 拉取数据文件。

---

## 系统配置

### 日志系统

* **级别**：[INFO]、[WARNING]、[ERROR]
* **输出**：同时输出到终端和 `logs/` 目录下的日期命名的日志文件中。
* **调用示例**：
```python
from src.logger import logger
logger.info("信息日志")

```

### 全局配置 (`src/config.py`)

* **管理内容**：数据路径映射、随机森林初始参数、训练测试集比例、特征列定义等。

---

## 示例运行结果

```text
[INFO] === 流程启动 ===
[INFO] 系统种子已设为: 42
[INFO] 执行数据清洗...
[INFO] 成功读取数据: D:\python\thermal-weight-opt\data\raw\materials.csv
[INFO] 执行 GridSearchCV 自动调优...
[INFO] 最佳参数选择: {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 200}
[INFO] R2: 0.5729
[INFO] MAE: 6.6964
[INFO] RMSE: 10.5812
[INFO] 可视化文件已生成: D:\python\thermal-weight-opt\visualize\feature_importance.png
[INFO] 可视化文件已生成: D:\python\thermal-weight-opt\visualize\evaluation_metrics.png
[INFO] 新材料预测 YS 结果: 493.45 MPa
[INFO] === 任务已完成 ===

```

## 许可证

本项目采用 MIT 许可证。

---