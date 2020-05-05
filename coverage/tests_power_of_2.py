import pytest
from .code_challenges.scripts.power_of_2 import is_power2, recurse_power

def test_self():
    check_4 = is_power2(4)
    check_3 = is_power2(3)
    assert (check_4 == True) & (check_3 == False)
