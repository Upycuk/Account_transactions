from src.classes import Transactions
from src.utils import get_executed_transactions


def test_get_executed_transactions():
    transactions = [
        {"state": "EXECUTED"},
        {"state": "EXECUTED"},
        {},
        {['qwerty']}
    ]

    executed_transactions = [
        {"state": "EXECUTED"},
        {"state": "EXECUTED"},
    ]

    assert get_executed_transactions(transactions) == executed_transactions


def test_transaction_instance():
    t = Transactions(
        state = "EXECUTED",
        date = "2019-08-26T10:50:58.294041",
        amount = "31957.58",
        currency = "руб.",
        description = "Перевод организации",
        from_ = "Maestro 1596837868705199",
        to = "Счет 64686473678894779589"
    )

    assert t.state == "EXECUTED"
    assert t.date == "26.08.2019"
    assert t.amount == "31957.58"
    assert t.currency == "руб."
    assert t.description == "Перевод организации"
    assert t.from_ == "Maestro  159683** **** 5199"
    assert t.to == "**9589"


def test_transaction_instance_none_from():
    t = Transactions(
        state = "EXECUTED",
        date = "2019-08-26T10:50:58.294041",
        amount = "31957.58",
        currency = "руб.",
        description = "Перевод организации",
        from_ = None,
        to = "Счет 64686473678894779589"
    )

    assert t.from_ == ""
