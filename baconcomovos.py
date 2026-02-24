"""
1- Receber um numero inteiro
2- Saber se o numero e multiplo de 3 e 5
    Bacon com Ovos
3- Saber se o numero e multiplo de 3
    Bacon
4- Saber se o numero e multiplo de 5
    Ovos
5- Saber se o numero nao e multiplo nem de 3 nem de 5
    Passar fome
"""

def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser int'
    if n % 3 ==0  and n % 5 == 0:
        return 'Bacon com Ovos'
    
    if n % 3 == 0 and n % 5 != 0:
        return 'Bacon'
    
    if n % 5 == 0 and n % 3 != 0:
        return 'Ovos'
    
    return 'Passar fome'