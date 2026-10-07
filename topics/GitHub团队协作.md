---
title: GitHub 团队协作（3 人实战指南）
date: 2026-09-28
type: 专题
tags: [git, github, pull-request, teamwork, code-review]
confidence: 高
---

# 📌 GitHub 团队协作实战：3 人如何各写各的、互不干扰

> 整理日期：2026-09-28 ｜ 类型：专题调研 ｜ 置信度：**高**（GitHub 官方文档 4 篇实际抓取核实）｜ 关联：`relations.md`
> 一句话总结：**团队协作的核心不是"各写各的代码不冲突"，而是"把冲突变少、变可见、变可控"——用分支隔离工作、用 PR 做质量门槛、用保护规则做制度兜底。3 个人的分工 = 3 条独立分支 + 3 个 PR + 1 条受保护的 main。**

---

## 1. 机制详解一：分支工作流（GitHub Flow，官方流程）

GitHub 官方推荐的协作模型（已核实官方文档）：

```
main（受保护，永远可发布）
  ↑ 只能通过 PR 合入
  └── feature/登录 ← 小明
  └── feature/笔记 ← 小红
  └── feature/资料 ← 小刚
```

**六步循环（每人每次需求都走一遍）：**
1. **建分支**：`git checkout -b 描述性名字`（如 `feature/add-login`）——安全的工作空间，不影响 main；
2. **写代码**：每次提交是"独立且完整的更改"（功能与修注释分开提交）；持续 push 备份；
3. **开 PR**：请求评审；可标 Draft 提前要反馈；关联 issue（合并后自动关闭）；
4. **评审对话**：评审者可在**具体行**上评论/提建议；作者继续提交，PR 自动更新；
5. **合并 PR**：评审通过（+自动化检查通过）才允许合并；
6. **删分支**：合并后删除（历史与 PR 不丢，可恢复）。

**关键点（官方原文强调）：** 分支隔离=安全工作空间；审查=合并前发现问题的质量关卡；**每个不相关的更改集用独立分支**，便于理解、恢复、扩展。

## 2. 机制详解二：PR 合并方式（三种，决策表）

| 方式 | 行为 | 历史 | 适合 |
|------|------|------|------|
| **合并提交**（Merge） | 用显式合并提交并入（--no-ff） | 保留每一次提交 | 重视完整历史、单个提交有意义 |
| **压缩合并**（Squash） | 整个 PR 压成一个提交 | 只留一个整合提交 | **每个 PR 代表一个逻辑变更**（最常用） |
| **变基合并**（Rebase） | 逐提交搬到 main | 线性历史、保留每提交 | 提交已经理得很清晰 |

**注意**：合并需写入权限；压缩/变基还要求仓库勾选允许；变基若 GitHub 无法自动完成需在本地手动解决；长生命周期分支慎用 squash（后续再开 PR 会把已合的提交再带回去）。

## 3. 机制详解三：分支保护规则（制度兜底，官方已核实）

管理员可在仓库 Settings → Branches 配置（要点）：
- **要求 PR 评审**：合并前至少 N 个批准（可要求 Code Owner）
- **必需状态检查**：CI 必须成功才能合（可为"严格"：必须与 main 最新同步）
- **解决对话**：所有评论解决后才能合并
- **必需线性历史** / **必需签名** / **合并队列**（自动排队）
- **禁止直接推送 main**（默认即禁止强制推送/删除）
- 管理员也可被约束："不允许绕过上述设置"

**这就是"3 人各自写各自"的制度保障：main 谁也不能直接推，改动必须过 PR 大门。**

---

## 4. 实例演算：3 人真实协作走一遍（含冲突）

场景：3 人开发 `note-app`（A 做登录、B 做笔记、C 做资料），仓库刚建，main 受保护。

```bash
# ── 开工：每人 clone 一次即可 ──────────────────────────
git clone https://github.com/MYC/note-app.git && cd note-app

# ── A：做登录（feature/login）─────────────────────────
git checkout -b feature/login
# …写 auth.go …
git add auth.go && git commit -m "feat: 新增登录接口"
git push -u origin feature/login
# → 网页开 PR：login → main，请求 C 评审

# ── B：做笔记（feature/notes），开工前先拉最新 main ─────
git checkout main && git pull
git checkout -b feature/notes
# …写 notes.py …
git add notes.py && git commit -m "feat: 新增笔记接口"
git push -u origin feature/notes      # → 开 PR，请 A 评审

# ── C：做资料页（feature/profile）────────────────────
git checkout -b feature/profile
# …写 profile.py …
git push -u origin feature/profile    # → 开 PR #3

# ── 冲突时刻：A 在 notes.py 加了"备注"参数，
#    B 也在同一行加了"标签"参数 ─────────────────────────
# A 的 PR 先合并 → B 的 PR 变红：冲突！
git checkout feature/notes
git pull origin main                  # 或 git merge main

#    Git 输出：CONFLICT (content): Merge conflict in notes.py
#    Automatic merge failed; fix conflicts and then commit.
git add notes.py      # 手动保留双方参数后暂存
git commit -m "merge: 解决 notes.py 冲突"
git push              # 推回 → 冲突按钮解除 → 评审通过 → Merge

# ── 纪律惯例 ─────────────────────────────────────────
git checkout main && git pull && git branch -d feature/notes  # 清分支
```

**冲突的真实规律（官方核实）**：两个人在**同一文件的同一行**改、或一人改一人删文件时 Git 无法自动决定 → 需人工解决。最**高频冲突路径**：长活分支拖太久。**解法 = PR 小而快 + 开工前拉最新 + 定期 merge main。** 冲突在 PR 里暴露得越早，代价越小。

---

## 5. 制度清单（直接抄给团队）

| 制度 | 内容 | 作用 |
|------|------|------|
| 保护 main | 禁止直接推送，强制 PR+1 审核 | 让 main 永远可发布 |
| CI 必过 | 状态检查（测试/构建/lint）通过才可合并 | 自动化兜底 |
| PR 小而快 | 一个 PR = 一个需求，2-3 天内合并 | 减少冲突概率 |
| 明确命名 | `feature/*`、`fix/*`、`docs/*` | 一看分支知意图 |
| 提交消息规范 | `feat:/fix:/docs:/refactor:` | 历史可读 |
| 合并方式固定 | 默认 Squash（干净历史） | 历史简介 |

---

## 6. 常见坑与建议

- 不要直接推 main（保护规则锁死前先在心理锁定）；
- 不要一个 PR 塞三个功能的代码（评审者和冲突都会爆炸）；
- 冲突不要用 `git push --force` 掩盖，先 pull 再说；
- 大文件/密钥**严禁**提交（.gitignore 从头置好，含 .env）；
- 评审是义务不是礼貌：让 3 人交叉互审，两个 PR 不相关者也看；
- fork + PR 模式留给外部贡献者；内部 3 人用"共享仓库 + 分支 + PR"最轻。

---

## 7. 参考来源（全部实际抓取核实 ✅）

- GitHub Flow（六步流程原文）：https://docs.github.com/zh/get-started/using-github/github-flow
- 关于 PR 合并（三种方式原文）：https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges
- 合并冲突（类型与解决流程）：https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts
- 分支保护规则（全部可配置项）：https://docs.github.com/zh/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches

---

## 8. 我的思考（留给自己）

> （我们团队现在最缺哪条制度？要先把"保护 main + PR"两条金标准立起来吗？）