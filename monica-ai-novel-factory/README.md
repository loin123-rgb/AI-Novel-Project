# MONICA AI 小說工廠

這個專案現在採用 `Codex + Python Workflow + Gemini API + Claude` 的協作架構，不再依賴 Hermes。

## 角色定位

- `Codex`
  - 負責結構控制、狀態更新、流程整理
- `Python Workflow + Gemini API`
  - 負責章節初稿生成與可選自檢
- `Claude`
  - 負責修稿、邏輯檢查、輸出 Revision Report

## 最小可執行流程

1. Codex 建立與維護核心 Markdown。
2. Python workflow 讀取 `style_guide.md`、`chapter_outline.md`、`story_state.md`。
3. Gemini API 生成 `chapters/chapter_xxx_draft.md`。
4. Claude 修稿並輸出：
   - `chapters/chapter_xxx_final.md`
   - `reports/chapter_xxx_revision_report.md`
5. Codex 根據 Revision Report 更新：
   - `state/story_state.md`
   - `templates/character_state.md`
   - `templates/foreshadowing.md`

## 文件索引

- [workflow.md](workflow.md)：單章標準流程
- [roles.md](roles.md)：角色分工與權限邊界
- [quality_control.md](quality_control.md)：A/B/C 級品質控制
- [android_pc_mode.md](android_pc_mode.md)：手機、平板、PC 的工作分工
- [templates/](templates/)：狀態模板與 Revision Report 模板
- [prompts/](prompts/)：Gemini、Claude、Codex 使用的提示詞
- [automation/pipeline.py](automation/pipeline.py)：Python 工作流骨架

## 架構原則

1. 正文與設定必須分離。
2. 狀態更新只能由 Codex 正式回寫。
3. 初稿生成由 Python workflow 呼叫模型完成，不直接讓模型改設定。
4. Claude 只能修稿與提出建議，不直接改狀態檔。
5. 之後若 Gemini API 遇到配額限制，可保留本機 Ollama 作為備援，但不改動整體流程。
