import json
from pathlib import Path

from src.classes import Transactions


def load_json(path: Path) -> list[dict]:
    """

    :param path:
    :return:
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_executed_transactions(transactions: list[dict]):
    """

    :param transactions:
    :return:
    """
    return [
        transaction
        for transaction in transactions
        if transaction.get("state") == "EXECUTED"
    ]


def get_transactions_instanses(transactions: list[dict]) -> list[Transactions]:
    """

    :param transactions:
    :return:
    """
    transactions_instanses = []
    for transaction in transactions:
        transact = Transactions(
            state = transaction["state"],
            date = transaction["date"],
            amount = transaction["operationAmount"]["amount"],
            currency = transaction["operationAmount"]["currency"]["name"],
            description = transaction["description"],
            to = transaction["to"],
            from_ = transaction.get("from"),
        )
        transactions_instanses.append(transact)
    return transactions_instanses


def sort_transactions_by_date(transactions: list[Transactions]) -> list[Transactions]:
    return sorted(transactions)
