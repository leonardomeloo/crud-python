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
        
    finally:
        cursor.close()

def Read():
    cursor = db.connection.cursor()
    sql = f'SELECT * FROM cliente'
    cursor.execute(sql)
    return cursor.fetchall()

def Update(opcao):
    
    cursor = db.connection.cursor()
    if opcao == "A":
        email = input("Digite o seu E-mail: ")
        old_value = input("Digite o valor atual: ")
        new_value =  input("Atualize o valor: ")
        sql = 'UPDATE cliente SET fullname = %s WHERE fullname = %s AND email = %s'
        values = (new_value, old_value,  email)
        
    elif opcao == "B":
        email = input("Digite o seu E-mail: ")
        old_value = input("Digite o valor atual: ")
        new_value =  input("Atualize o valor: ")
        sql = 'UPDATE cliente SET age = %s WHERE age = %s AND AND email = %s'
        values = (new_value, old_value, email)
    elif opcao == "C":
        email = input("Digite o seu E-mail: ")
        old_value = input("Digite o valor atual: ")
        new_value =  input("Atualize o valor: ")
        sql = 'UPDATE cliente SET profession = %s WHERE profession = %s AND email = %s'
        values = (new_value, old_value, email)
    elif opcao == "D":
        email = input("Digite o seu E-mail: ")
        old_value = input("Digite o valor atual: ")
        new_value =  input("Atualize o valor: ")
        sql = 'UPDATE cliente SET email = %s WHERE email = %s AND email = %s'
        values = (new_value, old_value, email)
    else:
        print('Valor incorreto.')
    try:
            cursor.execute(sql, values)
            db.connection.commit()
            print(f"{cursor.rowcount} registro(s) atualizado(s).")
    except Exception as error:
        print(f"Erro: {error}")
        db.connection.rollback()
    finally:
        cursor.close()

def Delete():
    cursor = db.connection.cursor()
    fullname = input("Digite o seu nome completo: ")
    email = input("Digite o seu E-mail: ")
    sql = 'DELETE FROM cliente WHERE fullname = %s and email = %s'
    values = (fullname, email)

    try:
        cursor.execute(sql, values)
        db.connection.commit()
        print(f"{cursor.rowcount} registro deletado com sucesso.")
    except Exception as error:
        print(error)
        db.connection.rollback()
    finally:
        cursor.close()
        