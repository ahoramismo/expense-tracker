import argparse


def create_parser():
    """
    supported commands
    1. add
    2. update
    3. delete
    4. view list (with filter)
    5. view summary (with filter)
    TODO: add help text to each command
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    # Update command
    update_parser = subparsers.add_parser(
        "update", help="Update the existing expense")
    update_parser.add_argument("--description", required=False)
    update_parser.add_argument("--amount", type=float, required=False)

    # Delete command
    delete_parser = subparsers.add_parser(
        "delete", help="Delete an expense entry")
    delete_parser.add_argument("--id", type=int, required=False)

    # List command
    list_parser = subparsers.add_parser(
        "list", help="visualize expense entries")
    list_parser.add_argument("--year", type=int, required=False)
    list_parser.add_argument("--month", type=int, required=False)
    list_parser.add_argument("--date", type=int, required=False)
    list_parser.add_argument("--filter", type=str, required=False)

    # Summary command
    summary_parser = subparsers.add_parser("summary", help="visualize entries")
    summary_parser.add_argument("--year", type=int, required=False)
    summary_parser.add_argument("--month", type=int, required=False)
    summary_parser.add_argument("--date", type=int, required=False)
    summary_parser.add_argument("--filter", type=str, required=False)
    
    return parser
