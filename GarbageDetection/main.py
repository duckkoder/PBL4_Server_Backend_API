from _datetime import datetime
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.models import load_model

from Data.ResultService import Result_Service
from Model.ResultDetection import ResultDetection


# Hàm dự đoán loại rác
def predict_waste_category(image_path, model):
    # Load và xử lý ảnh
    img = Image.open(image_path)
    img = img.resize((384, 512))  # Điều chỉnh kích thước ảnh theo kích thước đầu vào của mô hình
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Chuẩn hóa ảnh

    # Dự đoán loại rác
    prediction = model.predict(img_array)
    waste_categories = [ 'glass', 'metal', 'paper', 'plastic']
    predicted_category_index = np.argmax(prediction)
    predicted_category = waste_categories[predicted_category_index]
    # glass', 'metal', 'paper', 'plastic
    # Lấy xác suất dự đoán của loại rác
    probability = prediction[0][predicted_category_index]
    return predicted_category, probability

# Ví dụ sử dụng

basePath = 'D:\\Code\\PBL4\\Server_Backend_API\\wwwroot\\Images\\'
image_name = r"a.jpg"
image_path = basePath+ image_name
model_inception = load_model(r"D:\Code\PBL4\Server_Backend_API\GarbageDetection\garbage_classification_model_inception.h5")  # Load model đã lưu đúng cách
predicted_category, probability = predict_waste_category(image_path, model_inception)

result_detection = ResultDetection(
    imageName=image_name,
    result=predicted_category,
    dateCreated = datetime.now()
)

result_service = Result_Service()

result_service.insertResult(result_detection)

print("Predicted waste category:", predicted_category)
print("Probability:", probability)
# sad