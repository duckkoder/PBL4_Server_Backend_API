import pyodbc

class Connect_Db:
    def __init__(self):
        self.connection_string = r'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=LAPTOP-DB0H1E2V\SQLEXPRESS; Database=PBL4_database; UID=td; PWD=1'
        self.conn = None
        self.cursor = None


    def connect(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            self.cursor = self.conn.cursor()
            print("Kết nối thành công")
        except pyodbc.Error as e:
            print(f"Không thể kết nối: {e}")
            raise
    def create_table(self, table_name):
        self.connect()
        query = "CREATE TABLE IF NOT EXISTS " + table_name +("("
        " id )")
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()

