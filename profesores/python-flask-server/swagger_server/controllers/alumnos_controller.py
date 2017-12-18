import connexion
from swagger_server.models.alumno import Alumno
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

def borra_alumno(dni):
    """
    Borra un alumno
    Borra un alumno y todas sus notas.
    :param dni: DNI del alumno
    :type dni: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        #cursor.execute("DELETE FROM `calificacion` WHERE `calificacion`.`dni_alumno` = {}".format(dni))
        cursor.execute("DELETE FROM `alumno` WHERE `alumno`.`dni` = {}".format(dni))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no ha podido ser borrado.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no existe.")
    cursor.close()
    cnx.close()
    return "Alumno borrado correctamente."


def crear_alumno(alumno):
    """
    Crea un alumno
    Añade un alumno a la lista de alumnos.
    :param alumno: El alumno que se va a añadir.
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alumno = Alumno.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `alumno` (`dni`, `nombre`, `apellidos`) "
                   +"VALUES (\'{}\', \'{}\', \'{}\')".format(alumno.dni, alumno.nombre, alumno.apellidos))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no ha podido ser creado.")
    cursor.close()
    cnx.close()
    return "Alumno creado correctamente."
