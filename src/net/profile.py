import pickle
from dataclasses import dataclass
from src.events.event import Event


@dataclass(slots=True)
class Profile:
    host: str
    connection_date: str
    last_used_port: int
    last_connection_time: float
    last_event: Event
    attempted_attacks: int
    last_attempted_attack: str

    def update(self, data):
        for setting, value in data.items():
            setattr(self, setting, value)

    def serialize(self) -> bytes:
        return pickle.dumps(self)

    @classmethod
    def deserialize(cls, data: bytes):
        return pickle.loads(data)
