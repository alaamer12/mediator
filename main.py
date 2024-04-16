from abc import ABC, abstractmethod
from typing import List

# Mediator Interface
class Mediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender: 'User'):
        pass

# Concrete Mediator
class ChatRoom(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user: 'User'):
        self.users.append(user)

    def send_message(self, message: str, sender: 'User'):
        for user in self.users:
            if user != sender:
                user.receive_message(message)

# Colleague
class User:
    def __init__(self, name: str, mediator: Mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message: str):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive_message(self, message: str):
        print(f"{self.name} receives: {message}")

# Example
if __name__ == "__main__":
    chat_room = ChatRoom()
    user1 = User("Alice", chat_room)
    user2 = User("Bob", chat_room)

    chat_room.add_user(user1)
    chat_room.add_user(user2)

    user1.send_message("Hello, Bob!")
    user2.send_message("Hi, Alice!")
