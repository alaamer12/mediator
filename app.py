from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def send_message(self, message, sender):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleagues = {}

    def add_colleague(self, colleague):
        self.colleagues[colleague.name] = colleague

    def send_message(self, message, sender):
        for name, colleague in self.colleagues.items():
            if colleague != sender:
                colleague.receive_message(message)

class Colleague(ABC):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive_message(self, message):
        pass

class ConcreteColleague(Colleague):
    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive_message(self, message):
        print(f"{self.name} receives: {message}")

if __name__ == "__main__":
    mediator = ConcreteMediator()

    colleague1 = ConcreteColleague(mediator, "Colleague 1")
    colleague2 = ConcreteColleague(mediator, "Colleague 2")
    colleague3 = ConcreteColleague(mediator, "Colleague 3")

    mediator.add_colleague(colleague1)
    mediator.add_colleague(colleague2)
    mediator.add_colleague(colleague3)

    colleague1.send("Hello, colleagues!")
    colleague2.send("Hi, colleague1!")
    colleague3.send("Greetings, everyone!")
