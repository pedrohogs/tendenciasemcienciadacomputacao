import unittest
from calculadora import adicao, subtracao, multiplicacao, divisao_segura, raiz_quadrada, exponenciacao

class TestOperacoes(unittest.TestCase):
    def test_adicao(self):
        self.assertEqual(adicao(2.5, 2.5), 5.0)

    def test_divisao_segura(self):
        self.assertEqual(divisao_segura(10, 2), 5.0)
        with self.assertRaises(ValueError):
            divisao_segura(10, 0)
            
    def test_raiz_quadrada(self):
        self.assertEqual(raiz_quadrada(9), 3.0)
        with self.assertRaises(ValueError):
            raiz_quadrada(-4)
            
    def test_exponenciacao(self):
        self.assertEqual(exponenciacao(2, 3), 8.0)

if __name__ == "__main__":
    unittest.main()
