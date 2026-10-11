---
title: TypeSafe AI（企业调查：公司 / Jev / System One 模型）
date: 2026-10-11
type: 专题
tags: [typesafe-ai, jev, system-one, ai-company, decision-model, 企业调查]
confidence: 高
---

# 📌 TypeSafe AI（企业调查与信息查询）

> 整理日期：2026-10-11 ｜ 类型：专题调研 · 企业调查 ｜ 置信度：**高**（官网 / 官方文档 / 官方博客 / GitHub API / OpenRouter API / a16z 公告 / arXiv 论文原文 多源交叉；仅"$870M 融资额"为官方单源，已单独标注）｜ 关联：`relations.md`
> 一句话总结：**TypeSafe AI 是旧金山 AI 实验室，由前 OpenAI 研究员、InstructGPT 合著者 Diogo Almeida 创立，隐身两年后于 2026-09-15 发布"System One 决策模型"Jev——不做聊天、不生成文本，只接收"状态 + 类型化问题"并返回带校准置信度的结构化答案（Choice / Score / Noul）；上线 3 天被 a16z 称为"万亿 token"级采纳，2026-10 初 a16z 宣布领投（官方自述 $870M / $7.5B 估值）。**

---

## 0. 核实速览（关键说法 × 来源 × 状态）

| 关键说法 | 核实来源 | 状态 |
|---------|---------|------|
| 公司存在，旧金山，做 Jev 决策模型 | 官网 typesafe.ai + GitHub 组织 + a16z 公告 | ✅ 多源一致 |
| 创始人 Diogo Almeida（founder & CEO，前 OpenAI） | 官方博客 + a16z 公告 + 百度百科（摘要） | ✅ 多源 |
| 他是 GPT-4 论文贡献者 / InstructGPT 合著者 | arXiv 2303.08774 原文 PDF（grep 到作者名单） | ✅ 一手论文核实 |
| Jev 发布于 2026-09-15 | Vercel 博客（"introduced September 15"）+ npm 0.6.0 时间戳 + CSDN | ✅ 三方吻合 |
| 上架 Vercel AI Gateway（09-18），"Gateway 史上采纳最快" | Vercel 官方博客（2026-09-18） | ✅ 一手 |
| 上架 OpenRouter：`typesafe/jev-1.13`（$0.042/M、64K 上下文、uptime 100%） | OpenRouter API 实取 | ✅ 一手 |
| a16z 领投 | a16z 官方公告（2026-10-09，署名人含 Casado / Andreessen） | ✅ 一手 |
| $870M / $7.5B 估值 / Sequoia、DCVC 跟投 / Casado 入董事会 | 官方博客"TypeSafe A raises Series AI" | ⚠️ **官方单源自述**，a16z 公告未披露金额，未找到第三方媒体报道 |
| 财富 500 客户占比 | 官方博客"三分之一" vs a16z 公告"25%" | ⚠️ 两处口径不一致 |
| "零幻觉 / Zero Hallucinations" | 官网营销语 vs 官方文档"校准不保证单条答案正确" | ⚠️ 话术需打折理解（见 §7） |
| Cloudflare Workers AI 上架 `typesafe/jev` | CSDN 文章称有；Cloudflare 目录页未找到（重定向 `?unavailable=jev`） | ❌ 未证实，暂按"无"处理 |
| 官方博客"194 倍快 / 445 倍便宜" | 官网首页 + Vercel 博客转述 | ⚠️ 官方自评口径（见 §7 数字对账） |
| console / evals 子站可访问 | 本机（中国网络）访问返回 451 | ⚠️ 网络/合规拦截，未能核验 |

---

## 1. 公司档案（Fact Sheet）

| 项目 | 内容 | 来源 |
|------|------|------|
| 公司名 | TypeSafe AI（GitHub 组织 `typesafe-ai`，X 账号 `@typesafeai`） | 官网 / gh API |
| 定位 | "an AI lab building machine-native intelligence infrastructure for automation, designed to make decisions within software"（为自动化构建机器原生智能基础设施，让决策发生在软件内部） | 官网原文 |
| 总部 | 旧金山（官网 "Made in SF. With Love."；gh 组织地区 United States） | 官网 / gh API |
| 创始人 | Diogo Almeida（founder & CEO）：前 OpenAI 研究员，官方称其"helped build the methods that made language models useful at following instructions"（参与塑造了让语言模型学会遵循指令的方法）；GPT-4 技术报告贡献者、InstructGPT 论文合著者 | 官方博客 / a16z / arXiv |
| 隐身期 | "After two years in stealth"（约 2024 年中起）；GitHub 组织创建于 2024-05-28，与"两年"吻合 | 官方博客 / gh API |
| 发布 | Jev 于 2026-09-15 首发（early access）；2026-09-18 上架 Vercel AI Gateway | Vercel 博客 / npm 时间戳 |
| 融资 | A 轮：a16z 领投（公告 2026-10-09），官方博客自述 **$870M、估值 $7.5B**，Sequoia、DCVC 与天使跟投，Martin Casado 加入董事会 | a16z 公告（领投）✅ / 官方博客（金额）⚠️ |
| 产品 | Jev 1.13（System One 决策模型）、Jev Router（模型/推理强度路由器） | 官方文档 / OpenRouter |
| 分发 | 自有 API（api.typesafe.ai）、Vercel AI Gateway、OpenRouter；SDK：Python / JS | 多源 |
| 官方仓库 | 12 个公开仓库（skills 2654★、system-one-adapter-python 387★、sdk-python 281★、sdk-js 273★ 等） | gh API 实取 |
| 商业联系 | sales@typesafe.ai；企业版支持 ZDR（零数据保留） | 官方 legal 页 |
| 同名辨析 | ⚠️ 老牌 "Typesafe Inc."（2011 年成立，Scala/Akka 背后的公司，2016 年更名 Lightbend）与 TypeSafe AI **无任何关系**。GitHub 旧组织 `typesafehub` 现名 "Lightbend (Typesafe archive)"，搜索 "Typesafe" 极易混淆 | gh API 实取 |

**信息查询提示**：搜 "TypeSafe" 会同时命中 ①老 Lightbend（Scala/Akka）②本仓库此条（AI 公司）③大量 SEO 教程站（见 §4.3）；搜 "Jev" 还会命中人名与其它项目，建议用 `typesafe.ai` 域名或 `"TypeSafe AI" Jev` 组合词检索。

---

## 2. 产品：Jev 与 System One 模型

### 2.1 定位：给软件用的"判断节点"，不是聊天模型

官方定义：System One 模型是"a new class of frontier models built to make fast, structured decisions that software can use directly"（一类直接供软件使用、做快速结构化决策的前沿模型）。Jev 是其中第一个。

| 维度 | 传统 LLM | Jev（System One） |
|------|---------|------------------|
| 输出 | 自由文本（需解析 JSON） | **类型化决策**：选项 + 概率分布 + 置信度，无文本、无解析 |
| 延迟（官方口径） | 示例 8.566s | 示例 0.114s；区间 70–500ms |
| 成本（官方口径） | 示例 $0.013880/次 | 示例 $0.000081/次；**$0.042 / 百万输入 token，输出免费** |
| 幻觉 | 存在（自由生成） | 结构上"不可幻觉"（输出被约束为枚举/分值/概率），但**判断本身仍可能错** |
| 用途 | 对话、写作、写代码 | 代码里的判断节点：路由、打分、护栏、核对 |
| 训练目标 | 对齐人类偏好（RLHF） | **校准概率**（RLCD，见 §2.3） |

官方的一句概括："Send state and typed questions; get structured answers your code can use directly."（发状态和类型化问题，拿代码可直接使用的结构化答案。）

### 2.2 三种原语（Question Primitives）

| 原语 | 问什么 | 返回 | 典型用途 |
|------|--------|------|---------|
| **Choice** | 从给定选项里选（最多 255 项） | choice + 各选项概率 + confidence | 分诊、意图识别、下一步动作 |
| **Score** | 按有序量表打分（2–10 级） | score + 概率分布 + confidence | 紧急度、风险、质量评分 |
| **Noul** | 是非判断 | noul（0–1 的"是"概率，无 confidence 字段） | 护栏核对、事实核验 |

三种原语可**混在同一次调用**里；官方强调问题之间"并行且相互隔离地"被评估，"Adding questions barely changes the response time"（加问题几乎不增加响应时间），且多问题"不产生 context-rot"。

### 2.3 机制拆解（三个子系统）

**① 新架构 + 并行采样器（Parallel Sampler）**
官方称 Jev 用了"a new model architecture, a new sampler, and a new training algorithm"。与 LLM 逐 token 顺序生成不同，Jev 的采样器**一次前向并行产出全部答案**（"generates all outputs in a single query rather than token-by-token"）。这是它 70–500ms 延迟与"输出免费"的成本结构来源：答案空间被约束在有限类型上（Choice 基数上限 255，更高基数走两段式）。
旁证：其 GitHub 组织 fork 了 **LLaDA**（Large Language **Diffusion** Models 官方实现）与 vLLM——扩散式并行解码是业界实现"并行采样"的已知路线之一（此为观察推断，非官方声明）。

**② RLCD 训练（Reinforcement Learning for Calibrated Decisions）**
官方明确对比 RLHF/RLVR：RLHF 优化"人类偏好"（后果是 mode dropping、过度自信、不可靠，需要人在环），RLCD 优化"**认知诚实的概率**"——即在 System One 任务上给出与真实结果相符的校准概率。官方博客称这是"the opposite research direction"（相反的研究方向）。

**③ 置信度体系（Confidence）**
每次 Choice/Score 都返回 confidence，官方定位是"第二决策维度"：答案告诉你**做什么**，置信度告诉你**要不要直接执行**。文档同时给了关键限定：校准是"measured across groups of predictions; it does not guarantee that an individual answer is correct"（群体统计意义上的校准，不保证单条正确）。

命名彩蛋：**System One** 取自卡尼曼《思考，快与慢》（快直觉 vs 慢推理，这里主打"快而聚焦的判断"）；**Jev** 取自经济学家 William Stanley Jevons（杰文斯），官方借"煤与蒸汽机效率"的典故讲成本效率。

### 2.4 官方自曝的 9 个失败模式（jaggedness 页）

官方专门发了一页 "Jev 1.13 jaggedness"（模型缺陷），这在 AI 公司里少见，值得全文提炼：

| # | 失败模式 | 要点 |
|---|---------|------|
| 1 | 字面理解 | "answers the question you wrote, not the one you meant"，否定/隐含条件按字面处理 |
| 2 | 数学与数字 | "Jev is not a calculator"，计数不可靠；十六进制色值弱于英文色名；不能判断两数"接近" |
| 3 | 日期时间比较 | 把日期当文本读，排序/间隔/窗口判断不可靠 → 抽取交给模型、算术留在代码 |
| 4 | 间接表达 | 双重否定、复杂间接指令可靠性下降 |
| 5 | 大而杂的状态 | 无关内容越多准确率越低，且难归因——官方承认"suffers from context rot" |
| 6 | 对抗性内容 | state 默认被当作数据而非敌意输入，注入指令"can move the answer" |
| 7 | 自相矛盾的指令 | 指令与 criteria 不匹配会混淆；true 映射到 no 之类的反向问法表现更差 |
| 8 | 选项顺序 | 顺序会影响答案，偏向靠前的选项 |
| 9 | 生成 | 未训练生成文本，用链式 Choice 硬凑生成"会很慢且效果差" |

**通用建议**：别问代码能算的；别把多个判断塞进一个问题；别给 System Two（慢推理）任务；别塞爆 state。

---

## 3. 怎么用（教学 + 实例演算）

### 3.1 五分钟上手（官方 Quickstart 原文）

**安装与配置**（Python ≥ 3.10）：

```bash
pip install typesafe-sdk          # 或 uv add typesafe-sdk
export TYPESAFE_API_KEY=...       # 到 console.typesafe.ai/keys 申请
```

**Python 调用**（官方示例：客服工单分诊，一次调用问三个问题）：

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()

ticket = "Hi, I've been trying to connect my Stripe account for 3 days and the integration keeps failing. I'm losing sales. Please help ASAP."

response = client.system_one(
    state=ticket,
    questions={
        "department": Choice(
            instructions="Which team should handle this",
            criteria={
                "billing": "Payment or subscription issues",
                "technical": "Bugs or integration problems",
                "sales": "Pricing or account questions",
            },
        ),
        "frustration": Score(
            instructions="How frustrated the customer appears",
            criteria=["Calm, just stating facts", "Frustrated but civil", "Very angry, strong language"],
        ),
        "is_urgent": Noul(instructions="The message conveys urgency or time-sensitivity"),
    },
)

print(response.answers["department"].choice)   # "technical"
print(response.answers["frustration"].score)   # 1.0
print(response.answers["is_urgent"].noul)      # 1.0
```

**cURL 直调**（HTTP 层只有一个端点）：

```bash
curl -X POST https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" -H "Content-Type: application/json" \
  -d '{"state":"...","model":"jev-latest","questions":{"urgency":{"type":"noul","instructions":"Does this message express urgency?"}}}'
```

**官方返回结构**（截取 department 部分）：`choice: "technical"`，`confidence: 0.78`，`probabilities: {technical: 0.85, billing: 0.15, sales: 0.0}`，`usage: {input_tokens: 392, output_tokens: 65}`。

### 3.2 实例演算：置信度路由（Confidence-Gated Routing）

用上面官方示例的真实数字走一遍"决策 → 路由"闭环：

```
① 输入：一段 392 token 的工单 state + 3 个问题（Choice/Score/Noul）
② Jev 返回：department = technical（confidence 0.78；technical 0.85 / billing 0.15）
③ 代码读 confidence，而不是读文本：
      if confidence >= 0.90: 直接自动派单
      elif confidence >= 0.60: 派单但打"待抽查"标签
      else: 转人工队列
   → 本例 0.78 落在中档：自动派给技术组 + 抽查标记
④ 成本核算（按官方单价 $0.042/百万输入 token、输出免费）：
      392 × $0.042 / 1,000,000 ≈ $0.0000165 / 次
      对比官网给出的 LLM 示例 $0.013880 / 次 → 约 840 倍差价（本算式为按官方单价推算，非官方数字）
⑤ 失败兜底：若 state 含"忽略以上指令"之类的注入文本，答案可能被推动
   （官方 jaggedness 第 6 条）→ 高风险动作仍需代码规则二次校验
```

**要点**：Jev 的价值不在"答得对"，而在"答得**可编程**"——类型化输出让代码能直接分支，confidence 让代码能决定是否升级人工。

### 3.3 四种官方构建模式（Patterns）

| 模式 | 一句话 | 场景 |
|------|--------|------|
| **Speculative Fan-out** | 一次调用发几十上百个问题，并行拿到全部答案 | 批量打标、批量核对 |
| **Confidence-gated Routing** | 答案定去向，置信度定"自动执行 or 转人工" | 工单分诊、风控放行 |
| **Composite Scoring** | 把复杂判断拆成多个原子 Score，再用代码加权合成 | 内容质量、线索评分 |
| **Intent Routing** | 先分类意图，再路由到最合适的处理器/模型 | Agent 入口、请求分发 |

另有 20 个 Cookbook 配方（护栏、引用核对、RAG 片段分类、重排序、知识图谱实体对齐、简易记忆系统等），官方文档站（Mintlify 搭建）提供 `llms.txt` 全站索引，便于喂给 AI 助手。

### 3.4 与 Coding Agent 的边界（官方专门辟谣）

官方文档明确：Jev **不是** Claude Code / Cursor / Copilot 之类编程代理的"换脑"选项——"There is no `model: "jev-latest"` setting that turns your coding agent into a Jev-powered agent"（编码代理需要能流式输出文本、调工具、改文件，Jev 都不做）。正确姿势：**让 coding agent 写"调用 Jev 做判断"的代码**，并可安装官方 agent skill（`claude plugin marketplace add typesafe-ai/skills`）让代理了解 API。

### 3.5 限制清单（引用前必读）

- **上下文**：64K/请求，其中 state + 最长问题 ≤ 32K；**仅文本**（图/音/视频需自行转文本）
- **语言**：英语为主训练语言、准确率最高；CJK 等"handled but not equally well"
- **限流**：官方文档写 100K token/秒、80 请求/秒，且"adjusting dynamically"可无通知调整（⚠️ CSDN 教程写 250K/秒、1200 请求/分，与官方冲突，以官方为准）
- **不可微调**：不针对客户数据做微调/LoRA，所有账号同一权重；定制只靠请求里的 state / instructions / criteria
- **不解释理由**：只给答案与概率，不给推理过程
- **数据**：官方承诺不用客户请求/响应训练；企业版可谈 ZDR（零保留）

---

## 4. 分发渠道与生态（均已实取核实）

### 4.1 上架渠道

| 渠道 | 状态 | 关键事实 |
|------|------|---------|
| 自有 API | ✅ | `POST https://api.typesafe.ai/v1/systemone`；模型 `jev-1.13.0`（别名 `jev-latest` / `jev-preview`） |
| **Vercel AI Gateway** | ✅ 2026-09-18 博文 | Vercel 称其"the fastest-adopted model in AI Gateway history"：24 小时内近 **13% 付费团队**使用，是 GPT-5.6 家族的 2 倍、Fable 5.1 的 6 倍以上；18 小时触达 1/10 团队 |
| **OpenRouter** | ✅ API 实取 | `typesafe/jev-1.13`：上下文 64K、输入 $0.042/M、输出 $0、uptime 100%；另有 `typesafe/jev-router`（2026-09-26 上架，按请求挑"最佳模型 + 推理强度"，底层跑 Jev） |
| Cloudflare Workers AI | ❌ 未证实 | CSDN 称有 `typesafe/jev`（32K 上下文），Cloudflare 目录页未找到该模型 |
| Python SDK | ✅ PyPI 实取 | `typesafe-sdk` 0.7.4（首版 2026-09-09，累计 8 个版本），requires-python ≥3.10，作者 TypeSafe AI |
| JS/TS SDK | ✅ npm 实取 | `@typesafe-ai/sdk` 0.6.0（registry 创建于 2026-09-12；0.6.0 发布于 09-15 首发日） |
| LangChain 集成 | ✅ PyPI 实取 | `langchain-typesafe` 0.0.1a3（alpha，2026-09-17 首传；CSDN 称含 Classifier / ModelRouter / AutoMode 三件套） |

### 4.2 GitHub 生态（星数为 2026-10-11 gh API 实取）

**官方仓库（12 个，组织 1614 关注者）**：

| 仓库 | 星 | 说明 |
|------|---|------|
| typesafe-ai/skills | 2654 | 官方 Agent Skills（Claude Code 插件 / skills.sh 安装） |
| system-one-adapter-python | 387 | **"Drop-in TypeSafeClient replacement backed by LLM APIs"**——用普通 LLM 顶上同一接口，方便对照评测（与库内 EVAL 呼应） |
| typesafe-sdk-python / -js | 281 / 273 | 官方双语言 SDK |
| WorkflowEvals / typesafe-public-examples / n8n-nodes | 16 / 3 / 10 | 工作流评测代码、示例、n8n 节点 |
| LLaDA / vllm（fork） | 13 / 4 | 扩散语言模型与推理引擎 fork——架构研究线索（见 §2.3①） |

**社区项目（星数 top）**：

| 项目 | 星 | 一句话 |
|------|---|--------|
| yibie/awesome-jev | 2265 | 生态目录（另有 5+ 个同类 awesome 列表，总量可观但同质化明显） |
| firelex/jeff | 1502 | **开源复刻**：0.8B "System 1" 模型，可换 LoRA 适配器，本地部署（jeffhub.ai） |
| awlevin/typesafe-computer-use | 1220 | 用 Jev 做每步决策的 macOS 电脑操作：约 **$0.0002/步**（作者实测比 Claude Opus 5 裸截图方案便宜 155 倍） |
| fhshaik/typesafe-mario | 444 | 用 Jev 从模拟器结构化状态玩超级马里奥 |
| moritzkremb/jev-voice-browser | 398 | 语音控制浏览器，Jev 决定意图与目标 |
| 0xNatoshi/jev-codex-router | 273 | 给 Codex 每轮挑模型/推理深度 |
| mrnugget/jev-shell-history 等 | 100+ | 终端历史排序、语音命令、浏览器自动化等 |

### 4.3 中文内容生态（⚠️ 甄别提醒）

| 站点 | 性质 | 注意 |
|------|------|------|
| CSDN / cnblogs 教程 | 二手教程（2026-09 下旬） | 部分数字与官方冲突（限流、Cloudflare 上架），仅作线索 |
| typesafe-jev.com | 自称"独立社区学习站，与 TypeSafe AI 无隶属关系" | 主动标注"数值为示意"，可信度中等 |
| jevtypesafeai.com | CODEFASHION TECH LTD 运营，标注 "Not affiliated" | 声称价格 "$0.25–$0.42/M" 与官方 $0.042/M **差 10 倍**，疑为笔误；SEO 多语言站 |
| 百度百科词条 | 二手汇编 | 创始人信息与官方一致，可作交叉但非一手 |
| 知乎笔记 | ❌ 403 无法访问 | 仅 Bing 摘要可见 |

**结论**：中文侧"Jev 教程站"多为 SEO/导流站，读用法可以，读数字（价格/限流/上架）请以官方文档为准。

---

## 5. 商业模式与定价

- **定价**：输入 $0.042/百万 token（官网写作 $42/Btok），**输出免费**（"FREE (too cheap to meter)"）；1 美元 ≈ 2380 万 token。官网对比称"238x lower input price than Claude Fable 5.1"。
- **计费逻辑**：按输入 token 计费，意味着"问得越多越贵、答案不额外收费"——与"并行问一大堆问题"的 fan-out 模式天然契合。
- **获客**：免费 Playground（console.typesafe.ai）+ 早期访问制；第三方称注册送 $5 额度（⚠️ 未核实，且已出现"注册机"薅额度脚本，见 §7）。
- **企业版**：DPA / 隐私政策 / ZDR（零数据保留），联系 sales@typesafe.ai。
- **客户规模说法**：官方博客"A third of the Fortune 500 are getting their Jev on"；a16z 公告"25% of the fortune 500 enterprises have integrated Jev"（⚠️ 33% vs 25% 口径不一，且均未给统计方法）。

---

## 6. 多维评价

### 优势 / 价值
- **范式清晰**：把"给软件用的判断"从"给人类看的文本"里切出来，类型化输出 + 概率 + 置信度，工程上可直接分支，不需要解析/容错层。
- **成本结构狠**：输出免费 + 并行采样，让"每个 agent 每一步都问一次模型"从奢侈变成可行（社区电脑操作项目 $0.0002/步是最好例证）。
- **透明度反常识**：主动发布 9 个失败模式页、发"反基准刷分"宣言（"Lies, Damned Lies, and Benchmarks"：不发标准基准表、只用带日期的快照、内评数据连同挑刺一起公布）——在当下 AI 营销环境里罕见。
- **生态启动快**：官方 SDK 双语言 + agent skill + 适配器 + 2000+★ 社区项目，发布一个月形成可用生态。

### 问题 / 局限性
- **能力边界窄且硬**：不会算术/日期比较/生成；对抗注入不设防；选项顺序有偏置——它只能当"判断原语"，不能当"助手"。
- **校准 ≠ 正确**：官方自己写明 confidence 是群体统计性质，单条答案仍可能错；"零幻觉"只对"不生成文本"成立，不等于"不出错"。
- **英文优先**：CJK 用户的实际准确率官方未给数，只说"not equally well"。
- **封闭**：不开源权重、不支持微调、不可自部署（社区只能用 `system-one-adapter` 拿 LLM 模拟对照，或等 `jeff` 这类复刻）。

### 适用场景
- 工单/邮件/线索**分诊与路由**；内容与输出的**质量打分**；LLM 输出**护栏与核对**（引用核验、RAG 片段筛选）；Agent 每一步的**动作选择与升级判断**；批量**结构化抽取**（日期、实体、意图）。

### 发展趋势
- 从"单模型"走向"路由层"：`jev-router`、LangChain `ModelRouterMiddleware`、codex-router 都指向"Jev 当大模型系统的调度中枢"。
- 若"决策模型"品类成立，可能被大厂内化（各家 classifier 路线）或成为 agent 基础设施的标准件；a16z 的站台说明资本在押注"非聊天"路线。

### 横向对比

| 对照 | 差异 |
|------|------|
| Jev vs LLM 分类（prompt "只返回 JSON"） | Jev 结构由构造保证、便宜百倍、毫秒级；LLM 灵活但贵、慢、需容错 |
| Jev vs 传统 ML 分类器（BERT 等微调） | Jev 零训练、改 criteria 即改任务、带置信度；传统分类器要数据与训练但可离线、可解释 |
| Jev vs 规则引擎 | 规则精确但脆；Jev 处理模糊语义但不可审计——官方建议"代码定事实、模型做判断"混合使用 |
| TypeSafe AI vs 大模型实验室 | 不拼通用智能，拼"决策原语"的延迟/成本/校准，属基础设施型公司 |

### 与库内其他文档的关联
- **EVAL**：官方开源 `system-one-adapter-python`（用 LLM 顶替 Jev 做对照）+ `WorkflowEvals` + evals.typesafe.ai，且公开"反 benchmaxxing"立场——与本库 EVAL 概念、Vercel Run SDK 一条线。
- **Vercel 工具链**：Jev 是 AI Gateway 的现象级上架模型（本文同时更正了 Vercel 篇旧文"自有模型 Jev"的误记）。
- **机器学习全景 / 持续学习**：System One 是"不生成、只判断"的窄模型路线，与 LLM 生成路线形成对照样本。

---

## 7. 争议与风险

1. **数字对账**：官网标题"193.6x Faster, 444.6x Cheaper"与其下方示例数字（8.566s→0.114s ≈ 75x；$0.01388→$0.000081 ≈ 171x）**对不上**——可能为不同任务集的平均口径，但页面未说明；Vercel 转述为"up to 194x/445x"。引用倍数时应标注"官方自评、口径未明"。
2. **融资数字单源**：$870M / $7.5B 只见于官方博客；a16z 公告只说"领投"未披露金额；Bing 新闻/主流科技媒体（TechCrunch 等）**未检索到独立报道**。金额若被引用，需注明"官方自述，未经第三方证实"。
3. **客户占比打架**：官方"1/3 财富 500" vs a16z"25%"，且无统计口径。
4. **"零幻觉"话术**：官网 Zero Hallucinations 与官方文档"校准不保证单条正确"并存，营销与工程口径需分开理解。
5. **Token 量级不一**：a16z 称"3 天 1 万亿 token"（1T），CSDN 称"几天 1610 亿"（161B）——量级差 6 倍，可能统计窗口不同，未见官方统一口径。
6. **薅羊毛生态**：GitHub 出现 `typesafe_register`（133★，批量注册账号自动建 API Key，"多线程 0.12 秒一个"）——免费额度政策被滥用，反映早期增长含水分的可能。
7. **SEO 内容农场**：大量"Jev 教程/playground"站点蹭词，价格与限流数字常有错（见 §4.3），搜索者极易读到错误信息。
8. **访问性**：console.typesafe.ai 与 evals.typesafe.ai 从本机（中国网络）返回 **451**（因法律原因不可用），中国大陆直接使用可能受限，需代理。
9. **同名混淆**：Typesafe/Lightbend（Scala/Akka）与 TypeSafe AI 完全无关，尽调/检索时必须区分。

---

## 8. 参考来源（均为实际访问，标注核实状态）

**一手（官方/权威）**
- TypeSafe AI 官网首页（定位、Jev、193.6x/444.6x、零幻觉、SF）：https://typesafe.ai/ ✅ 抓取成功
- 官方文档·Introduction（三种原语、并行评估）：https://docs.typesafe.ai/introduction ✅
- 官方文档·Models（jev-1.13.0、别名、价格、限流 100K/s+80rps、64K/32K、语言、数据政策）：https://docs.typesafe.ai/models ✅
- 官方文档·System One（校准定义、命名由来）：https://docs.typesafe.ai/concepts/system-one ✅
- 官方文档·Quickstart（SDK 安装、工单示例代码与返回）：https://docs.typesafe.ai/introduction/quickstart ✅
- 官方文档·Coding Agents（Jev 不能替代编码代理）：https://docs.typesafe.ai/introduction/coding-agents ✅
- 官方文档·Jev 1.13 jaggedness（9 个失败模式）：https://docs.typesafe.ai/model-jaggedness/jev-1.13 ✅
- 官方文档·Legal（不训练客户数据、ZDR）：https://docs.typesafe.ai/legal ✅
- 官方文档站全站索引：https://docs.typesafe.ai/llms.txt ✅
- 官方博客·Introducing System One Models & Jev（两年隐身、RLCD、并行采样、Jevons 命名、Doom 演示）：https://typesafe.ai/blog/introducing-system-one-models-and-jev ✅（页面时间戳为抓取日动态渲染，实际发布≈09-15）
- 官方博客·TypeSafe A raises Series AI（$870M/$7.5B、a16z 领投、Sequoia/DCVC、Casado 入董事会）：https://typesafe.ai/blog/series-ai ✅（⚠️ 金额为自述单源）
- 官方博客·Lies, Damned Lies, and Benchmarks（反基准刷分立场）：https://typesafe.ai/blog/antibenchmaxxing ✅
- **a16z 官方公告·Investing in TypeSafe AI**（2026-10-09；领投、1T tokens/3 天、25% 财富 500、创始人 Diogo Almeida）：https://a16z.com/announcement/investing-in-typesafe-ai/ ✅
- **Vercel 官方博客·Jev on AI Gateway**（2026-09-18；09-15 发布、采纳最快、13% 付费团队）：https://vercel.com/blog/ai-gateway-jev-model-launch ✅
- **OpenRouter API**（`typesafe/jev-1.13` 价格/上下文/uptime；`typesafe/jev-router` 创建时间）：https://openrouter.ai/api/v1/models/typesafe/jev-1.13/endpoints ✅ API 实取
- **GitHub API**（组织 12 仓库/1614 关注者/创建于 2024-05-28；skills 2654★ 等）：https://github.com/typesafe-ai ✅ gh api 实取
- **PyPI / npm**（typesafe-sdk 0.7.4；@typesafe-ai/sdk 0.6.0；langchain-typesafe 0.0.1a3）：https://pypi.org/pypi/typesafe-sdk/json ✅ 实取
- **arXiv 2303.08774**（GPT-4 技术报告；在贡献者名单与文献 [63] InstructGPT 作者名单中 grep 到 Diogo Almeida）：https://arxiv.org/pdf/2303.08774 ✅ 原文核实
- GitHub 组织 `typesafehub`（同名辨析：现名 "Lightbend (Typesafe archive)"）：https://github.com/typesafehub ✅ gh api 实取

**二手（仅作交叉/线索）**
- CSDN《Jev 使用完整指南》（2026-09-21；发布日、控制台/限额数字与官方有冲突）：https://blog.csdn.net/aidoudoulong/article/details/166245683 ⚠️
- 博客园《2026 年完整指南：什么是 Jev》（System One/Two 框架、RLCD、Cloudflare/LangChain 说法）：https://www.cnblogs.com/sing1ee/p/23040079 ⚠️
- typesafe-jev.com（自称独立社区站，主动声明无隶属）：https://typesafe-jev.com/getting-started/ ⚠️
- jevtypesafeai.com（CODEFASHION TECH LTD 独立站，标注 Not affiliated；价格数字与官方差 10 倍）：https://jevtypesafeai.com/zh ⚠️
- 百度百科 TypeSafe AI 词条（创始人信息）：https://baike.baidu.com/item/TypeSafe%20AI/69115362 ⚠️ 直接访问 403，仅经 Bing 摘要引用

**未能访问（如实记录）**
- 知乎《TypeSafe (Jev) 学习笔记与架构思考》：https://zhuanlan.zhihu.com/p/2089319541859947086 ❌ 403
- X 账号 https://x.com/typesafeai ❌ 本机网络不可达（未取到内容）
- https://console.typesafe.ai/ 、 https://evals.typesafe.ai/ ❌ 返回 451（本机网络/合规拦截）

---

## 9. 我的思考（留给自己）

> （尽调视角：这家公司最值得追的一个问题是什么？它和我手里的哪个系统能接上？如果"决策模型"成立，我的 agent 里第一个该换成 Jev 的判断节点是哪一个？）
