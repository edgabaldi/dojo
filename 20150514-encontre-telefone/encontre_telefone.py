import unittest

# http://dojopuzzles.com/problemas/exibe/encontre-o-telefone/


class EncontreTelefone():

    dict_conversao = {'ABC': '2', 'DEF': '3', 'GHI': '4', 'JKL': '5',
                      'MNO': '6', 'PQRS': '7', 'TUV': '8', 'WXYZ': '9'}
    
    def converter_frase(self, frase):
        self._verificar_tamanho_frase(frase)
        return ''.join([self.converter_letra(letra) for letra in frase])

    def converter_letra(self, letra):
        self._verificar_tamanho_letra(letra)
        
        for chave, valor in self.dict_conversao.iteritems():
            if letra in chave:
                return valor
                
        return letra    
    
    def _verificar_tamanho_frase(self, frase):
        if len(frase) < 1 or len(frase) > 30:
            raise Exception("Deve conter entre de 1 a 30 caracteres.")
        
    def _verificar_tamanho_letra(self, letra):
        if len(letra) > 1:
            raise Exception('Deve ser passado somente uma letra.')

class EncontraTelefoneTest(unittest.TestCase):
    
    def setUp(self):
        self.encontra = EncontreTelefone()
    
    def test_tamanho_da_string_deve_ser_maior_ou_igual_a_1(self):
        with self.assertRaisesRegexp(Exception, 'Deve conter entre de 1 a 30 caracteres.'):
            self.encontra.converter_frase('')
    
    def test_tamanho_da_frase_nao_deve_ser_maior_que_30(self):
        
        frase_invalida = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        self.assertTrue(len(frase_invalida) > 30)
        
        with self.assertRaisesRegexp(Exception, 'Deve conter entre de 1 a 30 caracteres.'):
            self.encontra.converter_frase(frase_invalida)
            
    def test_converter_letra_usando_frase_lanca_exception(self):
        with self.assertRaisesRegexp(Exception, 'Deve ser passado somente uma letra.'):
            self.encontra.converter_letra('AGU')

    def test_frase_1_HOME_SWEET_HOME_deve_retornar_1_4663_79338_4663(self):
        convertido = self.encontra.converter_frase('1-HOME-SWEET-HOME')
        self.assertEqual('1-4663-79338-4663', convertido)

    def test_palavra_MY_deve_retornar_69(self):
        convertido = self.encontra.converter_frase('MY')
        self.assertEqual('69', convertido)
    
    def test_ABC_deve_retornar_2(self):
        
         for letra in 'ABC':
             convertido = self.encontra.converter_letra(letra)
             self.assertEqual('2', convertido)
    
    def test_DEF_deve_retornar_3(self):
        
         for letra in 'DEF':
             convertido = self.encontra.converter_letra(letra)
             self.assertEqual('3', convertido)

    def test_GHI_deve_retornar_4(self):
        
         for letra in 'GHI':
             convertido = self.encontra.converter_letra(letra)
             self.assertEqual('4', convertido)

    def test_JKL_deve_retornar_5(self):
        
         for letra in 'JKL':
             convertido = self.encontra.converter_letra(letra)
             self.assertEqual('5', convertido)

    def test_MNO_deve_retornar_6(self):
        
         for letra in 'MNO':
             convertido = self.encontra.converter_letra(letra)
             self.assertEqual('6', convertido)

    def test_PQRS_deve_retornar_7(self):
        
         for letra in 'PQRS':
             convertido = self.encontra.converter_letra(letra)
             self.assertEqual('7', convertido)

    def test_TUV_deve_retornar_8(self):
        
         for letra in 'TUV':
             convertido = self.encontra.converter_letra(letra)
             self.assertEqual('8', convertido)

    def test_WXYZ_deve_retornar_9(self):
        
         for letra in 'WXYZ':
             convertido = self.encontra.converter_letra(letra)
             self.assertEqual('9', convertido)
        
    def test_numero_um(self):
        convertido = self.encontra.converter_letra('1')
        self.assertEqual('1', convertido)
    
    def test_numero_zero(self):
        convertido = self.encontra.converter_letra('0')
        self.assertEqual('0', convertido)
        
    def test_hifem(self):
        convertido = self.encontra.converter_letra('-')
        self.assertEqual('-', convertido)

unittest.main()