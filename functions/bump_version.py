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
    # hotfix: increment last digit
    version[-1] += 1
    hotfix = True
    # 在 name 後面加上 hotfix 標記
    manifest["header"]["name"] += f"§n (hotfix v{version[2]})"
else:
    # release: increment second digit, reset last digit
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