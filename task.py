from dataclasses import dataclass

@dataclass
class Task:
    description: str
    completed: bool = False 

    def to_dict(self):
        return {
            "description": self.description,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["description"], data["completed"])