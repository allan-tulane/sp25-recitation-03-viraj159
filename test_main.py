from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 9
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(6)) == 30
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 100
