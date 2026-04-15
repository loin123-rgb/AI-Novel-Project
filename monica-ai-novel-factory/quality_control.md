# 品質控制

## A 級：直接可用

條件：

- 無明顯錯誤
- 人設一致
- 世界觀一致
- 節奏可接受
- 可直接進 final

處理：

- Claude 輕修即可。
- Codex 更新狀態。

## B 級：Hermes 修

條件：

- 小問題
- 重複句
- 語氣不順
- 局部描述需要整理

處理：

- Hermes 先產出 `draft_v2`。
- Claude 再做 final 修稿。

## C 級：Claude 修

條件：

- 人設錯
- 劇情錯
- 設定衝突
- 章節目標沒有完成
- 情緒或對話方向偏離

處理：

- Claude 深修。
- Revision Report 必須清楚列出衝突點。
- Codex 決定是否回寫狀態或調整章綱。
