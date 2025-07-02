@echo off
cd /d "%~dp0"
echo Iniciando o Previsor de Vendas...
py -m streamlit run interface.py

pause
