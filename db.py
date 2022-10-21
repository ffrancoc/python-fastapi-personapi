import sqlite3 as sqlite
from decouple import config

# Obtener la ruta de la base de datos del archivo .env
DATABASE = config('DATABASE')

class Database:
    
    # Cerrar el cursor y la conexion de la base de datos
    @staticmethod
    def close_connection(cur, conn):
        if cur: cur.close()
        if conn: conn.close()
    
    # Obtener todos los datos de todas las personas en la base de datos
    @staticmethod
    def read_personas()->list:
        personas = []
        try:
            conn = sqlite.connect(DATABASE)
            conn.row_factory= sqlite.Row
            cur = conn.cursor()
            personas = cur.execute('SELECT * FROM person').fetchall()            
        except Exception as ex:
            print('Error: %s' % ex)
        finally:
            Database.close_connection(cur, conn)            
        return personas

    # Obtener persona por id
    @staticmethod
    def read_person_by_id(id:int)->(tuple|None):
        persona = None
        try:
            conn = sqlite.connect(DATABASE)
            conn.row_factory= sqlite.Row
            cur = conn.cursor()
            persona = cur.execute('SELECT * FROM person WHERE id=:id', {'id':id}).fetchone()        
        except Exception as ex:
            print('Error: %s' % ex)
        finally:
            Database.close_connection(cur, conn)
        return persona

