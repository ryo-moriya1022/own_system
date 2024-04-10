import socket

def get_server_ip(server_name):
    try:
        # サーバーのIPアドレスを取得
        ip_address = socket.gethostbyname(server_name)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None

# サーバー名を指定
server_name = '100.85.35.80'  # 実際のサーバー名に置き換えてください

# サーバーのIPアドレスを取得
server_ip = get_server_ip(server_name)

if server_ip:
    print(f"The IP address of {server_name} is {server_ip}")
else:
    print(f"Failed to retrieve the IP address of {server_name}")
