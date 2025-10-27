class Lapis:
  def __init__(self, modelo, cor, tamanho, ponta):
    self.modelo = modelo
    self.cor = cor
    self.tamanho = tamanho
    self.ponta = ponta

  def riscar(self):
    print("Está riscando!")
  
  def pintar(self):
    print('Está pintando!')

  def escrever(self):
    print('Está escrevendo.')

modelo = input('Informe o modelo: ')
cor = input('Informe a cor: ')
tamanho = input('Informe o tamanho: ')
ponta = input('Informe a ponta: ')
objeto = Lapis(modelo,cor,tamanho,ponta)
objeto.escrever()