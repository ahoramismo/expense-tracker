from prettytable import PrettyTable


def draw(entries):
    """
    This function creates a table to display the expenses.
    """

    # Create a PrettyTable object
    table = PrettyTable()

    # Define the columns
    table.field_names = ["ID", "Date", "Description", "Amount"]

    # Add some sample data
    if not entries:
        print("No entries found.")
        return
    # Add rows to the table
    for entry in entries:
        table.add_row([entry["id"], entry["date"],
                      entry["description"], entry["amount"]])

    # Print the table
    print(table)
