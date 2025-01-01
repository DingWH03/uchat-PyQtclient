# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
import json
from dataclasses import dataclass

# Define data classes for requests and server responses
@dataclass
class RegisterRequest:
    action: str
    username: str
    password: str

    def to_json(self):
        return json.dumps({
            "action": self.action,
            "username": self.username,
            "password": self.password
        })

@dataclass
class LoginRequest:
    action: str
    username: str
    password: str

    def to_json(self):
        return json.dumps({
            "action": self.action,
            "username": self.username,
            "password": self.password
        })

@dataclass
class SendMessageRequest:
    action: str
    receiver: str
    message: str

    def to_json(self):
        return json.dumps({
            "action": self.action,
            "receiver": self.receiver,
            "message": self.message
        })

@dataclass
class ServerResponse:
    action: str
    data: dict
