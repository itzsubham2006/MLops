import pytest

def square(n):
    return n**2

def cube(n):
    return n**3


def test_square():
    assert square(2)==4, "Test failed: Square of 2 should be 4"
    
def test_cube():
    assert cube(2)==8, "Test failed: Cube of 2 should be 8"
    

def test_invalid():
    with pytest.raises(TypeError):
        square("string")