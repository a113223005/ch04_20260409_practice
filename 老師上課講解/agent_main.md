---
功能名稱: 英雄茶屋智慧 Agent 主控台 (System Map)
版本編號: v1.0.1
修改日期: 2026-03-28
功能類型: 系統管理地圖
內容描述: 負責連結與管理所有大腦規劃組件 (P-R-W-S) 之入口文件。
---

# 專案主控台：英雄茶屋智慧 Agent 系統

本文件為專案的「思維入口」，負責鏈結 `.agent/` 目錄下的所有核心規劃組件（P-R-W-S）。系統將依據此地圖讀取對應之性格、規則與流程。

## 1. 角色設定 (Persona)

- [./.agent/persona.md](./.agent/persona.md)
- **內容包含**：明確店長的身份、溝通風格與品牌背景。

## 2. 業務規則 (Rules)

- [./.agent/rules/topping_limit.md](./.agent/rules/topping_limit.md) (熱飲限制規則)
- **內容包含**：飲品規格邏輯、品質攔截與訂購門檻。

## 3. 實作能力 (Skills)

- [./.agent/skills/](./.agent/skills/) (實作能力組件資料夾)
- **核心範例**：[calculate_total.md](./.agent/skills/calculate_total.md) (訂單金額運算規格)
- **內容包含**：金額加總、庫存同步與外部環境偵測。

## 4. 運作流程 (Workflows)

- [./.agent/workflows/order_beverage.md](./.agent/workflows/order_beverage.md) (點餐標準程序)
- **內容包含**：標準點餐 SOP、決策路徑與異常應對流程。
