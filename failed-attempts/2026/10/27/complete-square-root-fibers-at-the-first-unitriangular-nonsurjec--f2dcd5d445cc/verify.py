#!/usr/bin/env python3
"""Finite-field checks of square-root fibers of the five-step unitriangular group.

The program independently enumerates the polynomial square map over F_2 and F_4,
then compares every target with the closed ten-stratum formula. Its finite checks
are not a proof over all finite fields.
"""
from collections import Counter
from itertools import product


def mul(x, y, q):
    if q == 2:
        return x & y
    if q == 4:
        r = 0
        a = x
        b = y
        while b:
            if b & 1:
                r ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 0b111  # T^2 + T + 1
        return r
    raise ValueError(q)


def field_add(x, y):
    return x ^ y


def prediction(q, target):
    A, B, C, D, E, F = target
    count = 0
    if A and C and B:
        count += (q - 1) * q**3
    if (bool(A) != bool(C)) and B == 0:
        count += (q - 1)**2 * q**3
    if A == B == C == 0:
        if D == E == 0:
            count += (q - 1)**2 * q**4
        elif D and E:
            count += (q - 1) * q**4
    if A and C == 0:
        count += (q - 1) * q**3
    if C and A == 0:
        count += (q - 1) * q**3
    if A == B == C == E == 0:
        count += (q - 1) * q**5
    if A == B == C == D == 0:
        count += (q - 1) * q**5
    if A == C == 0 and mul(B, F, q) == mul(D, E, q):
        if not any((B, D, E, F)):
            count += (2*q*q - 1) * q**4
        else:
            count += (q - 1) * q**4
    return count


def mapped(a,b,c,d,e,f,g,h,i,q):
    m = lambda x,y:mul(x,y,q)
    return (m(a,b),m(b,c),m(c,d),
            field_add(m(a,f),m(e,c)),
            field_add(m(b,g),m(f,d)),
            field_add(field_add(m(a,i),m(e,g)),m(h,d)))


def literal_square(a,b,c,d,e,f,g,h,i,j,q):
    entries = {(0,1):a,(1,2):b,(2,3):c,(3,4):d,
               (0,2):e,(1,3):f,(2,4):g,
               (0,3):h,(1,4):i,(0,4):j}
    target=[]
    for r,s in ((0,2),(1,3),(2,4),(0,3),(1,4),(0,4)):
        value=0
        for k in range(r+1,s):
            value^=mul(entries[r,k],entries[k,s],q)
        target.append(value)
    return tuple(target)


def check(q):
    histogram=Counter()
    # The 10th variable j = X[0,4] is invisible to X^2: count its q choices.
    for a,b,c,d,e,f,g,h,i in product(range(q),repeat=9):
        histogram[mapped(a,b,c,d,e,f,g,h,i,q)] += q
    for t in product(range(q),repeat=6):
        expected=prediction(q,t)
        observed=histogram[t]
        assert expected==observed, (q,t,expected,observed)
    assert sum(histogram.values())==q**10
    expected_image=q**6-q**5+q**4+q**3-q**2
    assert len(histogram)==expected_image,(q,len(histogram),expected_image)
    assert histogram[(0,)*6]==5*q**6-4*q**5
    # Independent literal multiplication of the underlying matrix.
    if q==2:
        iterates=product(range(q),repeat=10)
    else:
        # Reproducible diagonal-selection sample, not a randomized claim.
        iterates=((k%q,(k//q)%q,(k//q**2)%q,(k//q**3)%q,
                   (3*k+1)%q,(5*k+1)%q,(7*k+1)%q,(11*k+2)%q,
                   (13*k+2)%q,(17*k+3)%q) for k in range(4096))
    for v in iterates:
        assert mapped(*v[:9],q)==literal_square(*v,q)
    print('PASS',q,'image',expected_image,'domain',q**10,
          'zero_fiber',histogram[(0,)*6],'targets',q**6)

if __name__=='__main__':
    for Q in (2,4):
        check(Q)
    print('VERIFY_OK_UT5_SQUARE_FIBERS')
