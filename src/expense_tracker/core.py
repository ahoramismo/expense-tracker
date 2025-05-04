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
        next_id = max(entry["id"] for entry in data) + 1 if data else 1
        data.append({
            "id": next_id,
            "description": description,
            "amount": amount,
            "date": datetime.now().date().isoformat()
        })
        self.storage.save(data)
        print(f"Added expense: {description} - ${amount:.2f}")

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
                print(f"Updated expense with ID {id}")
                return

        print(f"Expense with ID {id} not found.")

    def delete(self, id: int):
        """
        Delete an expense entry.
        """
        data = self.storage.load()
        new_data = [entry for entry in data if entry.get("id") != id]
        if len(new_data) == len(data):
            print(f"Expense with ID {id} not found.")
            return
        self.storage.save(new_data)
        print(f"Deleted expense with ID {id}")

    def list_expenses(self, year: int = None, month: int = None, date: int = None, filter_term: str = None):
        """
        List all expense entries with optional filters.
        """
        data = self._apply_filters(self.storage.load(), year, month, date, filter_term)
        draw(data)

    def summary(self, year: int = None, month: int = None, date: int = None, filter_term: str = None):
        """
        Generate a summary of expenses with optional filters.
        """
        data = self._apply_filters(self.storage.load(), year, month, date, filter_term)

        if not data:
            print("No entries found.")
            return
        # Calculate total amount
        total = sum(entry["amount"] for entry in data)
        print(f"Total amount spent: ${total:.2f}")

    def _apply_filters(self, data, year, month, date, filter_term):
        """
        Apply common filtering to the dataset.
        """
        filtered = data
        if year:
            filtered = [e for e in filtered if datetime.fromisoformat(e["date"]).year == year]
        if month:
            filtered = [e for e in filtered if datetime.fromisoformat(e["date"]).month == month]
        if date:
            filtered = [e for e in filtered if datetime.fromisoformat(e["date"]).day == date]
        if filter_term:
            filtered = [e for e in filtered if filter_term.lower() in e["description"].lower()]
        return filtered
