# 项目名称

> 一句话描述项目用途

- **仓库地址**：https://github.com/yourname/your-project
- **作者**：XXX
- **邮箱**：xxx@example.com

## 项目简介

随着大语言模型的广泛应用，其生成内容的安全性问题日益突出。本项目设计并实现了一个**AI聊天内容安全监测系统**，采用双层检测架构：

- **第一层（敏感词过滤）**：基于AC自动机算法的高性能敏感词匹配，支持大规模词库实时检测
- **第二层（AI语义判断）**：调用大语言模型进行语义理解，识别越狱攻击、提示注入等高级威胁

系统支持DeepSeek、通义千问、智谱清言等多种AI模型，并提供完整的可视化监控面板、安全测试中心和对比实验功能。

## 环境与依赖

### 运行环境

| 项目 | 版本 | 说明 |
|------|------|------|
| 操作系统 | Windows 10 / 11 | 开发与测试所用系统 |
| Python | 3.9 - 3.11 | 核心语言版本 |
| GPU |  无 | 无需 GPU 加速 |

### 开源程序与第三方依赖

> 体积较大或需单独安装的程序，请在此列出下载链接与版本。

| 依赖名称 | 使用版本 | 下载链接 | 安装方式 | 说明 |
|----------|----------|----------|----------|------|
| Python | 3.11.0 | https://www.python.org/downloads/ | 官方安装包 | 运行环境 |
| pip | 23.0+ | 随Python安装 | 自动安装 | 包管理器 |

> **注意**：版本号必须填写实际使用的版本，而非"最新版"。请确保与代码兼容。

### Python  依赖

依赖清单文件：
- Python → `requirements.txt`（已包含在本仓库中）


安装命令：
```bash
# Python
pip install -r requirements.txt
pip install pyahocorasick


```

## 配置说明

### API密钥配置（重要）

本系统需要调用大语言模型 API，请在 `app.py` 中配置以下 API Key：

```python
# app.py 第22-38行
MODELS = {
    "deepseek": {
        "name": "DeepSeek",
        "api_key": "你的DeepSeek API Key",   # 请在此填入你的API Key
        "api_url": "https://api.deepseek.com/v1/chat/completions",
        "model_name": "deepseek-chat",
    },
    "qwen": {
        "name": "通义千问",
        "api_key": "你的通义千问 API Key",   # 请在此填入你的API Key
        "api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
        "model_name": "qwen-plus",
    },
    "glm": {
        "name": "智谱清言",
        "api_key": "你的智谱清言 API Key",   # 请在此填入你的API Key
        "api_url": "https://open.bigmodel.cn/api/paas/v4/chat/completions",
        "model_name": "glm-4-flash",
    }
}
```

> **安全提示**：敏感配置（密码、密钥）请使用环境变量
import os
api_key = os.environ.get("DEEPSEEK_API_KEY")
或 `.env` 文件，`.env` 已加入 `.gitignore`。
DEEPSEEK_API_KEY=你的密钥
QWEN_API_KEY=你的密钥
GLM_API_KEY=你的密钥

### 其他关键配置

| 配置项 | 默认值 | 说明 | 配置文件路径 |
|--------|--------|------|-------------|
| `SAMPLING_RATE` | 0.1 (10%) | AI采样率，未命中敏感词时触发AI判断的概率 | `app.py` 第15行 |
| `CURRENT_MODEL` | deepseek | 当前使用的AI模型（可选：deepseek/qwen/glm/siliconflow） | `app.py` 第18行 |
| `SERVER_PORT` | 5000 | Flask服务端口 | `app.py` 末尾 |
| `DATABASE` | database.db | SQLite数据库文件（自动生成） | `app.py` 第440行 |

## 数据集

### 数据集说明

| 数据集名称 | 来源 | 大小 | 格式 | 说明 |
|-----------|------|------|------|------|
| CRiskEval 中文版 | 复旦大学 | 107条 | CSV | 中文安全风险评估数据集 |
| AdvBench | 斯坦福大学 | 520条 | CSV | 英文有害行为基准测试集 |
| 敏感词库 | konsheng/Sensitive-lexicon | 3000+词 | TXT | 多分类中文敏感词库 |

> **体积较大的数据集不纳入 Git 仓库**，请通过外部链接下载后放置到指定目录。
>
> **小部分数据示例应提交到 Git 仓库中**（放置于 `data/samples/` 目录），用于：
> - 让其他开发者无需下载完整数据集即可快速了解数据格式与字段含义
> - 支撑单元测试和本地调试的最小可运行数据
> - 作为数据处理流程的输入示例，方便 Code Review 时对照理解逻辑
>
> 示例数据要求：
> - 条数控制在 5~20 条，文件大小不超过 100KB
> - 需脱敏处理，不得包含真实用户隐私信息
> - 文件命名建议：`sample_<数据集名>.csv` / `sample_<数据集名>.json`

### 数据集下载与放置

```bash
# 1. 创建数据目录
mkdir -p data/advbench
mkdir -p sensitive_words

# 2. 下载 AdvBench 数据集
curl -L "https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/data/advbench/harmful_behaviors.csv" -o data/advbench/harmful_behaviors.csv

# 3. 下载 CRiskEval 中文数据集（手动下载）
# 地址：https://github.com/tjunlp-lab/CRiskEval

# 4. 下载敏感词库（手动下载）
# 地址：https://github.com/konsheng/Sensitive-lexicon/tree/main/Vocabulary
```

数据集目录结构：
```
data/
├── CRiskEval_Chinese.csv          # 中文安全风险评估数据集（107条）
├── advbench/
│   └── harmful_behaviors.csv      # AdvBench 英文测试集（520条）
sensitive_words/                    # 敏感词库目录
├── COVID-19词库.txt               # 疫情相关词汇
├── GFW补充词库.txt                # 墙补充词库
├── 其他词库.txt                   # 其他敏感词
├── 反动词库.txt                   # 反动词汇
├── 广告类型.txt                   # 广告垃圾词
├── 政治类型.txt                   # 政治敏感词
├── 新思想启蒙.txt                 # 敏感思想词汇
├── 暴恐词库.txt                   # 暴恐内容词汇
├── 民生词库.txt                   # 民生敏感词
├── 涉枪涉爆.txt                   # 枪支爆炸物词汇
├── 网易前端过滤敏感词库.txt        # 前端过滤词库
├── 色情类型.txt                   # 色情内容词汇
├── 色情词库.txt                   # 色情词汇
├── 补充词库.txt                   # 补充词汇
└── 贪腐词库.txt                   # 贪污腐败词汇
```

> `data/` 目录已加入 `.gitignore`，但 `data/samples/` 通过 `!data/samples/` 规则**强制纳入版本控制**。

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/yourname/ai-content-safety-system.git
cd ai-content-safety-system

# 2. 安装依赖
pip install -r requirements.txt
pip install pyahocorasick

# 3. 配置 API Key
# 编辑 app.py，填入你的 API Key

# 4. 准备敏感词库
mkdir sensitive_words
# 将下载的词库文件放入 sensitive_words/ 目录

# 5. 启动项目
python app.py
```

## 项目结构

```
ai-content-safety-system/
├── app.py # 主程序（Flask应用）
├── test_cases.py # 测试用例集（7大类70+条）
├── sensitive_words.txt # 基础敏感词库
├── requirements.txt # Python依赖清单
├── database.db # SQLite数据库（自动生成）
├── data/ # 数据集目录
│ ├── CRiskEval_Chinese.csv # CRiskEval中文数据集（107条）
│ └── advbench/ # AdvBench数据集
│ └── harmful_behaviors.csv # AdvBench英文测试集（520条）
├── sensitive_words/ # 扩展词库目录
│ ├── 政治类型.txt # 政治敏感词
│ ├── 暴恐词库.txt # 暴力恐怖词汇
│ ├── 色情词库.txt # 色情低俗词汇
│ ├── 涉枪涉爆.txt # 枪支爆炸物词汇
│ ├── 反动词库.txt # 反动词汇
│ ├── 广告类型.txt # 广告垃圾词
│ ├── 民生词库.txt # 民生敏感词
│ ├── 贪腐词库.txt # 贪污腐败词汇
│ ├── 其他词库.txt # 其他敏感词
│ ├── COVID-19词库.txt # 疫情相关词汇
│ ├── GFW补充词库.txt # 墙补充词库
│ ├── 新思想启蒙.txt # 敏感思想词汇
│ ├── 网易前端过滤敏感词库.txt # 前端过滤词库
│ ├── 色情类型.txt # 色情内容词汇
│ └── 补充词库.txt # 补充词汇
├── templates/ # HTML模板
│ ├── base.html # 基础模板
│ ├── dashboard.html # 仪表盘
│ ├── chat.html # AI聊天
│ ├── logs.html # 安全日志
│ ├── security.html # 安全监控
│ ├── test_dashboard.html # 安全测试
│ ├── experiment.html # 对比实验
│ ├── sampling.html # 采样统计
│ └── settings.html # 系统设置
├── test_api.py # API测试脚本
├── test_base64.py # Base64解码测试
├── test_comparison.py # 对比实验脚本
└── README.md # 本文件
```

