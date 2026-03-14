class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} отримав повідомлення: {message}")

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# Демонстрація
subject = Subject()

obs1 = ConcreteObserver("Користувач 1")
obs2 = ConcreteObserver("Користувач 2")

subject.attach(obs1)
subject.attach(obs2)

subject.notify("Оновлення системи!")
