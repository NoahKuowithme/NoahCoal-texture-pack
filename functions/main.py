import os
import zipfile
import json
import uuid
import sys

def get_non_conflicting_filename(base_path):
    if not os.path.exists(base_path):
        return base_path

    base, ext = os.path.splitext(base_path)
    i = 1
    new_path = f"{base} ({i}){ext}"
    while os.path.exists(new_path):
        i += 1
        new_path = f"{base} ({i}){ext}"
    return new_path

def update_manifest_uuid(manifest_path):
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    # 隨機產生新的 uuid
    manifest["header"]["uuid"] = str(uuid.uuid4())
    if "modules" in manifest and len(manifest["modules"]) > 0:
        manifest["modules"][0]["uuid"] = str(uuid.uuid4())
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=4)

def zip_folder_to_mcpack(folder_path, output_path, lang="en"):
    output_path = get_non_conflicting_filename(output_path)
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path+1:])
    if lang == "zh":
        print(f"已生成 {output_path}")
    else:
        print(f"Generated {output_path}")

if __name__ == "__main__":
    folder = "src"
    output_file = "NoahPack.mcpack"
    # 先更新 manifest.json 的 uuid
    manifest_path = os.path.join(folder, "manifest.json")
    update_manifest_uuid(manifest_path)
    lang = "en"
    if len(sys.argv) > 1 and sys.argv[1] == "zh":
        lang = "zh"
    zip_folder_to_mcpack(folder, output_file, lang)