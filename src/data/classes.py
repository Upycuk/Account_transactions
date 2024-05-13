class transactions:
    def __init__(self,
                 state: str,
                 date: str,
                 amount: str,
                 currency: str,
                 description: str,
                 from_: str,
                 to: str
    ):
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.from_ = from_
        self.to = to
