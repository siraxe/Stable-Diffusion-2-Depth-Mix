CALL %~dp0%venv\Scripts\activate.bat

git clone https://github.com/facebookresearch/xformers.git
cd xformers
git submodule update --init --recursive
pip install -r requirements.txt
pip install -e .
cd ..

pause