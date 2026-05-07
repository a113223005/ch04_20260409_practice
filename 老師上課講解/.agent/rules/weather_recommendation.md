---
trigger: always_on
---

---
功能名稱: 氣候感測聯動推薦規則 (Weather-Based Rules)
版本編號: v1.0.0
修改日期: 2026-05-07
功能類型: 業務執行規則
內容描述: 根據「氣候感測技能」回傳的氣溫數據，動態調整飲品推薦邏輯。
---

# 業務規則：氣候感測聯動推薦 (Weather Recommendation)

## 進階實作規格

### 推薦決策表 (Recommendation Matrix)

| 觸發條件 (Condition) | 氣溫區間 | 推薦產品 (Primary) |
| :--- | :--- | :--- |
| **高溫** | `current_temp > 28` | 特調奶茶（冰） |
| **常溫** | `15 <= current_temp <= 28` | 天下紅茶 / 天下綠茶 |
| **低溫** | `current_temp < 15` | 天下紅茶（熱） |