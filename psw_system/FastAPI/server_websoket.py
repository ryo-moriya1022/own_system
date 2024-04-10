import socket
def main():
    # サーバーのIPアドレスとポート番号
    server_ip = 'localhost'  # 任意のIPアドレスまたは 'localhost'
    server_port = 5000  # クライアントと同じポート番号

    # ソケットの作成
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # ソケットをIPアドレスとポートにバインド
    server_socket.bind((server_ip, server_port))

    # クライアントの接続を待ち受け
    server_socket.listen()

    print(f"Server listening on {server_ip}:{server_port}")

    # クライアントからの接続を受け入れ
    client_socket, client_address = server_socket.accept()

    # クライアントからのデータを受信
    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")

    # ソケットを閉じる
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()