from singleton import Singleton

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton funciona, ambas as variáveis contêm a mesma instância.")
    else:
        print("Singleton falhou, as variáveis contêm instâncias diferentes.")
