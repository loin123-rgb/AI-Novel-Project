# MONICA Python Workflow + Gemini API 架構說明

## 目標

這份文件定義 MONICA AI 小說工廠後續要採用的執行架構：

```text
Codex + Python Workflow + Gemini API + Claude
```

這個版本不再依賴 Hermes。

---

## 核心定位

### Codex

負責：

- 管理專案結構
- 維護狀態檔
- 維護提示詞
- 控制章節流程
- 更新 `story_state.md`、`character_state.md`、`foreshadowing.md`

不負責：

- 生成章節正文

### Python Workflow

負責：

- 讀取 Markdown 輸入資料
- 組裝 prompt
- 呼叫 Gemini API
- 寫入章節草稿
- 保留執行 log
- 為未來的 Ollama 備援保留路由能力

不負責：

- 正式修改設定檔
- 取代 Claude 的修稿工作

### Gemini API

負責：

- 生成章節初稿
- 可選擇執行簡單自檢

### Claude

負責：

- 修稿
- 邏輯檢查
- 產出 final 版本
- 產出 Revision Report

---

## 執行流程

```text
讀取 md
→ 組裝 prompt
→ Gemini API 生成 draft
→ 可選自檢 draft_v2
→ Claude 修稿
→ 產出 revision report
→ Codex 更新 state
→ 下一章
```

---

## 最小可執行流程

### 輸入

- `style_guide.md`
- `chapter_outline.md`
- `state/story_state.md`
- `state/character_state.md`（可選）
- 必要角色 / 世界觀片段

### 輸出

- `chapters/chapter_xxx_draft.md`
- `chapters/chapter_xxx_final.md`
- `reports/chapter_xxx_revision_report.md`

---

## Python 專案結構

```text
automation/
├─ app/
│  ├─ __init__.py
│  ├─ config.py
│  ├─ models.py
│  ├─ providers/
│  │  ├─ __init__.py
│  │  ├─ base.py
│  │  ├─ gemini.py
│  │  └─ ollama.py
│  └─ workflows/
│     ├─ __init__.py
│     └─ novel_workflow.py
├─ .env.example
├─ config.example.yaml
├─ main.py
├─ pipeline.py
└─ requirements.txt
```

---

## 模組說明

### `config.py`

負責：

- 讀取 `.env`
- 讀取 YAML 設定
- 匯出執行設定

### `models.py`

負責：

- 定義章節任務資料結構
- 定義工作流輸入與輸出資料型別

### `providers/base.py`

負責：

- 定義模型供應商介面

### `providers/gemini.py`

負責：

- 對接 Gemini API
- 後續可改成 Interactions API 或標準 content generation 呼叫

### `providers/ollama.py`

負責：

- 預留本機 Ollama 備援接口

### `workflows/novel_workflow.py`

負責：

- 讀取 Markdown
- 建立 prompt
- 呼叫 provider
- 輸出草稿檔

### `main.py`

負責：

- 當 CLI 入口
- 指定工作流模式
- 指定章節編號

---

## Provider 路由策略

### 主模型

```text
Gemini API
```

### 備援模型

```text
Ollama（本機 RTX 4060 8GB）
```

### 建議策略

- 預設使用 Gemini
- 若 API 配額 / 429 問題發生，再手動切換到 Ollama
- 暫時不加入 OpenRouter

---

## 設定檔設計

### `.env`

建議內容：

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
OLLAMA_BASE_URL=http://127.0.0.1:11434
OLLAMA_MODEL=qwen2.5:7b
DEFAULT_PROVIDER=gemini
```

### `config.yaml`

建議內容：

```yaml
providers:
  default: gemini
  gemini:
    model: gemini-2.5-flash-lite
  ollama:
    model: qwen2.5:7b

paths:
  chapters_dir: chapters
  reports_dir: reports
  state_dir: state
  prompts_dir: prompts
```

---

## 章節工作流規格

### `draft`

Python workflow 讀取：

- `prompts/gemini_chapter_draft.md`
- `style_guide.md`
- `state/story_state.md`
- 指定章節 outline

輸出：

- `chapters/chapter_xxx_draft.md`

### `revision`

交由 Claude 處理：

- `draft.md`
- `style_guide.md`
- `state/story_state.md`
- `state/character_state.md`

輸出：

- `chapters/chapter_xxx_final.md`
- `reports/chapter_xxx_revision_report.md`

### `state_update`

由 Codex 根據 Revision Report 更新：

- `story_state.md`
- `character_state.md`
- `foreshadowing.md`

---

## 下一階段建議

### Phase 1

完成最小工作流：

- 可讀 md
- 可呼叫 Gemini
- 可輸出 draft

### Phase 2

加入：

- 章節編號參數
- log
- 簡單錯誤處理
- draft_v2 自檢模式

### Phase 3

加入：

- Ollama 備援切換
- revision report parser
- state update helper

---

## 給 Claude Code 的接手說明

下一步不需要重做架構，只需要補實作：

1. 實作 `providers/gemini.py`
2. 讓 `main.py` 支援 CLI 執行
3. 讓 `novel_workflow.py` 能真正輸出 draft
4. 視需要再補 Ollama 備援

一句話總結：

```text
現在要做的是把 MONICA 的「生成層」正式換成 Python + Gemini API，
而不是再回頭救 Hermes。
```
