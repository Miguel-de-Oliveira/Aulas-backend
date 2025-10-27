class Bola:
  def __init__(self,cor, marca):
    self.cor = cor
    self.marca = marca
    print('Valores iniciais: ',self.cor,self.marca)
  
  def mudarCor(self):
    self.cor_nova = input('Informe uma nova cor: ')
    print(f'Cor antiga: {self.cor}')
    print(f'Cor nova: {self.cor_nova}')


cor = input('Digite uma cor: ')
marca = input('Digite a marca: ')
objetoDaClasse = Bola(cor, marca)
objetoDaClasse.mudarCor()