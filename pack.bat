@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion
:asklang
set /p lang=Select language / 選擇語言 (en=English/zh=繁體中文): 
if /i "!lang!"=="zh" goto lang_zh
if /i "!lang!"=="en" goto lang_en
echo Invalid input. Please enter en or zh.
goto asklang
:lang_zh
set msg_ver=顯示目前版本
set msg_upgrade=是否升級版本？(y=正式版/n=hotfix/Enter=維持):
set msg_keep=保留目前版本
set msg_pack=正在打包最新的 Minecraft 資源包...
set msg_import=正在匯入最新的資源包...
set msg_keepfile=是否保留已匯入檔案？(y=保留/n=刪除):
set msg_moved=已移至 builds 資料夾
set msg_deleted=已刪除所有 .mcpack 檔案
set msg_delbuilds=是否刪除 builds 內檔案？(y=全部/n=指定版本/Enter=不刪):
set msg_delall=已刪除 builds 中的所有檔案
set msg_delver=請輸入要刪除的版本號(如V9或V9-hotfix):
set msg_delverdone=已刪除指定版本的檔案
set msg_keepbuilds=保留 builds 中的檔案
goto lang_done
:lang_en
set msg_ver=Display current version
set msg_upgrade=Upgrade version? (y=release/n=hotfix/Enter=keep):
set msg_keep=Keeping current version
set msg_pack=Packing latest Minecraft resource pack...
set msg_import=Importing latest resource pack...
set msg_keepfile=Keep imported file? (y=keep/n=delete):
set msg_moved=Moved to builds folder
set msg_deleted=Deleted all .mcpack files
set msg_delbuilds=Delete files in builds? (y=all/n=specific version/Enter=none):
set msg_delall=Deleted all files in builds
set msg_delver=Enter version to delete (e.g. V9 or V9-hotfix):
set msg_delverdone=Deleted specified version files
set msg_keepbuilds=Keeping files in builds
goto lang_done
:lang_done
echo !msg_ver!
python functions\get_version.py
set /p bumpver=!msg_upgrade!
if /i "!bumpver!"=="y" (
    python functions\bump_version.py
) else if /i "!bumpver!"=="n" (
    python functions\bump_version.py hotfix
) else (
    echo !msg_keep!
)
echo !msg_pack!
python functions\main.py
set "latest_mcpack="
for /f "delims=" %%f in ('dir /b /a-d /o-d *.mcpack') do (
    set "latest_mcpack=%%f"
    goto found
)
:found
start "" "!latest_mcpack!"
echo !msg_import!
timeout /t 15
set /p keepfile=!msg_keepfile!
if /i "!keepfile!"=="y" (
    if not exist builds mkdir builds
    move "!latest_mcpack!" ".\builds\"
    echo !msg_moved!
) else (
    del /q *.mcpack
    echo !msg_deleted!
    set /p delbuilds=!msg_delbuilds!
    if /i "!delbuilds!"=="y" (
        del /q .\builds\*.mcpack
        echo !msg_delall!
    ) else if /i "!delbuilds!"=="n" (
        set /p ver=!msg_delver!
        del /q .\builds\*!ver!*.mcpack
        echo !msg_delverdone!
    ) else (
        echo !msg_keepbuilds!
    )
)
pause
endlocal