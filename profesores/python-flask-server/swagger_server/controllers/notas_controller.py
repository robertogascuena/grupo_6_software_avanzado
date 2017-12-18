import connexion
from swagger_server.models.calificacion import Calificacion
from swagger_server.models.nota import Nota
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort

#user = "juan.antonio"
#password = "juan"
user = "root"
password = ""
database = "universidad"

def actualiza_nota(calificacion):
    """
    Actualiza una nota
    Actualiza la nota de un alumno en una asignatura.
    :param calificacion: La calificación que se va a actualizar.
    :type calificacion: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        calificacion = Nota.from_dict(connexion.request.get_json())
    cnx = mysql.connector.connect(user=user, password=password, database=database)    
    cursor = cnx.cursor()
    cursor.execute("UPDATE `calificacion` SET `nota` = "+str(calificacion.nota)
                   +" WHERE `calificacion`.`id_asignatura` = '"+str(calificacion.id_asignatura)
                   +"' AND `calificacion`.`dni_alumno` = '"+str(calificacion.dni_alumno)+"'")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "La nota no ha podido ser actualizada")
    cnx.commit()
    cursor.close()
    cnx.close()
    return 'Nota actualizada'


def notas_dni_alumno_get(dni):
    """
    Devuelve las notas
    Devuelve las notas del alumno
    :param dni: DNI del alumno
    :type dni: int

    :rtype: List[Calificacion]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `asignatura`.`id`, `asignatura`.`nombre` AS `nomb_asig`, `alumno`.`dni`, `alumno`.`nombre`, `alumno`.`apellidos`, `calificacion`.`nota`\n"
    + "FROM `alumno` \n"
    + "	INNER JOIN `calificacion` ON `alumno`.`dni` = `calificacion`.`dni_alumno`\n"
    + " INNER JOIN `asignatura` ON `calificacion`.`id_asignatura` = `asignatura`.`id`\n"
    + "WHERE `alumno`.`dni` = \""+str(dni)+"\"")
    DB = {}
    tuplas = 0
    for (id, nomb_asig, dni, nombre, apellidos, nota) in cursor:
        DB[tuplas] = Calificacion(dni, id, nota, nombre, apellidos, nomb_asig)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El alumno no existe o no está matriculado en ninguna asignatura")
    return [nota for _, nota in DB.items()]


def notas_dni_profesor_get(dni):
    """
    Devuelve las notas
    Devuelve las notas de los alumnos del profesor
    :param dni: DNI del profesor
    :type dni: int

    :rtype: List[Calificacion]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `asignatura`.`id`, `asignatura`.`nombre` AS `nomb_asig`, `alumno`.`dni`, `alumno`.`nombre`, `alumno`.`apellidos`, `calificacion`.`nota`\n"
    + "FROM `alumno` \n"
    + "	INNER JOIN `calificacion` ON `alumno`.`dni` = `calificacion`.`dni_alumno`\n"
    + " INNER JOIN `asignatura` ON `calificacion`.`id_asignatura` = `asignatura`.`id`\n"
    + " INNER JOIN `profesor` ON `asignatura`.`dni_profesor` = `profesor`.`dni`\n"
    + "WHERE `profesor`.`dni` = \""+str(dni)+"\"")
    DB = {}
    tuplas = 0
    for (id, nomb_asig, dni, nombre, apellidos, nota) in cursor:
        DB[tuplas] = Calificacion(dni, id, nota, nombre, apellidos, nomb_asig)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El profesor no existe o no tiene alumnos")
    return [nota for _, nota in DB.items()]


def notas_id_asignatura_get(id):
    """
    Devuelve las notas
    Devuelve las notas de la asignatura
    :param id: ID de la asignatura
    :type id: int

    :rtype: List[Calificacion]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `asignatura`.`id`, `asignatura`.`nombre` AS `nomb_asig`, `alumno`.`dni`, `alumno`.`nombre`, `alumno`.`apellidos`, `calificacion`.`nota`\n"
    + "FROM `alumno` \n"
    + "	INNER JOIN `calificacion` ON `alumno`.`dni` = `calificacion`.`dni_alumno`\n"
    + " INNER JOIN `asignatura` ON `calificacion`.`id_asignatura` = `asignatura`.`id`\n"
    + "WHERE `asignatura`.`id` = \""+str(id)+"\"")
    DB = {}
    tuplas = 0
    for (id, nomb_asig, dni, nombre, apellidos, nota) in cursor:
        DB[tuplas] = Calificacion(dni, id, nota, nombre, apellidos, nomb_asig)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "La asignatura no existe o no tiene alumnos")
    return [nota for _, nota in DB.items()]


def notas_user_profesor_get(nombreUsuario):
    """
    Devuelve las notas
    Devuelve las notas de los alumnos del profesor
    :param nombreUsuario: Nombre de usuario del profesor
    :type nombreUsuario: str

    :rtype: List[Calificacion]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `asignatura`.`id`, `asignatura`.`nombre` AS `nomb_asig`, `alumno`.`dni`, `alumno`.`nombre`, `alumno`.`apellidos`, `calificacion`.`nota`\n"
    + "FROM `alumno` \n"
    + "	INNER JOIN `calificacion` ON `alumno`.`dni` = `calificacion`.`dni_alumno`\n"
    + " INNER JOIN `asignatura` ON `calificacion`.`id_asignatura` = `asignatura`.`id`\n"
    + " INNER JOIN `profesor` ON `asignatura`.`dni_profesor` = `profesor`.`dni`\n"
    + "WHERE `profesor`.`nombre_usuario` = \""+nombreUsuario+"\"")
    DB = {}
    tuplas = 0
    for (id, nomb_asig, dni, nombre, apellidos, nota) in cursor:
        DB[tuplas] = Calificacion(dni, id, nota, nombre, apellidos, nomb_asig)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El profesor no existe o no tiene alumnos")
    return [nota for _, nota in DB.items()]

