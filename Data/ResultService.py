from Model import ResultDetection
from Data.ConnectDataBase import Connect_Db

class Result_Service:
    def __init__(self):
        self.dbContext = Connect_Db()  # dbContext là một instance của ConnectDb
        self.dbContext.connect()

    def insertResult(self, resultDetection: ResultDetection):
        query = """
        INSERT INTO ResultDetection (filePath, result, dateCreated)
        VALUES (?, ?, ?)
        """
        values = (resultDetection.imageName, resultDetection.result, resultDetection.dateCreated)

        try:
            self.dbContext.cursor.execute(query, values)
            self.dbContext.conn.commit()
        except Exception as e:
            print(f"Lỗi khi chèn dữ liệu: {e}")
        finally:
            self.dbContext.conn.close()

    def getAllResult(self):
        query = "SELECT * FROM ResultDetection"

        try:
            self.dbContext.cursor.execute(query)
            results = self.dbContext.cursor.fetchall()  # Lấy tất cả các dòng dữ liệu
            return results
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu: {e}")
            return None
        finally:
            self.dbContext.conn.close()
