# NoahCoal Texture Pack 🎮✨  
Minecraft Bedrock Edition 專用的高品質社群材質與音效包

---

## 🌟 專案簡介

NoahCoal 是由玩家社群共同打造的 Minecraft 基岩版材質包，結合 **精緻材質圖、沉浸式音效** 與自動化打包系統，讓你更方便參與製作、套用與分享。

---

## 📂 專案架構

```

NoahCoal-texture-pack/
├── pack.bat                  ← 一鍵執行主腳本（語言選擇＋打包＋匯入）
├── src/                      ← 資源包主體（textures、sounds、manifest.json 等）
├── builds/                   ← 自動儲存的歷史 .mcpack 檔案
└── functions/
   ├── main.py               ← 負責更新 UUID 並打包 src 為 .mcpack
   ├── get\_version.py        ← 顯示目前版本
   └── bump\_version.py       ← 升級版本（正式 / hotfix）

```

---

## 🚀 如何一鍵打包並匯入 `.mcpack`

### ✅ 使用步驟

1. 編輯 `src/` 資料夾內的內容（加入材質、音效等）
2. **雙擊執行 `pack.bat`**
3. 依照指示操作：
   - 選擇語言（繁體中文 / English）
   - 是否升級版本（正式版 / hotfix / 維持原版本）
   - 是否保留 `.mcpack` 檔案
   - 是否清除歷史檔案
4. `.mcpack` 將自動打包、匯入並啟動 Minecraft

---

## 🧰 自動化腳本說明

| 腳本檔案 | 功能 |
|----------|------|
| `pack.bat` | 主控制腳本（雙語介面，整合以下所有流程） |
| `functions/main.py` | 打包 `src/` 為 `.mcpack` 並隨機更新 UUID |
| `functions/get_version.py` | 顯示目前版本（含 hotfix 標記） |
| `functions/bump_version.py` | 升級正式版或 hotfix，並更新 `manifest.json` |

---

## 🔧 版本控制方式

| 類型 | 行為 | 範例版本 |
|------|------|----------|
| 正式版（release） | 第二位數 +1，尾數歸零 | V9 → V10 |
| Hotfix | 尾數 +1，並加註 `(hotfix vX)` | V10 → V10 (hotfix v1) |

版本資訊自動套用於：
- `manifest.json > header.version`
- `manifest.json > modules[0].version`
- `manifest.json > header.name`（會加入 `§n (hotfix vX)` 標記）

---

## 🎨 如何貢獻材質與音效

### 📁 對應資料夾

| 類型 | 路徑 | 格式建議 |
|------|------|----------|
| 方塊材質 | `src/textures/blocks/` | `.png` 16x16、32x32、64x64 |
| 道具材質 | `src/textures/items/` | `.png` |
| UI 圖示 | `src/textures/ui/` | `.png` |
| 音效檔案 | `src/sounds/` | `.ogg`（96kbps 以上） |

### 📝 投稿流程

1. Fork 本專案並建立分支
2. 將資源加入 `src/` 對應目錄
3. 可選擇加上預覽圖至 `assets/previews/`
4. 提交 Pull Request，等待審核合併！

---

## 💡 常見問題 FAQ

### Q1：匯入 `.mcpack` 後沒有生效？
- 請確認 Minecraft 是否啟用該資源包，並位於最上層
- 嘗試重啟 Minecraft 或清除快取

### Q2：如何辨別版本號？
- 顯示格式為：`V9`（正式版）或 `V9 (hotfix:1)`
- 所有版本資訊來自 `manifest.json` 並由腳本自動更新

### Q3：可以支援 Java Edition 嗎？
本專案針對 **Bedrock Edition** 開發。如需轉為 Java 請自行手動轉換與調整材質尺寸與結構。

---

## 📄 授權條款

本專案採用 **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh_TW)** 授權：

- ✅ 允許分享與修改
- ❌ 禁止商業用途
- 📌 修改後需採用相同授權並標示原作者

---

## 🌟 支持與參與

如果你喜歡這個專案：
- ⭐ 給我們一個 Star
- 🧠 加入我們，一起設計材質與音效
- 🪄 分享給你的 Minecraft 朋友們！

---

🧊 **Made with ❤️ by [@Squl032](https://github.com/Squl032) and Minecraft Community**
