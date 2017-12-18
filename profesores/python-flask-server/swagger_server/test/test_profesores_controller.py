# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.profesor import Profesor
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProfesoresController(BaseTestCase):
    """ ProfesoresController integration test stubs """

    def test_borra_profesor(self):
        """
        Test case for borra_profesor

        Borra un profesor
        """
        response = self.client.open('/profesores/delete-profesor/{dni}'.format(dni=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crear_profesor(self):
        """
        Test case for crear_profesor

        Crea un profesor
        """
        profesor = Profesor()
        response = self.client.open('/profesores/profesor',
                                    method='POST',
                                    data=json.dumps(profesor),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
