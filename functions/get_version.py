import json
import sys
import re
import os

# 啟用 Windows 控制台的 ANSI 支援
os.system('')

# Minecraft 顏色代碼對應 ANSI 轉義序列
MC_COLORS = {
    # 顏色碼（官方 + 擴充，避免使用 m, n 作為顏色碼）
    '§0': '\033[30m',  '§1': '\033[34m',  '§2': '\033[32m',  '§3': '\033[36m',
    '§4': '\033[31m',  '§5': '\033[35m',  '§6': '\033[33m',  '§7': '\033[37m',
    '§8': '\033[90m',  '§9': '\033[94m',  '§a': '\033[92m',  '§b': '\033[96m',
    '§c': '\033[91m',  '§d': '\033[95m',  '§e': '\033[93m',  '§f': '\033[97m',
    # 格式碼（單獨定義）
    '§k': '\033[5m',   # 閃爍
    '§l': '\033[1m',   # 粗體
    '§m': '\033[9m',   # 刪除線
    '§n': '\033[4m',   # 底線
    '§o': '\033[3m',   # 斜體
    '§r': '\033[0m',   # 重置
    # 擴充顏色碼，改用不衝突字元，如 §x, §y 等
    '§g': '\033[38;5;136m',  # 深黃色
    '§j': '\033[38;5;94m',   # 深咖啡色
    '§p': '\033[38;5;130m',  # 更深的黃色
    '§q': '\033[38;5;22m',   # 深綠色
    '§s': '\033[38;5;30m',   # 深水藍色
    '§t': '\033[38;5;19m',   # 深藍色
    '§u': '\033[38;5;54m',   # 深紫色
    '§v': '\033[38;5;166m',  # 橘色
    # 將原本用於顏色的 §m, §n 移除或換成其他代碼避免衝突
}

def apply_mc_colors(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+2] in MC_COLORS:
            result += MC_COLORS[text[i:i+2]]
            i += 2
        else:
            result += text[i]
            i += 1
    return result + '\033[0m'  # 重置顏色

with open("src/manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)
name = manifest["header"]["name"]
version_array = manifest["header"]["version"]

lang = "en"
if len(sys.argv) > 1 and sys.argv[1] == "zh":
    lang = "zh"

# 只擷取 V9 這類版本號
match = re.search(r'V\d+', name)
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