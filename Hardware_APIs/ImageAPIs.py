import uuid

from arrow import now
from fastapi import FastAPI, UploadFile, File
import os

from Data.ImageService import Image_Service

app = FastAPI()


@app.get("/api")
def read_root():
    return {"message": "Helloooo, World!"}


@app.post("/api/upload/image/")
async def upload_file(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"

    # Đọc nội dung file
    contents = await file.read()

    imageDir = r"D:\Code\PBL4\Server_Backend_API\wwwroot\Images"

    os.makedirs(imageDir, exist_ok=True)

    file_path = os.path.join(imageDir, file.filename)

    image_sv = Image_Service()
    image_sv.insertImage(file.filename,now)


    with open(file_path, "wb") as f:
        f.write(contents)

    return {"filename": file.filename}
# sad