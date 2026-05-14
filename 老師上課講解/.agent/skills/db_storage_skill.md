---
功能名稱: 雲端資料庫存檔技能 (db_storage_skill)
功能類型: Skill
---

# 技能：雲端資料庫存檔 (Database Storage Skill)

## 1. 業務目標
賦予代理人透過 Database MCP 伺服器將訂單資料安全地存入 Turso 雲端資料庫的能力，實現系統資料持久化 (Persistence)。

## 2. 資料結構要求 (Schema)
目標寫入的表格為 `orders`，其結構定義如下：
- `id`: 整數 (Integer)，主鍵且自動遞增
- `order_id`: 字串 (String)，訂單專屬編號
- `item_name`: 字串 (String)，飲品品項名稱
- `qty`: 整數 (Integer)，購買數量
- `unit_price`: 整數 (Integer)，單價
- `subtotal`: 整數 (Integer)，小計總額
- `created_at`: 時間戳記 (Timestamp)，系統自動產生寫入時間

## 3. 實作規範與 SQL 邏輯

執行此技能時，請呼叫名為 `database` 的 MCP 伺服器，並依序完成以下指令：

### A. 初始化表格 (若表格不存在則建立)
每次寫入前請確保資料表已經存在，請先執行以下 DDL 語法：
```sql
CREATE TABLE IF NOT EXISTS orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id TEXT NOT NULL,
  item_name TEXT NOT NULL,
  qty INTEGER NOT NULL,
  unit_price INTEGER NOT NULL,
  subtotal INTEGER NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### B. 寫入訂單資料 (參數綁定)
請提取 Workflow 傳遞過來的訂單結帳資訊，並將其映射至參數，執行以下 SQL 語法寫入資料庫：
```sql
INSERT INTO orders (order_id, item_name, qty, unit_price, subtotal)
VALUES (:order_id, :item_name, :qty, :unit_price, :subtotal);
```
*(請確保引數型態與欄位要求一致)*
