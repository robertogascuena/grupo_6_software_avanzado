# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.asignatura import Asignatura
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAsignaturasController(BaseTestCase):
    """ AsignaturasController integration test stubs """

    def test_borra_asignatura(self):
        """
        Test case for borra_asignatura

        Borra una asignatura
        """
        response = self.client.open('/profesores/delete-asignatura/{id}'.format(id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crear_asignatura(self):
        """
        Test case for crear_asignatura

        Crea una asignatura
        """
        asignatura = Asignatura()
        response = self.client.open('/profesores/asignatura',
                                    method='POST',
                                    data=json.dumps(asignatura),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
