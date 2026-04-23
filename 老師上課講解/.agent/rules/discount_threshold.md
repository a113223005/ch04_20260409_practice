---
trigger: always_on
---

---
功能名稱: 天下茶屋滿額折抵規則 (Discount Threshold)
版本編號: v1.0.0
修改日期: 2026-04-23
功能類型: 業務執行規則
內容描述: 定義顧客訂單達到金額門檻後的自動折抵邏輯。
---

# 業務規則：滿額折抵 (Discount Threshold)

## 進階實作規格 (AI好理解版)

### 折抵決策表 (Threshold Matrix)

| 條件 | 折抵金額 |
| :--- | :--- |
| `total >= 1000` | `floor(total / 1000) × 100` |
| `total < 1000` | `0` |