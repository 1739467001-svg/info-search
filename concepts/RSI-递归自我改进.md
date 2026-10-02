---
title: RSI（递归自我改进 / Recursive Self-Improvement）
date: 2026-09-28
type: 概念
tags: [ai, agi, self-improvement, alphaevolve, safety]
confidence: 高
---

# 💡 RSI（递归自我改进 / Recursive Self-Improvement）

> 整理日期：2026-09-28 ｜ 类型：概念解读 ｜ 置信度：**高**（AlphaEvolve 官方博客与 DGM 论文均实际抓取核实；I.J. Good 史实为公认常识）｜ 关联：`relations.md`
> 一句话总结：**AI 系统改进"它自己"——改进出的更强版本继续用来改进自己，循环复利增强。2025 年 Google DeepMind 的 AlphaEvolve 让这个老思想第一次有了工业级落地：它优化了"制造它自己的工厂"（训练流水线与算力调度）。**

---

## 1. 名词解释（准确版）

**定义：** Recursive Self-Improvement（RSI）指一个人工智能系统把"改进自身"作为任务——修改自己的代码、算法或训练流程，并用改进后的版本继续下一轮改进。

**思想源头（教科书级史实）：** 统计学家 I. J. Good 1965 年提出"超智能机器"（ultraintelligent machine）思想实验：一台超越所有人类智能的机器去设计更好的机器，改进将循环发生——"智能爆炸"（intelligence explosion）由此而来。（本条为广泛转引的经典论述，本轮未在线核验原文链接。）

**排歧义（重要）：**
- 股市技术分析里的 RSI = Relative Strength Index（相对强弱指标），与本概念无关；
- "自进化 / self-evolving / 自我改进 / recursive improvement" 在当下语境常混用，严谨写作中 RSI 特指"改进对象是自身"的闭环。

---

## 2. 2025 年的两大代表项目（均在线核实）

### Google DeepMind — AlphaEvolve（2025-05-14 发布）

- **机制**：进化式编码 agent。Gemini Flash 出广度想法 + Gemini Pro 深度实现 + **自动评估器**验证打分 + 程序数据库保存进化最优解；前作 FunSearch 只能进化单个函数，AlphaEvolve 可进化整个代码库。
- **战绩**：
  - 4×4 复数矩阵乘法 48 次标量乘法，打破 Strassen 1969 年纪录；
  - Borg 数据中心调度优化，**平均回收 Google 全球 0.7% 算力**（生产环境运行一年以上）；
  - Gemini 矩阵乘内核提速 23%，**Gemini 训练时间缩短 1%**；FlashAttention 内核指令级提速至 32.5%；
  - 50+ 数学开放问题：约 75% 重现最优解，约 20% 改进最优（含 11 维吻接数问题新下界 593）。
- **"递归"的准确理解**：它优化了"训练它自己底座模型（Gemini）的流水线"——**间接递归**（改工厂，不是模型直接改自己权重）。

### Darwin Gödel Machine（DGM，arXiv:2505.22954）

- **机制**：agent **直接迭代修改自己的代码**，每次修改用编码基准实证验证；维护一棵不断分叉的"agent 进化树"（达尔文式开放式探索）。区别于理论版 Gödel Machine（需证明改进有益），DGM 只要求实证有效。
- **战绩**：SWE-bench **20.0% → 50.0%**；Polyglot 14.2% → 30.7%。
- **安全措施**：沙箱隔离 + 人类监督（论文明确说明）。

---

## 3. 概念谱系与辨析

| 概念 | 关系/区别 |
|------|-----------|
| 自我博弈（self-play, AlphaZero） | 通过对弈生成训练信号的 RL 前身，"自己练自己"的窄版本 |
| STaR / 自举（bootstrapping） | 用模型自生成数据再训练自己（推理能力自举），不改代码 |
| 持续学习（Continual Learning） | 近亲但不同：CL 关注"学新任务不忘旧"；RSI 关注"改进自身能力" |
| 强化学习（RL） | 自我改进循环常用的引擎（进化搜索/RL 优化） |
| EVAL / 自动评估器 | RSI 的瓶颈组件：判断"确实变好了"必须靠评测，评估失准则进化方向失真（Goodhart） |

---

## 4. 争议与视角

| 视角 | 观点 |
|------|------|
| 快速起飞派（Yudkowsky 等） | RSI 一旦越过一个阈值，能力会指数式脱缰（"FOOM"），人类可能失去控制窗口 |
| 渐进派（Hanson 等） | 改进存在回报递减与工程瓶颈，智能增长更可能是连续渐进而非爆炸 |
| 现实派/工程视角 | 2025 年的"递归"都是间接、局部、被沙箱与人工监督约束的工程优化；将其等同于"天网"是误解 |
| 安全研究界 | 主流安全框架把"失控风险/自主自我改进"列为需评测的关键能力之一 |

---

## 5. 如何理解它（给 AI 开发者）

1. 现阶段的"自进化"= **"LLM 提出变异 + 自动评估器选择 + 数据库积累"的进化搜索**，不是模型觉醒；
2. 想复现小实验：可以做一个"prompt 自己优化 prompt"或"代码 agent 用 benchmark 做适应度函数"的小闭环——这就是 AlphaEvolve 的微缩版；
3. 关键设计点是**评估器**：评估指标偏了，进化会朝着错误方向"优化得很起劲"（呼应库内 EVAL / Goodhart 条目）。

---

## 6. 参考来源（实际抓取成功）

- **Google DeepMind — AlphaEvolve 官方博客**（机制、48 次乘法、0.7% 算力、23% 内核提速、训练时间 -1%、吻接数 593）：https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- **Darwin Gödel Machine 论文**（SWE-bench 20→50%、自改代码机制、沙箱监督）：https://arxiv.org/abs/2505.22954
- **I. J. Good 1965 / FOOM 辩论**：本轮 LessWrong、维基页面被拦截（429/超时），标注为公认史实未附链接

---

## 7. 我的思考（留给自己）

> （我更信"爆炸"还是"渐进"？想拿什么小闭环做一次微缩 RSI 实验？）