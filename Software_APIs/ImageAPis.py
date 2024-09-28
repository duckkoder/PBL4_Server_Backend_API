import uuid
from fastapi import FastAPI, UploadFile, File, HTTPException
from Data.ImageService import Image_Service
from Model import ImageViewModel

app = FastAPI()


@app.get("/Image/{filePath}")
def getImage(filePath: str):
    image_sv = Image_Service()
    try:
        data = image_sv.get_Image(filePath)
        if data is None:
            raise HTTPException(status_code=404, detail="Image not found")
        return image_view_model
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



