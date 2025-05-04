from expense_tracker.core import Expense
from expense_tracker.parser import create_parser
from expense_tracker.storage import JSONStorage


def main():
    """
    TODO:
    - Add expense categories and allow users to filter expenses by category.
    - Allow users to set a budget for each month and show a warning when the user exceeds the budget.
    - Allow users to export expenses to a CSV file.
    """
    parser = create_parser()
    args = parser.parse_args()
    expense = Expense(storage=JSONStorage("database/expenses.json"))

    match args.command:
        case "add":
            expense.add(args.description, args.amount)
        case "update":
            expense.update(args.id, args.description, args.amount)
        case "delete":
            expense.delete(args.id)
        case "list":
            expense.list_expenses(args.year, args.month, args.date, args.filter)
        case "summary":
            expense.summary(args.year, args.month, args.date, args.filter)


if __name__ == '__main__':
    main()
