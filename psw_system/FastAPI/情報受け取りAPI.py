from fastapi import FastAPI

app = FastAPI()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://gindflfccbmpmimonmagcpolnkcmfhnd"],  # すべてのオリジンを許可する場合（セキュリティ上の注意が必要）
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可する場合
    allow_headers=["*"],  # すべてのヘッダーを許可する場合
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": f"APIのid:{item_id}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
