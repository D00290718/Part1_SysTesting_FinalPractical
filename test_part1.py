#D00290718 - Samuel Delaney
#Y1 System Testing & CI Last Final Practical Lab 3. 06/05/26.

import pytest
from part1 import calculate_interest

def test_tier1():

    a = calculate_interest(10)
    assert a == "0.30"

def test_tier2():

    a = calculate_interest(5000)
    assert a == "170.00"

def test_tier3():

    a = calculate_interest(15000)
    assert a == "540.00"


def test_tier4():

    a = calculate_interest(250000)
    assert a == "10690.00"

def test_negative_input(): #Unit Testing: Your pytest implementation must check for invalid partitions as specified in the specification
    with pytest.raises(ValueError):
        calculate_interest(-10)
