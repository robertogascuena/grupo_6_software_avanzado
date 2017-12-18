# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.matricula import Matricula
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMatriculasController(BaseTestCase):
    """ MatriculasController integration test stubs """

    def test_crea_matricula(self):
        """
        Test case for crea_matricula

        Matricula a un alumno
        """
        matricula = Matricula()
        response = self.client.open('/profesores/matricula',
                                    method='POST',
                                    data=json.dumps(matricula),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
