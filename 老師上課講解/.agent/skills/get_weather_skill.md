---
功能名稱: 氣候感測技能 (Get Weather Skill)
版本編號: v1.0.0
修改日期: 2026-04-23
功能類型: 環境感知 / MCP 對接技能
內容描述: 透過 MCP Server「weather」之 get_weather 工具取得即時氣溫，提供給 Persona 與 Rules 作為決策依據。
---


## 2. 進階實作規格 (AI好理解版)

### 技能呼叫規格 (Skill Specification)

| 欄位 (Field) | 內容 (Value) |
| :--- | :--- |
| **mcp_server** | `weather` |
| **tool_name** | `get_weather` |
| **input_param** | `city: string`（來源：Knowledge 天氣查詢城市） |
| **output_field** | `current_temp: number` (°C) |

### 錯誤處理矩陣 (Error Handling)

| 錯誤情境 (Scenario) | 處理動作 (Action) | 降級輸出 (Fallback) |
| :--- | :--- | :--- |
| Server 未啟動 | 回報「氣候感測暫時無法使用」 | 顯示預設推薦（不套用 weather_recommendation） |
| 城市名不合法 | 回報參數錯誤 | 提示改用 `Taipei`（英文） |
| 網路逾時 | 重試 1 次，仍失敗則降級 | 同上 |