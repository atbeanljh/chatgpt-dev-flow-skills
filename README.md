# chatgpt-dev-flow-skills
<p align="center">
  <h1 align="center">chatgpt-dev-flow-skills</h1>
  <p align="center">一套完整的 Codex 开发任务工作流 Skill 集合</p>
  <p align="center">需求分析 → 方案设计 → 实施计划 → 编码实现 + Bug 修复</p>
</p>

---

chatgpt-dev-flow-skills 是一组专为 **Codex**（OpenAI 的编程智能体）设计的工作流 Skill。它把开发任务拆成四个标准阶段，外加一个独立的 Bug 修复流程，让 Codex 在复杂项目上的行为更结构化、可追踪、可恢复。

## 包含的 Skill

| Skill | 触发词 | 作用 |
|-------|--------|------|
| **task-require** | `/require` | 需求分析 — 产出一份 `.cospec` 风格的需求文档 |
| **task-design** | `/design` | 方案设计 — 功能 + 技术设计，产出设计文档 |
| **task-plan** | `/plan` | 实施计划 — 将方案拆分为可执行的任务清单 |
| **task-code** | `/code` | 编码实现 — 按任务清单逐一实现、编译、验证 |
| **task-fix** | `/fix` | Bug 修复 — 根因分析 → 修复编码 → 验证交付 |

## 工作流概览

```
  主流程                          独立流程
 ┌──────────┐                  ┌──────────┐
 │ 需求分析  │ ← /require      │ Bug 修复 │ ← /fix
 │ task-require│                │ task-fix │
 └────┬─────┘                  └──────────┘
      │ /design（手动触发）
      ▼
 ┌──────────┐
 │ 方案设计  │ ← /design
 │ task-design│
 └────┬─────┘
      │ /plan（手动触发）
      ▼
 ┌──────────┐
 │ 实施计划  │ ← /plan
 │ task-plan│
 └────┬─────┘
      │ /code（手动触发）
      ▼
 ┌──────────┐
 │ 编码实现  │ ← /code
 │ task-code│
 └──────────┘
```

每个阶段启动时，**自动确认上一阶段已完成**（更新 status.md），但阶段间的切换仍由你手动通过触发词控制。

编码实现完成后，**自动执行收尾工作**：确认任务清单全部完成、更新状态文件、汇总变更内容。

## 安装

### 前提条件

- 你需要有 **Codex**（桌面版或 CLI 均可）

### 安装方式

在 Codex 中直接说：

> 帮我安装 skill，从 `https://github.com/atbeanljh/chatgpt-dev-flow-skills` 安装 task-require、task-design、task-plan、task-code、task-fix

Codex 会自动下载并安装到 `~/.codex/skills/` 目录下。安装后下一次对话即可使用。

## 使用方式

### 开始一个新任务

1. 在项目目录中跟 Codex 说：`/Task Rquirement 帮我加一个用户反馈功能`
2. Codex 创建任务文件夹，分析项目，产出需求文档
3. 确认需求后，说 `/Task Design` 进入方案设计
4. 确认设计后，说 `/Task plan` 进入任务拆解
5. 确认计划后，说 `/Task code` 开始编码

### 修复一个 Bug

直接说：`/Task Bug fix 用户列表页面点编辑时白屏`，Codex 会自动定位分析并修复。

## 项目结构

```
chatgpt-dev-flow-skills/
├── task-require/              # 需求分析
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── scripts/
│       ├── init_task_folder.py
│       └── resolve_task_folder.py
├── task-design/               # 方案设计
│   ├── SKILL.md
│   └── agents/openai.yaml
├── task-plan/                 # 实施计划
│   ├── SKILL.md
│   └── agents/openai.yaml
├── task-code/                 # 编码实现
│   ├── SKILL.md
│   └── agents/openai.yaml
├── task-fix/                  # Bug 修复
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── scripts/
│       └── init_fix_folder.py
└── README.md
```

## 特性

- **阶段性产出** — 每个阶段产生独立文档（需求 / 设计 / 任务清单 / 修复记录），方便追溯
- **可中断恢复** — status.md 记录进度，中断后可从断点继续
- **自动确认** — 启动下一阶段时自动确认上一阶段，减少手动操作
- **编码后收尾** — 编码完成后自动执行文件状态更新和变更总结
- **独立修复流程** — Bug 修复不干扰主工作流，产出单独的修复记录

## 注意

这些 Skill 是 **Codex 专属**的，依赖 Codex 的 Skill 机制（SKILL.md 元数据装载）。无法在 Cursor、Claude Code、GitHub Copilot 等其他工具中原样使用。

## License

MIT

