# Expense Tracker CLI

A simple command-line tool to track your expenses. This application allows you to add, update, delete, list, and summarize your expenses, all through an easy-to-use CLI.

## Project Acknowledgment

This project is inspired by the [Expense Tracker Project](https://roadmap.sh/projects/expense-tracker) from [Roadmap.sh](https://roadmap.sh). The goal is to implement a simple yet functional expense tracker with various features like adding, updating, deleting, and listing expenses.

---

## Features

- **Add** a new expense
- **Update** an existing expense
- **Delete** an expense
- **List** all expenses with optional filters
- **Summary** of total expenses with optional filters

## Installation

1. Install [Poetry](https://python-poetry.org/docs/#installation) (if not already installed):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/ahoramismo/expense-tracker.git
    ```

3. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

4. Run the application using Poetry's virtual environment:
    ```bash
    poetry run expense-tracker <command> [options]
    ```



## Commands

- `add`: Add a new expense
  - `--description`: Description of the expense
  - `--amount`: Amount of the expense
  
- `update`: Update an existing expense
  - `--id`: ID of the expense
  - `--description`: (Optional) New description
  - `--amount`: (Optional) New amount

- `delete`: Delete an expense
  - `--id`: ID of the expense

- `list`: List all expenses
  - `--year`: (Optional) Filter by year
  - `--month`: (Optional) Filter by month
  - `--date`: (Optional) Filter by date
  - `--filter`: (Optional) Filter by description

- `summary`: Get the total amount spent
  - `--year`: (Optional) Filter by year
  - `--month`: (Optional) Filter by month
  - `--date`: (Optional) Filter by date
  - `--filter`: (Optional) Filter by description

## Example Usage

1. **Add an expense**:
    ```bash
    expense-tracker add --description "Lunch" --amount 20
    ```

2. **Update an expense**:
    ```bash
    expense-tracker update --id 1 --description "Lunch at cafe" --amount 25
    ```

3. **Delete an expense**:
    ```bash
    expense-tracker delete --id 1
    ```

4. **List all expenses**:
    ```bash
    expense-tracker list
    ```

5. **Get summary of expenses**:
    ```bash
    expense-tracker summary
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
