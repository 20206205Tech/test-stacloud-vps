from fastapi import FastAPI

# Khởi tạo ứng dụng
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "STACloud", "Status": "Running"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# Lưu ý: Trên Pterodactyl, bạn thường chạy qua command startup 
# hoặc thêm đoạn code dưới đây nếu muốn chạy trực tiếp bằng 'python main.py'
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=30005)


