import services.database as db

def Creat(cliente):
    cursor = db.connection.cursor()
    sql = ("INSERT INTO cliente "
                "(fullname, age, profession, email) "
                "VALUES (%s, %s, %s, %s)")
    values = (cliente.fullname, cliente.age, cliente.profession, cliente.email)
    try:
        cursor.execute(sql, values)
        db.connection.commit()
        print(f"{cursor.rowcount} registro(s) inserido(s).")
    
    except Exception as error:
        print(f"Erro: {error}")
        cursor.close()

def Read():
    cursor = db.connection.cursor()
    sql = f'SELECT * FROM cliente'
    cursor.execute(sql)
    return cursor.fetchall()

def Update(cliente):
    pass

def Delete(cliente):
    pass
