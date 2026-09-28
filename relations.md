# 🕸️ 知识关系图谱（Relational Map）

> 这个文件记录所有研究过的主题，以及它们之间的关系。
> 每研究完一个新主题，我会：① 加一个节点；② 指明它和已有节点的关系（包含/基于/区别于/延伸出…）。
> **实线 = 已研究主题的实际关联；虚线 = 尚未研究、后续待展开的关联。**

```mermaid
graph LR
    EVAL["💡 EVAL<br/>LLM 评测"]:::done
    J["💡 LLM-as-a-Judge<br/>LLM 当裁判"]:::done
    BOOK["📖 现代思维工具 100 讲<br/>万维钢·音频课"]:::done
    BAY["💡 贝叶斯推理<br/>Bayes' Theorem"]:::done

    EVAL -->|评分器之一| J
    BAY -.->|区别于| FREQ["频率学派统计<br/>待研究"]
    J -.->|区别于,推理期 vs 训练期| RM["Reward Model 奖励模型<br/>待研究"]
    J -.->|更准但更贵| HMAN["人类评估 Human Eval<br/>待研究"]
    EVAL -.->|横向关联| BENCH["Benchmark 基准<br/>待研究"]
    EVAL -.->|延伸| AGENT["Agent 评测<br/>如 SWE-bench"]
    EVAL -.->|应用场景| RAG["RAG 检索增强<br/>待研究"]
    EVAL -.->|实践理念| EDD["评测驱动开发<br/>待研究"]
    J -.->|工程落地| TOOL["Promptfoo / LangSmith / OpenAI Evals<br/>待研究"]

    BOOK -->|涵盖·核心工具| BAY
    BOOK -.->|涵盖| FWK["心智模型 / 思维工具<br/>待研究"]
    BOOK -.->|涵盖| ANTF["反脆弱<br/>待研究"]
    BOOK -.->|延伸阅读| TBOOK["《思考，快与慢》等认知书<br/>待研究"]
    BAY -.->|应用到 AI 工程| EVAL

    classDef done fill:#e6f4ea,stroke:#34a853,stroke-width:2px;
    classDef td fill:#fef7e0,stroke:#f9ab00,stroke-width:1px,stroke-dasharray: 4 3;
    class EVAL,J,BOOK,BAY done;
    class FREQ,RM,HMAN,BENCH,AGENT,RAG,EDD,TOOL td;
    class FWK,ANTF,TBOOK td;
```

> 说明：实线 = 已研究关联；虚线 = 待研究潜在关联。节点内容对应下方表格。

---

## 节点清单（已收录）

| 关键词 | 类型 | 一句话 | 文档 | 收录日期 |
|--------|------|--------|------|----------|
| EVAL | 💡 概念 | 给大模型应用写"测试"，衡量 AI 输出的好坏 | [concepts/EVAL.md](concepts/EVAL.md) | 2026-09-27 |
| LLM-as-a-Judge | 💡 概念 | 用更强的大模型按评分标准给 AI 输出打分 | [concepts/LLM-as-Judge.md](concepts/LLM-as-Judge.md) | 2026-09-27 |
| 现代思维工具 100 讲 | 📖 书籍 | 万维钢音频课程：思维工具的系统目录（非纸质书） | [<span>books/现代思维工具100讲.md</span>](books/现代思维工具100讲.md) | 2026-09-27 |
| 贝叶斯推理 | 💡 概念 | 先验 × 证据 → 后验，信念按比例更新的方法论 | [concepts/贝叶斯推理.md](concepts/贝叶斯推理.md) | 2026-09-27 |

## 关系清单（边）

| 来源 | 关系 | 目标 | 说明 |
|------|------|------|------|
| EVAL | 包含 **评分器** → | LLM-as-Judge | 最重要评分器（已收录） |
| LLM-as-Judge | **区别于**（推理期 vs 训练期）→ | Reward Model | 训练期打分器（待展开） |
| LLM-as-Judge | **参照基准** → | 人类评估 | 人类是最准确基准（待展开） |
| EVAL | **区别于** → | Benchmark | 自建评测 vs 公开基准（待展开） |
| EVAL | **延伸应用** → | Agent 评测 | SWE-bench 等（待展开） |
| EVAL | **应用场景** → | RAG 评测 | faithfulness 等指标（待展开） |
| EVAL | **实践理念** → | 评测驱动开发 | 写用例→跑评测→迭代（待展开） |
| LLM-as-Judge | **工程落地** → | Promptfoo / LangSmith / OpenAI Evals | 三大框架内置（待展开） |
| 现代思维工具 100 讲 | **涵盖·核心工具** → | **贝叶斯推理** | 概率思维一讲的核心（已收录） |
| 现代思维工具 100 讲 | **涵盖** → | 心智模型 / 反脆弱等 | 课程工具目录（待展开） |
| 贝叶斯推理 | **区别于** → | 频率学派统计 | 先验 vs 长期频率（待展开） |
| 贝叶斯推理 | **应用到** → | LLM 评测（EVAL） | 概率视角的校准思想（浅关联，已标注） |

---

## 待研究队列（虚线节点，后续激活）

**AI 工程线：** Reward Model / 人类评估 / Benchmark / Agent 评测 / RAG 评测 / 评测驱动开发 / 评测工具对比 / 频率学派统计
**认知线（来自思维课）：** 心智模型清单 / 反脆弱 / 《思考，快与慢》/ 第一性原理（如提到）

---
*本文件在每次新增主题时自动维护。*