import pytest
from .code_challenges.scripts.power_of_2 import is_power2

def test_self():
    check_2 = is_power2(2)
    check_4 = is_power2(4)
    check_8 = is_power2(8)
    check_16 = is_power2(16)
    check_32 = is_power2(32)
    check_20 = is_power2(20)
    assert (check_2 == True) & (check_4 == True) & (check_8 == True) & \
           (check_16 == True) & (check_32 == True) & (check_20 == False)
