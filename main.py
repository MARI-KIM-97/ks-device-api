from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 요청 body 모델 정의
class SearchRequest(BaseModel):
    deviceName: str

# 임시 시험조건 데이터베이스 (추후 DB 연결 가능)
mock_db = {
    "에어컨": "절연 시험 500V DC, 누설전류 시험 1mA 이하",
    "세탁기": "방수 시험, 절연 시험 1000V",
    "전자레인지": "내열 시험, 절연 시험 1500V",
}

# 시험조건 검색 API
@app.post("/api/search")
async def search_device(request: SearchRequest):
    device = request.deviceName
    result = mock_db.get(device, "해당 장치에 대한 시험조건 정보가 없습니다.")
    return {"result": result}
