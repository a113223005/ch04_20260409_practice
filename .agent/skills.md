---
功能名稱: 手搖飲 Agent 外部技能 (Skills)
版本編號: v1.0.1
修改日期: 2026-03-28
描述: 定義 Agent 的具體計算能力與外部 API 調用介面。
---

# 🛠️ 技能清單 (Skills & Tools)

本 Agent 包含以下核心功能 (Skills)，可供系統調用執行：

## 🥤 飲品邏輯 (Beverage Logic)
*   **`calculate_order(price_list, cart)`**：
    *   **描述**：自動加總品項金額。
    *   **參數**：品項單價 + 附加料費用（珍珠 $10, 椰果 $5）。
    *   **結果**：產出格式化的小計與總金額。

*   **`stock_sync(item_id)`**：
    *   **描述**：連線庫存系統檢查當前茶湯與加料剩餘量。
    *   **結果**：傳回「充足」或「短缺，建議改點 [替代品]」。

## 🌤️ 外部環境 (Environment Intelligence)
*   **`weather_suggest(city)`**：
    *   **描述**：查詢即時天氣資訊。
    *   **結果**：溫度決策。

## 📊 報表與導出 (Export)
*   **`generate_invoice_json(order)`**：
    *   **描述**：訂單轉換為廚房 JSON 格式。
