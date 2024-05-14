from settings import TRANSACTION_PATH
from src.utils import load_json, get_executed_transactions, get_transactions_instanses, sort_transactions_by_date

transactions = load_json(TRANSACTION_PATH)
executed_transactions = get_executed_transactions(transactions)
transactions_instanses = get_transactions_instanses(executed_transactions)
sort = sort_transactions_by_date(transactions_instanses)

for transaction in sort[:5]:
    print(transaction)
