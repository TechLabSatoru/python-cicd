
import pytest
from main import add_integers

def test_正常系():
    assert add_integers(1, 1) == 2

def test_異常系_引数の値に浮動小数点を指定した場合():
    with pytest.raises(TypeError):
        add_integers(2, 2.5)
    with pytest.raises(TypeError):
        add_integers(2.5, 2)
