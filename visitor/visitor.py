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
