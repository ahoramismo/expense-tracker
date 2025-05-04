import argparse


def add_common_date_filters(parser):
    parser.add_argument("--year", type=int, help="Filter by year (e.g., 2025)")
    parser.add_argument("--month", type=int, help="Filter by month (1-12)")
    parser.add_argument("--date", type=int, help="Filter by day of the month (1-31)")
    parser.add_argument("--filter", type=str, help="Keyword filter for descriptions")


def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense (e.g., 'Lunch')")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount spent (e.g., 12.50)")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument("--id", type=int, required=True, help="ID of the expense to update")
    update_parser.add_argument("--description", help="New description for the expense")
    update_parser.add_argument("--amount", type=float, help="New amount for the expense")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete an expense entry")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense to delete")

    # List command
    list_parser = subparsers.add_parser("list", help="List expense entries with optional filters")
    add_common_date_filters(list_parser)

    # Summary command
    summary_parser = subparsers.add_parser("summary", help="Show a summary of expenses")
    add_common_date_filters(summary_parser)

    return parser
