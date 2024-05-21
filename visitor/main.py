from visitor import ConcreteElementA, ConcreteElementB, ConcreteVisitor1, ConcreteVisitor2

if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]

    visitor1 = ConcreteVisitor1()
    visitor2 = ConcreteVisitor2()

    for element in elements:
        element.accept(visitor1)
        element.accept(visitor2)
