"""
TDD
"""

import unittest
from baconcomovos import bacon_com_ovos

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_Assertion_se_nao_recebe_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('a')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_tres_e_cinco(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com Ovos'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} nao retornou {saida}'
                )

    def test_bacon_com_ovos_deve_retornar_passa_fome_se_nao_for_nem_multiplo_de_tres_nem_de_cinco(self):
        entradas = (4, 7, 13)
        saida = 'Passar fome'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} nao retornou {saida}'
                )

    def test_bacon_com_ovos_deve_retornar_Bacon_se_for_multiplo_so_de_tres(self):
        entradas = (9, 21, 27)
        saida = 'Bacon'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} nao retornou {saida}'
                )

    def test_bacon_com_ovos_deve_retornar_Ovos_se_for_multiplo_so_de_cinco(self):
        entradas = (5, 10, 20)
        saida = 'Ovos'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} nao retornou {saida}'
                )


unittest.main(verbosity=2)