# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnosController(BaseTestCase):
    """ AlumnosController integration test stubs """

    def test_borra_alumno(self):
        """
        Test case for borra_alumno

        Borra un alumno
        """
        response = self.client.open('/profesores/delete-alumno/{dni}'.format(dni=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crear_alumno(self):
        """
        Test case for crear_alumno

        Crea un alumno
        """
        alumno = Alumno()
        response = self.client.open('/profesores/alumno',
                                    method='POST',
                                    data=json.dumps(alumno),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
