from province import Province
from data import sampleProvinceData
import pytest


@pytest.fixture()
def asia():
    return Province(sampleProvinceData())


@pytest.mark.usefixtures('asia')
class TestProvince:
    def test_shortfall(self, asia):
        assert asia.shortFall == 5

    def test_profit(self, asia):
        assert asia.profit == 230

    def test_change_production(self, asia):
        asia.producers[0].production = 20
        assert asia.shortFall == -6
        assert asia.profit == 292
