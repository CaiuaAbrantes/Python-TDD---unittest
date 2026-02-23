import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma_cinco_e_cinco_deve_retornar_dez(self):
        self.assertEqual(soma(5,5), 10)

    def test_soma_cinco_negativo_e_cinco_deve_retornar_zero(self):
        self.assertEqual(soma(-5,5), 0)

    def test_varias_eentradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (15, 10, 25),
            (10, 20, 30),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida = x_y_saida):
                x, y, saida =  x_y_saida
                self.assertEqual(soma(x,y), saida)

    def test_soma_x_nao_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    
    def test_soma_y_nao_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(0, '0')


unittest.main()