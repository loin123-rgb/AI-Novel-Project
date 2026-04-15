# 單章標準流程

## STEP 1：讀取資料

輸入：

- `style_guide.md`
- `chapter_outline.md` 指定章節
- `story_state.md`
- `characters/` 必要片段
- `world/` 必要片段

## STEP 2：Hermes 生成初稿

輸出：

- `chapters/chapter_xxx_draft.md`

規則：

- 不可改設定。
- 必須推進劇情。
- 保留情緒與畫面。
- 不處理深層邏輯修正。

## STEP 3：Hermes 自檢，可選

檢查：

- 重複句
- 語氣不順
- 明顯錯字
- 簡單連貫錯誤

輸出：

- `chapters/chapter_xxx_draft_v2.md`

## STEP 4：Claude 修稿

輸入：

- `chapter_xxx_draft.md` 或 `chapter_xxx_draft_v2.md`
- `style_guide.md`
- `story_state.md`
- `character_state.md`
- `world/` 必要片段

處理：

- 修文風
- 修節奏
- 修對話
- 修邏輯
- 檢查設定衝突

輸出：

- `chapters/chapter_xxx_final.md`
- `reports/chapter_xxx_revision_report.md`

## STEP 5：Claude 輸出回報

Claude 必須輸出 Revision Report，格式見：

- [templates/revision_report.md](templates/revision_report.md)

## STEP 6：回餵系統

回 Hermes：

- 語氣調整
- 節奏模式
- 情緒模式
- 下一章續寫限制

回 Codex：

- 建議更新 `story_state.md`
- 建議更新 `character_state.md`
- 建議更新 `foreshadowing.md`

## STEP 7：Codex 更新 Markdown

Codex 動作：

- 同步所有狀態變更。
- 確保設定一致。
- 只採納 Claude 報告中確認合理的變更。
- 不把正文直接混入設定。

## STEP 8：進入下一章

循環：

```text
Codex → Hermes → Claude → 回餵 → Codex → 下一章
```
