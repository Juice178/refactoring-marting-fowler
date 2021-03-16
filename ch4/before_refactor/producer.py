class Producer:
    def __init__(self, aProvince, data) -> None:
        self._province = aProvince
        self._cost = data.cost
        self._name = data.name
        self._production = data.production or 0
    
    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, arg):
        self._cost = int(arg)

    @property
    def production(self):
        return self._production

    @production.setter
    def production(self, amountStr):
        amount = int(amountStr)
        newProduction = 0 if amount is None else amount
        self._province.totalProduction += newProduction - self._production
        self._production = newProduction