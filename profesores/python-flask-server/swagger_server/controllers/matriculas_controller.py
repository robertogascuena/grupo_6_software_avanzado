import connexion
from swagger_server.models.matricula import Matricula
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort

user = "root"
password = ""
database = "universidad"

def crea_matricula(matricula):
    """
    Matricula a un alumno
    Matricula a un alumno en una asignatura.
    :param matricula: La matricula que se va a crear.
    :type matricula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        matricula = Matricula.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `calificacion` (`id_asignatura`, `dni_alumno`) "
                   +"VALUES (\'{}\', \'{}\')".format(matricula.id_asignatura, matricula.dni_alumno))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La matricula no ha podido ser creada.")
    cursor.close()
    cnx.close()
    return "Matricula creada correctamente."
