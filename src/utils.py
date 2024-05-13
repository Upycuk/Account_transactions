import json
from pathlib import Path


def load_json(path: Path) -> list[dict]:
    """

    :param path:
    :return:
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_executed_operation(operations: list[dict]):
    """

    :param operations:
    :return:
    """
    return [
        operation
        for operation in operations
        if operation.get("state") == "EXECUTED"
    ]
