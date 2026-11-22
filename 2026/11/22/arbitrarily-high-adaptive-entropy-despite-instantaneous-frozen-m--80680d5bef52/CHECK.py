"""Exact arithmetic checks for a family of two-state adaptive transfer maps.

Run: python CHECK.py
"""
from fractions import Fraction as Q

A, B = Q(1, 8), Q(1, 4)
C, D = Q(3, 4), Q(7, 8)

def q(x, m):
    assert m >= 2 and Q(0) <= x <= Q(1)
    if x <= A:
        return C
    if x < B:
        v = m * (x - A) / (B - A)
        j = v.numerator // v.denominator
        s = v - j
        return C + (D-C) * s if j % 2 == 0 else D - (D-C) * s
    if x <= Q(3,8):
        endpoint = D if m % 2 else C
        return endpoint + (Q(7,16)-endpoint)*(x-B)/(Q(3,8)-B)
    if x <= Q(5,8):
        return Q(1,4)+x/2
    if x < C:
        return Q(9,16)+(B-Q(9,16))*(x-Q(5,8))/(C-Q(5,8))
    if x <= D:
        return Q(1)-x
    return A

def breakpoints(m):
    return sorted({Q(0), Q(1), B, Q(3,8), Q(1,2), Q(5,8), C, D} |
                  {A + (B-A)*Q(j,m) for j in range(m+1)})

def f2(x,m):
    return q(q(x,m),m)

def primitive_period(point, m, horizon):
    x = point
    for k in range(1,horizon+1):
        x = q(x,m)
        if x == point:
            return k
    return None

def periodic_symbolic_point(m, word):
    """Fixed point of the itinerary of full branches of q^2 on L."""
    alpha, beta = Q(1), Q(0)
    for j in word:
        aj = A + (B-A)*Q(j,m)
        if j % 2:
            slope, offset = Q(m), A-Q(m)*aj
        else:
            slope, offset = Q(-m), B+Q(m)*aj
        alpha, beta = slope*alpha, slope*beta+offset
    return beta/(1-alpha)

def main():
    tested = 0
    for m in range(2,19):
        bp=breakpoints(m)
        assert all(A <= q(x,m) <= D for x in bp)
        assert all((q(x,m) > x if x<Q(1,2) else
                    q(x,m) < x if x>Q(1,2) else q(x,m)==x) for x in bp)
        assert all(q(Q(1,2)+dx,m)==Q(1,2)+dx/2 for dx in (Q(0),Q(1,128),-Q(1,128)))
        for j in range(m+1):
            x = A+(B-A)*Q(j,m)
            assert f2(x,m) == (B if j%2==0 else A)
            tested += 1
        for k in range(1,9):
            word=(0,)*(k-1)+(1,) if k>1 else (0,)
            x=periodic_symbolic_point(m,word)
            assert A < x < B
            y=x
            for j in word:
                aj=A+(B-A)*Q(j,m)
                bj=aj+(B-A)/m
                assert aj <= y <= bj
                y=f2(y,m)
                tested+=1
            assert y==x
            assert primitive_period(x,m,2*k) == 2*k
    print('PASS: exact range, unique-fixed-point sign, local slope,')
    print('      M-branch endpoint covering and primitive even-period witnesses')
    print('      for m=2..18 and periods 2..16; exact comparisons:', tested)

if __name__=='__main__':
    main()
