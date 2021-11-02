import sqlite3
class testing:
    def __init__(self,**kwargs):
        self.name = kwargs['name']
        self.Class = kwargs['Class']
        self.mark = kwargs['mark']
        self.grade = kwargs['grade']


class database():

    def __init__(self,file_name,table_name):
        self.table_name=table_name
        self.file_name=file_name


    def get_connection(self):
        conn = sqlite3.connect(self.file_name)
        print("conection ready")
        return conn



    def create_file(self , conn):
        conn.execute('''CREATE TABLE IF NOT EXISTS ''' + self.table_name + '''(name,Class,mark,grade)''')
        print("Table created")


    def create_Table(self,conn,obj):
        qr= f'''INSERT INTO {self.table_name} (name,Class,mark,grade) VALUES (?,?,?,?)'''
        conn.execute(qr,(obj.name,obj.Class,obj.mark,obj.grade))
        conn.commit()
        print("table_created")


    def con_close(self,conn):
        conn.close()
        print("connection_closed")


db = database("grade.db","grade")
con=db.get_connection()
db.create_file(con)
obj=testing(name="carl",Class="10",mark="90",grade="A+")
db.create_Table(con,obj)
db.con_close(con)