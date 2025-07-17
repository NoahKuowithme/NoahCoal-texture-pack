@echo off
echo "正在打包最新的 Minecraft 資源包..."
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
<<<<<<< HEAD
=======
echo "正在匯入最新的資源包... 15 秒後自動刪除"

>>>>>>> 865bcd47e70cdeadddc8f9592ddf87aae4abb6c3
timeout /t 15

REM 刪除所有 .mcpack 檔案
del /q *.mcpack
pause 