import json
from pathlib import Path
from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def load(self):
        """
        Load expenses from the storage.
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def save(self, data):
        """
        Save expenses to the storage.
        """
        raise NotImplementedError("Subclasses should implement this!")


class JSONStorage(Storage):
    def __init__(self, filename: str):
        self.filename = filename
        self.filepath = Path(filename)

    def load(self):
        """
        Load expenses from the JSON file.
        Returns an empty list if file does not exist or is invalid.
        """
        if not self.filepath.exists():
            return []

        try:
            with self.filepath.open("r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty list.")
            return []

    def save(self, data):
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        with self.filepath.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
