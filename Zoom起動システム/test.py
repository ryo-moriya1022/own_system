import psutil

target_port = 8501

for process in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        if process.info['cmdline'] is not None and str(target_port) in ' '.join(map(str, process.info['cmdline'])):
            pid = process.info['pid']
            print(f"プロセス {pid} - {process.info['name']} を終了しています。")
            psutil.Process(pid).terminate()
    except Exception as e:
        print(f"エラーが発生しました: {e}")

print("すべてのlocalhostプロセスが終了しました。")
