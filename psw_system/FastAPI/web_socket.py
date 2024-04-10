import socket
def socket_sousin(class_name,psw):
# 送信先のIPアドレスとポート番号
    server_ip = '100.85.35.80'
    server_port = 5000  # 適切なポート番号に変更

    # ソケットの作成
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # サーバーに接続
    client_socket.connect((server_ip, server_port))

    # サーバーにデータを送信
    #message = "Hello, Server!"
    message=class_name + ":"+psw
    client_socket.sendall(message.encode())

    # ソケットを閉じる
    client_socket.close()
socket_sousin("test","1234")