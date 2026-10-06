---
title: Vercel 与 AI 工具链（v0 / Eve / Sandboxes）
date: 2026-09-28
type: 专题
tags: [vercel, ai-tools, v0, deployment, agent]
confidence: 高
---

# 📌 Vercel：AI 时代的部署与代理基础设施

> 整理日期：2026-09-28 ｜ 类型：专题调研 ｜ 置信度：**高**（vercel.com 首页/产品页/博客实际抓取 + Bing 交叉核实 "FX/Drive"）｜ 关联：`relations.md`
> 一句话总结：**Vercel 是前端与无服务器部署起家的云平台，2025–2026 年已转型为"Agentic 基础设施"；拳头 AI 产品是 v0（文字生成应用/UI）与 Eve（持久化 Agent 框架），并推出 Run SDK（给 Agent 做评测）等新工具。"Vercel FX"与"Vercel Drive"经多重核实均不存在——你印象里的 "FX" 可能是 v0，"Drive" 最接近的是 Sandboxes 里的 Drives 功能。**

---

## 1. 核实记录（先回答 "FX / Drive"）

| 用户说法 | 核实来源 | 结果 |
|---------|---------|------|
| "vervel" | vercel.com | = **Vercel**，Agentic 云平台 ✅ |
| "Vercel FX" | 官网产品页、博客（最近 10+ 篇）、Bing 精确搜索 | ❌ **不存在**（无官方产品/公告/教程使用该名） |
| "Vercel Drive" | 同上交叉 | ❌ 无该产品；⚠️ 最接近：产品侧边栏 **Sandboxes 下有 "Drives"** 条目（临时计算环境组件，官方文档待核） |

**已核实的 Vercel 产品矩阵（官方产品页）：**

| 分类 | 产品 | 一句话 |
|------|------|--------|
| 部署 | Projects / CDN / Containers / Edge Functions | 看家本领：部署、缓存、容器、边缘计算 |
| AI 生成 | **v0**（v0.dev） | 文字→应用/UI 的 AI 工具，已出 v2 编程式 API |
| Agent | **Eve** | "framework for building durable agents"（持久化 Agent 框架）|
| Agent | Vercel Agent（任务/配方/线程）、Workflows | 平台级自动化编排 |
| 评测 | **Run SDK** | "secure eval for your agents"——给 Agent 做安全评测（2026-08 发布，与库内 EVAL 条目呼应） |
| 模型网关 | **AI Gateway** | 统一接入各家模型（日志/Key 管理）；2026 年自有模型 **Jev** 上线（自称被采纳最快的模型） |
| 环境 | **Sandboxes**（含 **Drives**、Devbox 任务、快照） | 弹性计算/沙盒环境，供 AI 编码代理使用 |
| 数据 | Storage（Postgres/KV/Blob 集成）| 绑定数据库/存储 |
| 安全 | Passport、Firewall、Observability | 身份接入、防火墙、可观测 |

---

## 2. v0 是什么 + 怎么用（重点教学）

**v0** = Vercel 的 AI 应用生成器：输入一句文字（或截图/仓库），它在你描述的沙盒里实时生成可用 UI/应用，带实时预览，一键部署。2026 年 v0 v2 API 开放了"无头（headless）"调用——程序化生成、供 Agent 使用。

### 2.1 Web 用法（零代码路径，5 分钟）
1. 打开 v0.dev，用 GitHub 账号登录；
2. 输入需求，如"给宠物店做一个预约小程序，移动端优先，橙色主题"；
3. 在生成的界面里继续对话修改（"改成网格布局""加上评价功能"）；
4. 满意后点 Deploy（一键部署到 Vercel，自动获得域名）；
5. 后续改动在 v0 对话里继续，或本地克隆仓库开发。

### 2.2 API 用法（开发者路径，2026 新 v2）
```bash
pnpm add v0@latest        # 官方 SDK（已核实博客说明）
```
- 用 prompt / 仓库 / ZIP / 文件创建 chat；
- 支持**流式**看 Agent 的每一步（改文件、调工具、跑命令）；
- 预览可 iframe 嵌入你自己的页面；一键部署到 Vercel；
- 可通过 **MCP、AI SDK 工具、或 Eve** 接入你自己的 Agent 流程；
- 典型场景：CI/脚本/Webhook 触发自动生成 UI、白标应用生成器、"Agent 交付可用应用而不是代码片段"。

### 2.2 实例演算：让 v0 API 生成一个 TODO 应用
```
① 服务器路由保护 API Key（不要放前端）
② 调 createChat(prompt="做一个响应式 TODO 应用，支持拖拽排序")
③ 订阅流式事件：观察 file edit / tool call / bash 事件
④ 完成后取预览 token → iframe 嵌进部署页面给用户看
⑤ 一键 deploy → 返回 url
⑥ 后续某步"加入暗色模式"→ 追加消息 → 继续生成
```
（流程基于官方 API 发布说明构造，参数细节以官方文档为准。）

---

## 4. Sandboxes 与 Drives（疑云解答 + 用法）

- **Sandboxes**：Vercel 提供的云端可委托环境（如临时 devbox），配合 AI 编码代理（Claude Code / Cursor 等）远程操作项目；官方侧边栏把它列为 "Drives、Devbox 任务、快照" 一组功能——**"Drives" 最可能是用户听到的 "Drive"**：沙盒的驱动盘/会话持久空间（⚠️ 官方 docs 404 未直核，待补）。
- **典型工作流**：Vercel 项目 → 创建 Sandbox → 用 AI 编程工具连接 → 代理在其中改代码/跑测试 → 状态和文件持久在 Drives → 可快照回滚 → 完成后部署。

---

## 5. 概念辨析

| 对 | 区别 |
|----|------|
| v0 vs Lovable / Bolt | 同为 AI 建站三雄；v0 强在 React/Next.js 生态与 Vercel 部署一体化 |
| Vercel vs Netlify / Cloudflare Pages | 同为 JAMstack 部署；Vercel 的 AI/Agent 层（v0/Eve/AI Gateway）明显更厚 |
| Vercel vs 自建服务器 | 托管省运维 vs 自控；成本与锁定效应是常被吐槽点 |
| Vercel 的 Run SDK vs 库内 EVAL | 平台级 Agent 评测 vs 自建评测体系——互补对照（待研究） |

---

## 6. 争议与注意

- **供应商锁定与费用**：v0/托管服务极方便，但长期成本高于自建（社区共识）；
- **生成代码质量**：AI 生成的 UI 适合 MVP/原型，复杂业务逻辑仍需工程化重构；
- **"FX/Drive"的记忆错位**：建议以官方产品页为准；若在第三方教程见过 "FX"，大概率是 v0 或第三方封装名。

---

## 7. 参考来源（实际抓取成功）

- Vercel 官网（首页，Eve/Passport/Containers 定义）：https://vercel.com/
- Vercel 产品总览页（完整产品列表 + Sandboxes"Drives"条目）：https://vercel.com/products
- Vercel 博客（10+ 篇最新文章，含 v0 v2 API、Run SDK、Jev）：https://vercel.com/blog
- v0 新 API 公告（实例演算依据）：https://vercel.com/blog/introducing-the-new-v0-api
- Bing 交叉核实（Vercel FX / Vercel Drive 不存在）：https://cn.bing.com/search?q=%22Vercel+FX%22
- ⚠️ 未核：Sandbox "Drives" 官方文档页 404，标注待补

---

## 8. 我的思考（留给自己）

> （我想用 v0 自动生成什么？还是先跑一次 Run SDK 给手里 Agent 做评测？）