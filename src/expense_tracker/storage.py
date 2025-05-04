import os
import json


class Storage:
    def load(self):
        """
        Load expenses from the storage.
        """
        raise NotImplementedError("Subclasses should implement this!")

    def save(self, data):
        """
        Save expenses to the storage.
        """
        raise NotImplementedError("Subclasses should implement this!")


class JSONStorage(Storage):
    def __init__(self, filename: str):
        self.filename = filename
        self.load()

    def load(self):
        data = []
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty list.")

        return data

    def ensure_directory(self):
        """
        Ensure the directory for the file exists.
        """
        directory = os.path.dirname(self.filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def save(self, data):
        self.ensure_directory()
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
