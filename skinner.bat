@echo off
set /p original="Original image path: "
set /p skinned="Skinned image destination path (must end in .png): "
python -m skinner %original% %skinned%
if errorlevel 0 (
    echo Wrote skinned image to %skinned%
)