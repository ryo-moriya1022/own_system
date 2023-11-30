import subprocess
import os

# パスをエスケープするか生文字列として扱う
directory_path = r"C:\Users\eva10\OneDrive\デスクトップ\創作物一覧\Zoom起動システム"

# Change the working directory
os.chdir(directory_path)

# Run the command in the updated working directory
subprocess.call('streamlit run display.py', shell=True)
