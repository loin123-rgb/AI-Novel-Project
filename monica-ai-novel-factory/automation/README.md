# Automation Layer

這個資料夾是 MONICA AI 小說工廠的 Python 執行層。

目前目標：

- 保留乾淨的 workflow 骨架
- 主供應商使用 Gemini API
- 預留 Ollama 備援接口
- 讓後續 Claude Code 可以直接接手補實作

## 設計原則

1. 工作流只做流程控制，不直接寫死特定模型邏輯。
2. 模型供應商透過 provider 抽象層切換。
3. Markdown 檔案是唯一穩定資料來源。
4. 狀態更新仍由 Codex / 報告流程控制，不由生成模型自行改寫。
