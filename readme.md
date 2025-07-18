# NoahCoal Texture Pack 🎮🎨  
一款針對 Minecraft 基岩版 (Bedrock Edition) 打造的社群驅動材質與音效包

![NoahCoal Logo](https://github.com/Squl032/NoahCoal-texture-pack/blob/main/src/pack_icon.png?raw=true)

---

## 🧱 專案宗旨

NoahCoal 是一款由玩家社群驅動的 Minecraft Bedrock 材質與音效包，致力於提供 **清新、細膩、沉浸感強烈** 的遊戲體驗。我們歡迎各方玩家投稿材質、音效、UI 圖像，讓這個資源包成為社群共同打造的作品！

---

## 📦 支援版本

- 平台：Minecraft Bedrock Edition（基岩版）
- 最低版本支援：v1.20+
- 檔案格式：`.mcpack`

---

## 🎨 如何貢獻材質與音效

我們鼓勵社群成員貢獻優質資源，以下是投稿流程與規範：

### ✅ 投稿流程

1. Fork 此專案並建立你的分支（例如：`add-new-ores-texture`）。
2. 將你的資源加入對應資料夾：
   - 材質：`textures/blocks/`、`textures/items/`
   - 音效：`sounds/` 內對應資料夾（如 `sounds/mob/`）
3. 如有需要，編輯 `manifest.json` 更新作者資訊。
4. 提交 Pull Request，附上修改說明與預覽圖（可放在 `assets/previews/`）。
5. 待審核合併後，你的作品就會成為正式內容！

### 📏 資源規範

| 類別 | 格式 | 推薦尺寸 | 命名建議 |
|------|------|----------|----------|
| 材質圖 | `.png` | `16x16` / `32x32` / `64x64` | 沿用原始 Minecraft 檔名 |
| 音效 | `.ogg` | 96kbps+ 建議 | 保持與原始檔名一致 |
| UI 圖像 | `.png` | 根據 Minecraft UI 尺寸需求 | 例如：`textures/ui/pack_icon.png` |

> 建議使用工具：Blockbench（3D 模型與材質）、Aseprite（像素圖）、Audacity（音效處理）

---

## 🚀 一鍵自動打包 `.mcpack`

我們已提供自動化工具，讓你無需手動壓縮與改檔名！

### 🛠️ 使用方法

1. **準備好你的修改內容**（材質、音效等）
2. **雙擊執行根目錄下的 [`pack.bat`](./pack.bat)**
3. 程式會自動：
   - 打包 `.mcpack`
   - 安裝至你的 Minecraft 資源包資料夾
   - 開啟 Minecraft 供你測試

> ⚠️ 注意：第一次執行會需要 Python 環境，如未安裝請前往 https://www.python.org 下載。

### 🔎 pack.bat 做了什麼？

- 呼叫 `functions/main.py` 腳本進行打包處理
- 自動生成 UUID 與時間戳（如需要）
- 拷貝並安裝 `.mcpack` 到 Minecraft 對應資料夾
- 可依照個人需求修改 `functions/pack.py` 腳本進行進階設定

---

## 💡 附加小技巧

- 編輯完 `manifest.json` 後，建議使用 JSON 檢查工具以避免語法錯誤
- 測試材質沒變化時請：
  - 清除快取
  - 調整材質包順序
  - 重啟 Minecraft

---

## 👥 貢獻者名單

| 名稱 | 貢獻項目 |
|------|----------|
| [@Squl032](https://github.com/Squl032) | 專案創建 / 自動打包工具開發 |
| [@NoahKuowithme](https://github.com/NoahKuowithme) | 材質、音效、翻譯等貢獻 |

---

## 📄 授權與使用條款

本專案採用 **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh_TW)** 授權：

- ✅ 可自由修改與分享
- ❌ 禁止商業用途
- 🔁 修改後須同樣採用相同授權，並註明原作者

---

## ❓ 常見問題 FAQ

### Q1：為什麼我安裝後沒看到變化？
請確認是否重啟 Minecraft，並將材質包設定為「啟用中」且位於最上方優先順序。

### Q2：如何新增材質給生物或方塊？
請根據 Minecraft 原始資源包的檔名，加入對應的 `.png` 至 `textures/blocks/` 或 `textures/entity/` 目錄下。

### Q3：Python 是必要的嗎？
是的，若你要使用自動打包功能，必須安裝 Python。手動打包也可以參考舊方法。

---

## ⭐ 支持與參與

如果你喜歡這個專案，請幫我們按下 Star 🌟，或是分享給其他 Minecraft 玩家。也歡迎提交你的作品，一起讓 NoahCoal 更豐富！

---

🧊 **Made with ❤️ by Minecraft 社群**
