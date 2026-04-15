# MONICA AI 小說工廠

這個資料夾整理「Codex + Hermes + Claude」三代理分工的小說量產流程。

## 核心定位

- `Codex`：結構控制與狀態管理，只負責設定、架構、狀態更新，不直接生成正文。
- `Hermes`：章節初稿量產，只負責依既有資料生成初稿，不修改設定與狀態。
- `Claude`：修稿、邏輯檢查與回饋，輸出 final 版本與 Revision Report。

## 最小可執行流程

1. Codex 建立並維護必要 Markdown。
2. Hermes 依章綱產出 `chapter_xxx_draft.md`。
3. Claude 修稿並產出 `chapter_xxx_final.md` 與 `Revision Report`。
4. Codex 依 report 更新 `story_state.md`、`character_state.md`、`foreshadowing.md`。
5. Hermes 依最新狀態續寫下一章。

## 主要文件

- [workflow.md](workflow.md)：完整單章循環流程。
- [roles.md](roles.md)：三代理角色邊界。
- [quality_control.md](quality_control.md)：A/B/C 級品質分流。
- [android_pc_mode.md](android_pc_mode.md)：手機/平板 + PC 操作模式。
- [templates/](templates/)：狀態檔與報告模板。
- [prompts/](prompts/)：Hermes、Claude、Codex 提示詞模板。
- [automation/pipeline.py](automation/pipeline.py)：Python 自動化流程骨架。

## 最重要原則

1. 正文與設定一定分開。
2. 修改正文後，一定要回寫 state。
3. Hermes 永遠不能改規則。
4. Claude 只能建議改設定。
5. Codex 才能正式改設定。
