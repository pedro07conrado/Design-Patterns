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
