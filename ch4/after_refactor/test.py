from province import Province
from data import sampleProvinceData

def test_shortfall():
    asia = Province(sampleProvinceData())
    assert asia.shortFall == 5