import pymysql

class DAOEmpleados:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="", db="db_poo")

    def read(self, id):
        con = self.connect()
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM empleados order by nombre asc")
            else:
                cursor.execute("SELECT * FROM empleados WHERE id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = self.connect()
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO empleados(nombre, apellido, email, DNI) VALUES(%s, %s, %s, %s)",
                (data['nombre'], data['apellido'], data['email'], data['DNI'])
            )
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = self.connect()
        cursor = con.cursor()

        try:
            cursor.execute(
                "UPDATE empleados SET nombre = %s, apellido = %s, email = %s, DNI = %s WHERE id = %s",
                (data['nombre'], data['apellido'], data['email'], data['DNI'], id)
            )
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = self.connect()
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM empleados WHERE id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()