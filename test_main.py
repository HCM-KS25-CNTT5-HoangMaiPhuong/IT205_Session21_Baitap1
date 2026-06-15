from main import deposit
import pytest   
def test_positive_value():
    assert deposit(0) == 0
    
def test_string_value ():
    with pytest.raises(ValueError) :
        deposit(0,"abc")