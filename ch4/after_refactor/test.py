from province import Province
from data import sampleProvinceData
import pytest


@pytest.fixture()
def asia():
    return Province(sampleProvinceData())


@pytest.fixture()
def no_producers():
    return {
        'name': "No producers", 
        'producers': [], 
        'demand': 30, 
        'price': 20
    }


@pytest.mark.usefixtures('asia', 'no_producers')
class TestProvince:
    def test_shortfall(self, asia):
        assert asia.shortFall == 5

    def test_profit(self, asia):
        assert asia.profit == 230

    def test_change_production(self, asia):
        asia.producers[0].production = 20
        assert asia.shortFall == -6
        assert asia.profit == 292

    def test_no_producers(self, no_producers):
        noProducers = Province(no_producers)
        assert noProducers.shortFall == 30
        assert noProducers.profit == 0

    def test_zero_demand(self, asia):
        asia.demand = 0
        assert asia.shortFall == -25
        assert asia.profit == 0

    def test_negative_demand(self, asia):
        asia.demand = -1
        assert asia.shortFall == -26
        assert asia.profit == -10

    def test_empty_demand(self, asia):
        asia.demand = ""
        assert asia.shortFall == None
        assert asia.profit == None