# Padrões de Projeto
# Design Patterns Examples

Este repositório contém exemplos de três padrões de projeto: Singleton, Adapter e Visitor.

## Singleton

### Propósito
Garantir que uma classe tenha apenas uma instância e fornecer um ponto global de acesso a ela.

### Problema
Às vezes é importante ter exatamente uma instância de uma classe, por exemplo, um único objeto de configuração compartilhado por toda a aplicação.

### Solução
O Singleton impede que mais de uma instância de uma classe seja criada, fornecendo um único ponto de acesso global à instância.

### Diagrama UML
![Singleton UML](url_da_imagem_do_diagrama_uml)

### Código
```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass
```
### Como testar
```
from singleton import Singleton

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton funciona, ambas as variáveis contêm a mesma instância.")
    else:
        print("Singleton falhou, as variáveis contêm instâncias diferentes.")
```

## Adapter

### Propósito
Permitir que classes com interfaces incompatíveis trabalhem juntas.

### Problema
Uma classe que usa outra classe incompatível, cujo comportamento é necessário.

### Solução
O Adapter converte a interface de uma classe em outra interface que um cliente espera.

### Diagrama UML
### Código
```
class Target:
    def request(self):
        return "Target: O comportamento padrão do target."

class Adaptee:
    def specific_request(self):
        return ".eetpadA roivaheb laicepS"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATE) {self.adaptee.specific_request()[::-1]}"
```
### Como testar
```
from adapter import Target, Adaptee, Adapter

if __name__ == "__main__":
    target = Target()
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    print(target.request())
    print(adapter.request())
```

## Visitor

### Propósito
Permitir que novas operações sejam definidas em uma estrutura de objetos sem mudar as classes dos objetos sobre os quais opera.

### Problema
É necessário adicionar novas funcionalidades a uma hierarquia de classes sem modificar essas classes.

### Solução
O Visitor separa o algoritmo dos objetos sobre os quais opera.

### Diagrama UML
### Código
```
class Visitor:
    def visit_concrete_element_a(self, element):
        pass

    def visit_concrete_element_b(self, element):
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{element.feature_a()} + ConcreteVisitor1")

    def visit_concrete_element_b(self, element):
        print(f"{element.feature_b()} + ConcreteVisitor1")

class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{element.feature_a()} + ConcreteVisitor2")

    def visit_concrete_element_b(self, element):
        print(f"{element.feature_b()} + ConcreteVisitor2")

class Element:
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def feature_a(self):
        return "ConcreteElementA"

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def feature_b(self):
        return "ConcreteElementB"
```
### Como Testar
```
from visitor import ConcreteElementA, ConcreteElementB, ConcreteVisitor1, ConcreteVisitor2

if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]

    visitor1 = ConcreteVisitor1()
    visitor2 = ConcreteVisitor2()

    for element in elements:
        element.accept(visitor1)
        element.accept(visitor2)
```




