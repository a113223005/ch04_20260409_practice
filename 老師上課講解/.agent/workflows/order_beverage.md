---
description: 
---

---
功能名稱: 智慧點餐 SOP 流程 (Order Beverage Workflow)
版本編號: v1.0.0
修改日期: 2026-04-23
功能類型: 操作流程 / SOP
內容描述: 定義天下茶屋智慧 App 自「App 啟動」到「訂單送出」的完整操作流程，串接 Persona、Rules、Skills 與 Knowledge 四大元件。
---


# 工作流程：天下茶屋飲品點購程序 (Order SOP)

## 1. 基礎實作規劃 (人類好閱讀版)

本流程規定了 App 系統如何一步步協助顧客完成下單：

## 進階實作規格

為確保流程之一致性，定義下列狀態位移：

### 狀態轉換表 (State Transition Matrix)

| 狀態 (State) | 觸發事件 (Trigger) | 執行動作 (Action) | 下一狀態 |
| :--- | :--- | :--- | :--- |
| **S0** | App 啟動 | 調用 `get_weather_skill` → 套用 `weather_recommendation` → 生成開場白 | S1 |
| **S1** | 顧客選品項 | 記錄 `item_code, qty, temp` | S2 |
| **S2** | 送出選擇 | 執行 `delivery_threshold` 校驗 | 通過 → S3；失敗 → 回 S1 |
| **S3** | 進入結帳 | 調用 `calculate_total` 計算 `final_total` | S4 |
| **S4** | 顧客確認 | 產出訂單編號並結帳 | S5 |
| **S5** | 自動通知 | 執行 `line_messaging_skill` 進行推播 | S6 |
| **S6** | 雲端存檔 | 執行 `db_storage_skill` 寫入資料庫 | 結束 |

### 系統執行狀態表 (State Transitions)

| 階段序號 | 執行動作名稱 | 動作內容描述 | 關鍵產出數據 |
| :--- | :--- | :--- | :--- |
| **S1** | **Query_Intent** | 向用戶進行需求採集 | 品項、數量、溫標 |
| **S2** | **Validate_Policy** | 執行業務規則校驗 | 是否合規標籤 (True/False) |
| **S3** | **Calc_Price** | 執行金額自動計算 | 最終實付總額 (Net_Total) |
| **S4** | **Confirm_Order** | 產出訂單摘要 | 支付連結、訂單序號 |
| **S5** | **Line_Notify** | 通過 `notification_consent` 檢查權限後，將 Persona 產生的推播內容傳遞給 `line_messaging_skill` 進行發送 | 推播結果狀態 |
| **S6** | **Persistence** | 當訂單確認且結帳成功後，呼叫 `db_storage_skill`，將本次交易的所有品項存至 Turso 雲端 | 回饋使用者「您的訂單已安全存入雲端資料庫」 |