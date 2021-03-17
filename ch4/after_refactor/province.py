from producer import Producer
from functools import reduce

class Province:
    def __init__(self, doc) -> None:
        self._name = doc['name']
        self._producers = []
        self._totalProduction = 0
        self._demand = doc['demand']
        self._price = doc['price']
        for d in doc['producers']:
            self.addProducer(Producer(self, d))

    def addProducer(self, arg) -> None:
        self._producers.append(arg)
        self._totalProduction += arg.production
        return self._totalProduction

    @property
    def name(self):
        return self._name

    @property
    def producers(self):
        return self._producers[:]
    
    @property
    def totalProduction(self):
        return self._totalProduction

    @totalProduction.setter
    def totalProduction(self, arg):
        self._totalProduction = arg

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, arg):
        self._demand = int(arg) if arg != '' else None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, arg):
        self._price = int(arg) if arg != '' else None

    @property
    def shortFall(self):
        try:
            return self._demand - self.totalProduction
        except TypeError:
            return None

    @property
    def profit(self):
        try:
            return self.demandValue - self.demandCost
        except TypeError:
            return None

    @property
    def demandCost(self):
        remainingDemand = self.demand
        result = 0
        # self.prodcers = [p.cost for p in self.producers].sort()
        for p in sorted(self.producers, key=lambda p: p.cost):
            constribution = min(remainingDemand, p.production)
            remainingDemand -= constribution
            result += constribution * p.cost
        return result


    @property
    def demandValue(self):
        return self.satisfiedDemand * self.price

    @property
    def satisfiedDemand(self):
        return min(self._demand, self.totalProduction)