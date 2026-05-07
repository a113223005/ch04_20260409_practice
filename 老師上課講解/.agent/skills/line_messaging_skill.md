# 定義與 LINE MCP Server 的對接技能

## 實作

| 設定項目 | 內容說明 |
| :--- | :--- |
| **核心能力** | 對指定 LINE 用戶發送文字訊息 |
| **呼叫對象** | 呼叫名為 `line` 的 MCP 伺服器 |
| **使用工具** | 使用 `push_message` 工具（也就是 LINE 官方提供的「主動發送推播」功能） |
| **發送對象 (to)** | 系統自動讀取 `.env` 裡的 `DESTINATION_USER_ID`，不需要手動指定 |
| **發送內容 (text)** | 由流程 (Workflow) 傳入剛剛 Persona 產生的推播訊息文字 |