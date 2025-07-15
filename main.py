import os
import zipfile

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

def zip_folder_to_mcpack(folder_path, output_path):
    output_path = get_non_conflicting_filename(output_path)
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path+1:])
    print(f"已生成 {output_path}")

if __name__ == "__main__":
    folder = "src"
    output_file = "NoahPack.mcpack"
    zip_folder_to_mcpack(folder, output_file)