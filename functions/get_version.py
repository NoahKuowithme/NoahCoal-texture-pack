import json
import sys
import re
import os

# 啟用 Windows 控制台的 ANSI 支援
os.system("")

# Minecraft 顏色代碼對應 ANSI 轉義序列
MC_COLORS = {
    # 官方基本顏色 (§0 ~ §f)
    "§0": "\033[30m",  # 黑
    "§1": "\033[34m",  # 深藍
    "§2": "\033[32m",  # 深綠
    "§3": "\033[36m",  # 青色
    "§4": "\033[31m",  # 深紅
    "§5": "\033[35m",  # 紫色
    "§6": "\033[33m",  # 金色
    "§7": "\033[37m",  # 淺灰
    "§8": "\033[90m",  # 深灰
    "§9": "\033[94m",  # 藍
    "§a": "\033[92m",  # 綠
    "§b": "\033[96m",  # 淺藍
    "§c": "\033[91m",  # 紅
    "§d": "\033[95m",  # 淺紫
    "§e": "\033[93m",  # 黃
    "§f": "\033[97m",  # 白
    # 格式碼
    "§k": "\033[5m",  # 閃爍
    "§l": "\033[1m",  # 粗體
    "§m": "\033[9m",  # 刪除線 (你說 §m 是深紅色，但 §m 原本是刪除線，這裡特別處理)
    "§n": "\033[4m",  # 底線 (你說 §n 是淺咖啡色，這裡另外新增顏色)
    "§o": "\033[3m",  # 斜體
    "§r": "\033[0m",  # 重置
    # 你提供的額外顏色 (用 256 色碼近似)
    "§g": "\033[38;5;136m",  # 深黃色 (色碼136，類似金黃)
    "§j": "\033[38;5;94m",  # 深咖啡色 (色碼94，深棕色)
    "§m": "\033[38;5;124m",  # 深紅色 (色碼124，比紅色更深)
    "§n": "\033[38;5;180m",  # 淺咖啡色 (色碼180，米棕色)
    "§p": "\033[38;5;130m",  # 比§g更深的黃色 (色碼130，深金黃)
    "§q": "\033[38;5;22m",  # 深綠色 (色碼22，森林綠)
    "§s": "\033[38;5;30m",  # 深水藍色 (色碼30，深青色)
    "§t": "\033[38;5;19m",  # 深藍色 (色碼19，深海軍藍)
    "§u": "\033[38;5;54m",  # 深紫色 (色碼54，深紫羅蘭)
    "§v": "\033[38;5;166m",  # 橘色 (色碼166，橘紅色)
}


def apply_mc_colors(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i : i + 2] in MC_COLORS:
            result += MC_COLORS[text[i : i + 2]]
            i += 2
        else:
            result += text[i]
            i += 1
    return result + "\033[0m"  # 重置顏色


with open("src/manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)
name = manifest["header"]["name"]
version_array = manifest["header"]["version"]

lang = "en"
if len(sys.argv) > 1 and sys.argv[1] == "zh":
    lang = "zh"

# 只擷取 V9 這類版本號
match = re.search(r"V\d+", name)
if match:
    base_version = match.group(0)
    # 如果最後一位不是0，表示是hotfix版本
    if version_array[2] != 0:
        version = f"{base_version} (hotfix:{version_array[2]})"
    else:
        version = base_version
else:
    version = name

if lang == "zh":
    msg = f"目前版本：{apply_mc_colors(version)}"
else:
    msg = f"Current version: {apply_mc_colors(version)}"

print(msg)
