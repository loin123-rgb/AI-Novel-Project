# 角色分工

## Codex：結構控制

負責：

- 建立與維護設定文件
- 管理故事架構與章節流程
- 更新 `story_state.md`
- 更新 `character_state.md`
- 更新 `foreshadowing.md`
- 控制檔名、資料夾與流程一致性

不負責：

- 直接生成章節正文
- 把正文當成狀態檔寫回

## Python Workflow + Gemini API：初稿生成

負責：

- 讀取章綱與狀態檔
- 生成章節初稿
- 可選擇進行簡單自檢
- 輸出：
  - `chapter_xxx_draft.md`
  - `chapter_xxx_draft_v2.md`（可選）

不負責：

- 修改設定
- 回寫狀態檔
- 自行修復重大邏輯衝突

## Claude：修正與回饋

負責：

- 修文風
- 修節奏
- 修對話
- 修邏輯
- 檢查人設與世界觀
- 輸出：
  - `chapter_xxx_final.md`
  - `Revision Report`

不負責：

- 正式修改設定檔
- 擅自新增硬設定

## 權限邊界

- 初稿生成模型只能產生正文草稿。
- Claude 只能修稿與提出建議。
- Codex 是唯一能正式更新設定與狀態的角色。
