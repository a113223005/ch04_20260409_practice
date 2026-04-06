---
功能名稱: 手搖飲 Agent 訂單工作流 (Workflow)
版本編號: v1.0.1
修改日期: 2026-03-28
描述: 定義 Agent 的具體執行步序、決策邏輯與流程圖渲染。
---

# 🔄 訂飲料工作流 (Beverage Order Workflow)

本工作流定義了 Agent 接到點餐指令後的操作邏輯步序。

## 📍 流程定義 (Step by Step)

### 1. 需求分析 (Input Analysis)
*   **動作**：解析用戶輸入。
*   **分支**：若細節不足，立即反向詢問。

### 2. 資料對應與庫存檢查 (Stock Check)
*   **動作**：調用 **`stock_sync`** 與溫度邏輯。

### 3. 金額計算 (Calculation)
*   **動作**：調用 **`calculate_order`**。

### 4. 最終確認與傳送 (Final Confirmation)
*   **動作**：產出 JSON 給予廚房。

---

## 📈 流程圖 (Mermaid)

```mermaid
graph LR
    Start[需求分析] --> Options{指標細項?}
    Options -- 缺失條件 --> Ask[詢問對應條件]
    Ask --> Options
    Options -- 條件齊全 --> Stock{庫存檢查}
    Stock -- 充足 --> Calc[金額計算]
    Calc --> FinalConfirm{訂單確認}
    FinalConfirm -- 修改 --> Options
    FinalConfirm -- 送出 --> OrderSent[廚房 JSON 產出]
```
