@echo off
REM 執行 Python 打包腳本
python main.py

REM 等待 Python 執行完畢 (可視需要加入超時或延遲)

REM 找出當前資料夾中最新的 .mcpack 檔案
for /f "delims=" %%f in ('dir /b /a-d /o-d *.mcpack') do (
    set latest_mcpack=%%f
    goto found
)
:found

REM 用預設程式開啟最新的 mcpack
start "" "%latest_mcpack%"

REM 刪除所有 .mcpack 檔案
del /q *.mcpack