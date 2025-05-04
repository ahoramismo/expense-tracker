from datetime import datetime
from expense_tracker.table import draw

class Expense:
    def __init__(self, storage):
        self.storage = storage

    def add(self, description: str, amount: float):
        """
        Add a new expense entry.
        """
        data = self.storage.load()
        data.append({
            "id": max(entry["id"] for entry in data) + 1 if data else 1,
            "description": description,
            "amount": amount,
            "date": datetime.now().date().isoformat()
        })
        self.storage.save(data)

    def update(self, id: int, description: str, amount: float):
        """
        Update an existing expense entry.
        """
        data = self.storage.load()
        for entry in data:
            if entry.get("id") == id:
                if description:
                    entry["description"] = description
                if amount:
                    entry["amount"] = amount
                self.storage.save(data)
                break
            else:
                print(f"Expense with ID {id} not found.")

    def delete(self, id: int):
        """
        Delete an expense entry.
        """
        data = self.storage.load()
        for entry in data:
            if entry.get("id") == id:
                data.remove(entry)
                self.storage.save(data)
                print(f"Deleted expense with ID {id}")
                return
        print(f"Expense with ID {id} not found.")
        

    def list_expenses(self, year: int = None, month: int = None, date: int = None, filter: str = None):
        """
        List all expense entries with optional filters.
        """
        data = self.storage.load()
        if year:
            data = [entry for entry in data if datetime.fromisoformat(entry["date"]).year == year]
        if month:
            data = [entry for entry in data if datetime.fromisoformat(entry["date"]).month == month]
        if date:
            data = [entry for entry in data if datetime.fromisoformat(entry["date"]).day == date]
        if filter:
            data = [entry for entry in data if filter.lower() in entry["description"].lower()]
        draw(data)


    def summary(self, year: int = None, month: int = None, date: int = None, filter: str = None):
        """
        Generate a summary of expenses with optional filters.
        """
        data = self.storage.load()
        if year:
            data = [entry for entry in data if datetime.fromisoformat(entry["date"]).year == year]
        if month:
            data = [entry for entry in data if datetime.fromisoformat(entry["date"]).month == month]
        if date:
            data = [entry for entry in data if datetime.fromisoformat(entry["date"]).day == date]
        if filter:
            data = [entry for entry in data if filter.lower() in entry["description"].lower()]
        
        if not data:
            print("No entries found.")
            return
        # Calculate total amount
        total_amount = sum(entry["amount"] for entry in data)
        print(f"Total amount spent: {total_amount}")
