from province import Province
from data import sampleProvinceData
import pytest


@pytest.fixture()
def asia():
    return Province(sampleProvinceData())

@pytest.mark.usefixtures('asia')
class TestProvince:
    def test_shortfall(self, asia):
        #asia = Province(sampleProvinceData())
        assert asia.shortFall == 5

    def test_province(self, asia):
        #asia = Province(sampleProvinceData())
        assert asia.profit == 230