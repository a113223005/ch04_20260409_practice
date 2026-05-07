---
description: 
---

# 工作流程：天下茶屋飲品點購程序 (Order SOP)

## 1. 基礎實作規劃 (人類好閱讀版)

本流程規定了 App 系統如何一步步協助顧客完成下單：

## 進階實作規格

為確保流程之一致性，定義下列狀態位移：

### 系統執行狀態表 (State Transitions)

| 階段序號 | 執行動作名稱 | 動作內容描述 | 關鍵產出數據 |
| :--- | :--- | :--- | :--- |
| **S1** | **Query_Intent** | 向用戶進行需求採集 | 品項、數量、溫標 |
| **S2** | **Validate_Policy** | 執行業務規則校驗 | 是否合規標籤 (True/False) |
| **S3** | **Calc_Price** | 執行金額自動計算 | 最終實付總額 (Net_Total) |
| **S4** | **Confirm_Order** | 產出訂單摘要 | 支付連結、訂單序號 |
| **S5（自動通知）** | 先通過 `notification_consent` 檢查權限，通過後將 Persona 產生的「推播內容」傳遞給 `line_messaging_skill` 進行發送 |