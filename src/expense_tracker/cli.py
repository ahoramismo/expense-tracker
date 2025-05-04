import expense_tracker.core as core
from expense_tracker.parser import create_parser


def main():
    """
    supported commands
    1. add
    2. update
    3. delete
    4. view list (with filter)
    5. view summary (with filter)
    """

    parser = create_parser()
    args = parser.parse_args()

    match args.command:
        case "add":
            core.add(args.description, args.amount)
        case "update":
            core.update(args.description, args.amount)
        case "delete":
            core.delete(args.id)
        case "list":
            core.list_expenses(args.year, args.month, args.date, args.filter)
        case "summary":
            core.summary(args.year, args.month, args.date, args.filter)


if __name__ == 'main':
    main()
