# import logging
import sqlite3 as sqlite
from decouple import config
from filelog import FileLog

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
            # logging.exception('Error: %s', ex)
            FileLog.save_message('/persons/', ex)
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
            # logging.exception('Error: %s', ex)
            FileLog.save_message('(/person/id/{id}|/person?id=)', ex)
        finally:
            Database.close_connection(cur, conn)
        return persona


    @staticmethod
    def read_persons_by_nombre(nombre:str)->list:
        personas = []
        try:
            conn = sqlite.connect(DATABASE)
            conn.row_factory= sqlite.Row
            cur = conn.cursor()
            personas = cur.execute('SELECT * FROM person WHERE nombre= :nombre', {'nombre': nombre}).fetchall()
        except Exception as ex:
            # logging.exception('Error: %s', ex)
            FileLog.save_message('/persons/nombre/{nombre}', ex)
        finally:
            Database.close_connection(cur, conn)
        return personas
        
