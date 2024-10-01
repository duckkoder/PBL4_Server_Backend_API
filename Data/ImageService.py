import pyodbc
from ConnectDataBase import Connect_Db
from Model import ImageViewModel

class Image_Service:
    def __init__(self):
        self.dbContext = Connect_Db()  # dbContext là một instance của ConnectDb
        self.dbContext.connect()    # Kết nối tới cơ sở dữ liệu khi khởi tạo

    def get_Image(self, filePath):
        try:
            query = "SELECT dateCreated, filePath FROM Images WHERE filePath = ?"
            self.dbContext.cursor.execute(query, (filePath,))
            result = self.dbContext.cursor.fetchone()  # Lấy một kết quả duy nhất

            if result is None:
                print(f"Không tìm thấy hình ảnh với filePath: {filePath}")
                return None

            # Giả sử kết quả chứa 2 cột: dateCreated và filePath
            date_created, file_path = result
            image = ImageViewModel(
                dateCreated=date_created,
                filePath=file_path
            )
            return image
        except pyodbc.Error as e:
            print(f"Lỗi khi lấy Image: {e}")
            return None

    def insertImage(self, filePath, dateCreated):
        try:
            query = "INSERT INTO Images (filePath, dateCreated) VALUES (?, ?)"
            self.dbContext.cursor.execute(query, (filePath, dateCreated))
            self.dbContext.conn.commit()
            print("Insert Image thành công.")
        except pyodbc.Error as e:
            print(f"Lỗi khi Insert Image: {e}")

    def fetchImages(self):
        try:
            query = "SELECT * FROM Images"
            self.dbContext.cursor.execute(query)
            records = self.dbContext.cursor.fetchall()
            return records
        except pyodbc.Error as e:
            print(f"Lỗi khi lấy dữ liệu: {e}")
            return None

    def deleteImage(self, filePath):
        try:
            query = "DELETE FROM Images WHERE filePath = ?"
            self.dbContext.cursor.execute(query, (filePath,))
            self.dbContext.conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Lỗi khi Delete Image: {e}")
            return False

    def close(self):
        if self.dbContext.cursor:
            self.dbContext.cursor.close()
        if self.dbContext.conn:
            self.dbContext.conn.close()
        print("Kết nối đã được đóng.")
        # sad