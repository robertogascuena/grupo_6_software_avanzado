import connexion
from swagger_server.models.profesor import Profesor
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

def borra_profesor(dni):
    """
    Borra un profesor
    Borra un profesor de la lista de profesores.
    :param dni: DNI del profesor
    :type dni: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM `profesor` WHERE `profesor`.`dni` = {}".format(dni))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no ha podido ser borrado.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no existe.")
    cursor.close()
    cnx.close()
    return "Profesor borrado correctamente."


def crear_profesor(profesor):
    """
    Crea un profesor
    Añade un profesor a la lista de profesores.
    :param profesor: El profesor que se va a añadir.
    :type profesor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        profesor = Profesor.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `profesor` (`dni`, `nombre`, `apellidos`, `nombre_usuario`) "
                   +"VALUES (\'{}\', \'{}\', \'{}\', \'{}\')".format(profesor.dni, profesor.nombre, profesor.apellidos, profesor.nombre_usuario))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no ha podido ser creado.")
    cursor.close()
    cnx.close()
    return "Profesor creado correctamente."
