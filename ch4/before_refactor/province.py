from producer import Producer


class Privince:
    def __init__(self, doc) -> None:
        self._name = doc.name 
        self._producers = []
        self._totalProduction = 0
        self._demand = doc.demand
        self._price = doc.price 
        map(lambda d: self.addProducer(Producer(self, d)), doc.producers)

    def addProducer(self, arg) -> None:
        self._producers.append(arg)
        self._totalProduction += arg.production

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
        self._demand = int(arg)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, arg):
        self._price = int(arg)

    @property
    def shortFall(self):
        return self._demand - self.totalProduction

    @property
    def profit(self):
        return self.demandValue - self.demandCost

    @property
    def demandCost(self):
        remainingDemand = self.demand
        result = 0
        self.prodcers = [p.cost for p in self.producers].sort()
        for p in self.producers:
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