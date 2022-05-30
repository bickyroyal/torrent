@echo off
if [%1] == [] exit
if [%1] == [%cd%\Films] exit
if [%1] == [%cd%\Films\subtitles] exit
for %%a in (%1) do set "parent=%%~dpa"
for /r %1 %%f in (*.mp4 *.mkv) do @move "%%f" "%parent%\Films"
for /r %1 %%f in (*.srt *.sub) do @move "%%f" "%parent%\Films\subtitles"
RMDIR /S /Q %1
