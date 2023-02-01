from mecanica import Mecanica
from seguranca import Seguranca
from acessorios import Acessorios
        
class Esteira(Mecanica, Seguranca, Acessorios):
    
    def __init__(self, modelo):
        self.modelo = modelo

    def start(self):
        consumo = str()
        talvez_consumo_tb = str()
        cambio = str()
        qtd_marchas = int()
        tipo_injecao = str()
        amortecedor = str()
        radiador_tubular = bool()
        freios_abs = bool()
        turbo = bool()
        
        while True:
            print('''Escolha a opção que indica qual o consumo
                1 - Gasolina
                2 - Diesel
                3 - Elétrico
                ''')
            
            primeira_escolha = str(input('Digite a opção: '))
            
            if primeira_escolha == '1':
                consumo = 'Gasolina'
                talvez_consumo_tb = 'Elétrico'
                break
                    
            elif primeira_escolha == '2':
                consumo = 'Diesel'
                cambio = 'Manual'
                break
                
            elif primeira_escolha == '3':
                consumo = 'Elétrico'
                cambio = 'Automático'
                talvez_consumo_tb = 'Gasolina'
                break
                
            else:
                print('\nEscolha uma opção valida!\n')
                
        while primeira_escolha != '2':
            segunda_escolha = str(input(f'Ele também é a {talvez_consumo_tb}?[y/n] ')).upper()
            
            if segunda_escolha == 'Y':
                consumo = 'Híbrido'
                break
            elif segunda_escolha == 'N':
                break
            else:
                print('\nEscolha uma opção valida!\n')
        
        Mecanica.write_consup(self, consumo)
        
        if consumo != 'Diesel' and consumo != 'Elétrico':
            while True:
                print('''Escolha a opção que indica o tipo de Câmbio:
                    1 - Manual
                    2 - Automático
                    ''')
                
                escolha = str(input('Sua escolha: '))
                
                if escolha == '1':
                    cambio = 'Manual'
                    break
                    
                elif escolha == '2':
                    cambio = 'Automático'
                    break
                    
                else:
                    print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_exchange(self, cambio)
        
        while True:
            print('''Escolha a Qtd de marcha: 
                  1 - 5 marchas
                  2 - 6 marchas
                  ''')
            
            escolha = str(input('Sua escolha: '))
            
            if escolha == '1':
                qtd_marchas = 5
                break
                
            elif escolha == '2':
                qtd_marchas = 6
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
        
        Mecanica.write_amount_gears(self, qtd_marchas)
        
        while True:
            print('''Escolha o Tipo de injeção:
                  1 - Eletrônica 
                  2 - Convencional
                  ''')
            
            escolha = str(input('Sua escolha: '))
            
            if escolha == '1':
                tipo_injecao = 'eletrônica'
                break
                
            elif escolha == '2':
                tipo_injecao = 'convencional'
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_type_injection(self, tipo_injecao)
        
        while True:
            print('''Escolha o tipo de Amortecedores:
                  1 - reforçados
                  2 - comum
                  ''')
            
            escolha = str(input('Sua escolha: '))
            
            if escolha == '1':
                amortecedor = 'reforçados'
                break
                
            elif escolha == '2':
                amortecedor = 'comum'
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_absorver(self, amortecedor)
                
        while True:
            escolha = str(input('O carro possui Radiador tubular?[y/n] ')).upper()
            
            if escolha == 'Y':
                radiador_tubular = True
                break
                
            elif escolha == 'N':
                radiador_tubular = False
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_tub_radiator(self, radiador_tubular)
        
        while True:
            escolha = str(input('O carro possui Freios ABS?[y/n] ')).upper()
            
            if escolha == 'Y':
                freios_abs = True
                break
                
            elif escolha == 'N':
                freios_abs = False
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_brakes_abs(self, freios_abs)
        
        while True:
            escolha = str(input('O carro possui Turbo?[y/n] ')).upper()
            
            if escolha == 'Y':
                turbo = True
                break
                
            elif escolha == 'N':
                turbo = False
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_turbo(self, turbo)


##############################################################################################################################################

onix = Esteira('onix')

onix.start()

print(onix.read_all_mechanics())
