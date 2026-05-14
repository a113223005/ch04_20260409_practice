# 前端開發規範：Turso 雲端資料庫整合

## 規範目標
確保所有前端頁面具備直接與 Turso 雲端資料庫通訊並寫入資料的能力，以實現前端直連的持久化 (Persistence) 架構。

## 實作守則
1. **引入 LibSQL SDK**：所有前端 HTML 頁面，必須在 `<head>` 區塊內引入能連接 Turso 雲端資料庫的 **LibSQL Web Client SDK**。
2. **版本要求**：請選用穩定且適合瀏覽器環境使用的 CDN 版本（例如 `@libsql/client-web` 或相關官方建議的 Web SDK CDN）。

請在任何涉及 HTML 結構修改時，嚴格遵守此規範。
