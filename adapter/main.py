from adapter import Target, Adaptee, Adapter

if __name__ == "__main__":
    target = Target()
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    print(target.request())
    print(adapter.request())
