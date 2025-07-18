import json
import sys

manifest_path = "src/manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

version = manifest["header"]["version"]
hotfix = False

lang = "en"
if len(sys.argv) > 2 and sys.argv[2] == "zh":
    lang = "zh"

if len(sys.argv) > 1 and sys.argv[1] == "hotfix":
    # 移除舊的 hotfix 標記（避免重複）
    old_tag = f"§n (hotfix v{version[2]})"
    manifest["header"]["name"] = manifest["header"]["name"].replace(old_tag, "")

    # hotfix: increment最後一位
    version[-1] += 1
    hotfix = True

    # 加上新的 hotfix 標記
    new_tag = f"§n (hotfix v{version[2]})"
    manifest["header"]["name"] += new_tag
else:
    # release: 增加第二位，重置最後一位
    version[1] += 1
    version[2] = 0

manifest["header"]["version"] = version
manifest["modules"][0]["version"] = version

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=4)

if hotfix:
    if lang == "zh":
        print(f"已推進 hotfix 版本: {version}")
    else:
        print(f"Advanced hotfix version: {version}")
else:
    if lang == "zh":
        print(f"已推進正式版本: {version}")
    else:
        print(f"Advanced release version: {version}")