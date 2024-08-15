# HERANÇA
# Permite que as classes compartilhem atributos e métodos, e que as classes mais especializadas herdem métodos e atributos de classes mais 
# genéricas. A herança é usada para reaproveitar código ou comportamento generalizado, ou para especializar operações ou atributos. 

# Classes Base (Superclasse[PAI]) e Classes Derivadas (Subclasse[FILHO])
print('HERANÇA')

class Animal: # Classes Base (Superclasse[PAI]
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return "Som genérico"

class Cachorro(Animal):  # Classes Derivadas (Subclasse[FILHO])
    def fazer_som(self):  # Sobrescreve o método da classe pai
        return "Latido"

# Criando instâncias
animal = Animal("Animal Genérico")
cachorro = Cachorro("Rex")

# Exibindo no terminal
print("Animal: {} faz {}".format(animal.nome, animal.fazer_som()))
print("Cachorro: {} faz {}".format(cachorro.nome, cachorro.fazer_som()))
