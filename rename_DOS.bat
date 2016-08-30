@echo off
setlocal enabledelayedexpansion
mkdir RENAMED_FOLDER
set count=0
set sdf=0
for %%x in (*) do set /a count+=1
for /F "delims=" %%x in ('dir /B/D *.jpg *.png *.bmp *.jpeg *.mov *.wmv *.mp4 *.3gp') do (
	for /f "tokens=* delims=" %%i in ('exiftool "%%x" ^| findstr /i modification') do (set line=%%i)
	echo !line!
	for /f "tokens=* delims=" %%j in ('dir "%%x" ^| findstr "\.jpg \.bmp \.png \.jpeg \.mov \.wmv \.mp4 \.3gp"') do (set ext=%%j)
	echo !ext!
	if !ext:~-4!==jpeg (set ext=!ext:~-4!) else (set ext=!ext:~-3!)
	echo !ext!
	set year=!line:~34,4!
	set month=!line:~39,2!
	set day=!line:~42,2!
	set hour=!line:~45,2!
	set minute=!line:~48,2!
	set sec=!line:~51,2!
	echo "%%x" to "!year!-!month!-!day! !hour!.!minute!.!sec!.!ext!"
	ren "%%x" "!year!-!month!-!day! !hour!.!minute!.!sec!.!ext!"
	move "!year!-!month!-!day! !hour!.!minute!.!sec!.!ext!" RENAMED_FOLDER
	set /a sdf+=1
	echo !sdf!/!count!
)
endlocal
