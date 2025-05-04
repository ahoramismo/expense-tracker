from prettytable import PrettyTable


def draw(entries):
    """
    Display a list of expense entries in a formatted table.

    Parameters:
        entries (list): A list of dictionaries containing expense data.
    """

    if not entries:
        print("No entries found.")
        return

    table = PrettyTable(field_names=["ID", "Date", "Description", "Amount"])
    table.align["Description"] = "l"
    table.align["Amount"] = "r"

    for entry in entries:
        amount_str = f"${entry.get('amount', 0):.2f}"
        table.add_row([
            entry.get("id"),
            entry.get("date"),
            entry.get("description"),
            amount_str
        ])

    print(table)
