import datetime
import re


class Transactions:
    def __init__(self,
                 state: str,
                 date: str,
                 amount: str,
                 currency: str,
                 description: str,
                 to: str,
                 from_: str | None
    ):
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.from_ = from_ if from_ is not None else ''
        self.to = to


    def convert_from(self) -> str:
        """

        :return:
        """
        if self.from_:
            result = "".join(re.findall(r'\d+', self.from_))
            from_ = "".join(self.from_)
            name = from_.replace(result, '')
            return f'{name} {result[:6]}** **** {result[-4:]}'
        else:
            return ''


    def convert_to(self) -> str:
        """

        :return:
        """
        result = "".join(re.findall(r'\d+', self.to))
        return f'**{result[-4:]}'


    def convert_data(self) -> str:
        """

        :return:
        """
        iso_date = datetime.datetime.fromisoformat(self.date)
        return iso_date.strftime('%d.%m.%Y')


    def convert_description(self):
        """

        :return:
        """
        return self.description


    def convert_operationAmount_amount(self):
        return self.amount


    def convert_operationAmount_currency(self):
        return self.currency


    def __lt__(self, other):
        return self.date < other.date


    def __gt__(self, other):
            return self.date > other.date


    def __str__(self):
        return (f'{self.convert_data()} {self.convert_description()}\n'
                f'{self.convert_from()} -> {self.convert_to()}\n'
                f'{self.convert_operationAmount_amount()} {self.convert_operationAmount_currency()}\n')
