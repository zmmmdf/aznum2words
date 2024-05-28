import pytest
from aznum2words.converter import AzerbaijaniNumberConverter

@pytest.fixture
def converter():
    return AzerbaijaniNumberConverter()

def test_convert_zero(converter):
    assert converter.convert(0) == "sıfır"

def test_convert_positive_number(converter):
    assert converter.convert(123456789) == "bir yüz iyirmi üç milyon dörd yüz əlli altı min yeddi yüz səkkiz doqquz"

def test_convert_negative_number(converter):
    assert converter.convert(-123) == "mənfi bir yüz iyirmi üç"

def test_convert_large_number(converter):
    assert converter.convert(1234567890123456789) == "bir kvadrilyon iki yüz otuz dörd trilyon beş yüz altmış yedi milyard səkkiz yüz doxsan milyon on iki min üç yüz qırx beş"
