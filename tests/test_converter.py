import pytest
from aznum2words.converter import AzerbaijaniNumberConverter

@pytest.fixture
def converter():
    return AzerbaijaniNumberConverter()

def test_convert_zero(converter):
    assert converter.convert(0) == "sıfır"

def test_convert_positive_number(converter):
    assert converter.convert(123456789) == "yüz iyirmi üç milyon dörd yüz əlli altı min yeddi yüz səksən doqquz"

def test_convert_negative_number(converter):
    assert converter.convert(-123) == "mənfi yüz iyirmi üç"

def test_convert_large_number(converter):
    assert converter.convert(12345678901234567) == "on iki kvadrilyon üç yüz qırx beş trilyon altı yüz yetmiş səkkiz milyard doqquz yüz bir milyon iki yüz otuz dörd min beş yüz altmış səkkiz"

def test_convert_fractional_number(converter):
    assert converter.convert(123.4567) == "yüz iyirmi üç tam on mində dörd min beş yüz altmış yeddi"

def test_convert_negative_fractional_number(converter):
    assert converter.convert(-2.7021) == "mənfi iki tam on mində yeddi min iyirmi bir"
