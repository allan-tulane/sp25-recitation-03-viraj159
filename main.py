"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    # Convert x and y to binary vector
    xvec = x.binary_vec
    yvec = y.binary_vec

    # Pad xvec and yvec so they have the same length
    xvec, yvec = pad(xvec, yvec)

    # Base case: if length is 1, then multiply the single bits
    if len(xvec) == 1:
        return BinaryNumber(int(xvec[0]) * int(yvec[0]))

    # Split xvec and yvec into left and right
    mid = len(xvec) // 2
    x_left = binary2int(xvec[:mid])
    x_right = binary2int(xvec[mid:])
    y_left = binary2int(yvec[:mid])
    y_right = binary2int(yvec[mid:])

    # Recursively compute products
    A = _quadratic_multiply(x_left, y_left)    
    B = _quadratic_multiply(x_left, y_right)  
    C = _quadratic_multiply(x_right, y_left)  
    D = _quadratic_multiply(x_right, y_right)

    # Combine results
    n = len(xvec)
    A_shifted = bit_shift(A, n)

    # Shift (B + C) by n/2 bits
    BC_sum = BinaryNumber(B.decimal_val + C.decimal_val)
    BC_shifted = bit_shift(BC_sum, n // 2)

    # Final results
    result = A_shifted.decimal_val + BC_shifted.decimal_val + D.decimal_val

    return BinaryNumber(result)


def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    
    return (time.time() - start)*1000


    
    

