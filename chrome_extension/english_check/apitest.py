import requests

# APIキーとエンドポイントの設定
api_key = "AIzaSyC_MgvIo7ulAkU7HtqMubb0EeAkFiBIFyA"
endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + api_key

# 送信するデータの準備
data = {
    "contents": [{
        "parts":[{
        "text": """今から英文を提出します。正しい英語か確認してください。もし違う場合は違う理由と修正した文章を一緒に教えてください。
                I was going to do to eating, but I didn't finish the home work"""
        }]
    }]
}

# APIにリクエストを送信
headers = {
    "Content-Type": "application/json"
}
response = requests.post(endpoint, json=data, headers=headers)

# レスポンスの処理
if response.status_code == 200:
    print("APIリクエストが成功しました。")
    print("Response:")
    print(response.json())
else:
    print(f"APIリクエストが失敗しました。ステータスコード: {response.status_code}")
    print("Response:")
    print(response.text)
