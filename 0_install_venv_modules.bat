:: Clone git and mode dir for models
git clone -v https://github.com/Stability-AI/stablediffusion.git

:: Install and activate venv
python -m venv venv
CALL %~dp0%venv\Scripts\activate.bat

:: Install base modules
python.exe -m pip install --upgrade pip
pip install torch torchvision==0.13.1 torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
pip install transformers==4.19.2 diffusers invisible-watermark timm
cd %~dp0%stablediffusion\
pip install -r requirements.txt
cd ..

pause