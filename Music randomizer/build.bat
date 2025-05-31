@echo off
setlocal enabledelayedexpansion

echo Instalando PyInstaller se necessário...
pip install pyinstaller || (
    echo Erro ao instalar PyInstaller. Verifique se o Python está instalado corretamente.
    pause
    exit /b 1
)

echo Construindo o executável...
python -m PyInstaller --onefile --noconsole ^
    --add-data "Configs;Configs" ^
    --add-data "Music Categories;Music Categories" ^
    --add-data "Patches;Patches" ^
    --add-data "liteips.exe;." ^
    --name "FF6_Music_Randomizer" ^
    "FF6_Music_Randomizer.py"

if errorlevel 1 (
    echo Ocorreu um erro durante a compilação!
    pause
    exit /b 1
)

echo.
echo Build completo! O executável está em: dist\FF6_Music_Randomizer.exe
echo.
pause
