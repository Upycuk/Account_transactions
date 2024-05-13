import datetime


class Transactions:
    def __init__(self,
                 state: str,
                 date: str,
                 amount: str,
                 currency: str,
                 description: str,
                 to: str,
                 from_: str = None
    ):
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.from_ = self.convert_payment_data(from_) if from_ is not None else ''
        self.to = self.convert_payment_data(to)


    def convert_payment_data(self, payment_data: str) -> str:
        """

        :param payment_data:
        :return:
        """
        if payment_data.startswith('Счет'):
            return f'Счет **{payment_data[-4:]}\n'
        return f'**** {payment_data[-4:]}\n'


    def convert_data(self) -> str:
        """

        :return:
        """
        iso_date = datetime.datetime.fromisoformat(self.date)
        return iso_date.strftime('%d.%m.%Y')


    def __lt__(self, other):
        return self.date < other.date


    def __gt__(self, other):
            return self.date > other.date
