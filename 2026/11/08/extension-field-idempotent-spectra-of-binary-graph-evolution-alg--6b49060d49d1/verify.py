#!/usr/bin/env python3
"""Independent direct finite-field tests of an idempotent-extension count."""
from itertools import product
from functools import reduce

def mul(a,b,f,poly):
    out=0
    for _ in range(f):
        if b&1: out^=a
        b>>=1
        a<<=1
        if a & (1<<f): a^=poly
    return out & ((1<<f)-1)

def mat_vec(rows,v,n):
    return tuple(sum(((rows[i]>>j)&1)*v[j] for j in range(n))&1 for i in range(n))

def power_mat(rows,n,k):
    v=[tuple(int(j==i) for j in range(n)) for i in range(n)]
    # columns of identity, matrix action repeated
    for _ in range(k):
        v=[mat_vec(rows,col,n) for col in v]
    return [[v[j][i] for j in range(n)] for i in range(n)]

def nullity_af_minus_i(rows,n,f):
    power=power_mat(rows,n,f)
    # build rows of A^f+I
    a=[sum((power[i][j]^(i==j))<<j for j in range(n)) for i in range(n)]
    rk=0
    for col in range(n):
        piv=next((i for i in range(rk,n) if (a[i]>>col)&1),None)
        if piv is None: continue
        a[rk],a[piv]=a[piv],a[rk]
        for i in range(n):
            if i!=rk and (a[i]>>col)&1: a[i]^=a[rk]
        rk+=1
    return n-rk

def brute(rows,n,f,poly):
    q=1<<f
    sq=[mul(a,a,f,poly) for a in range(q)]
    count=0
    for x in product(range(q),repeat=n):
        y=tuple(sq[z] for z in x)
        if all(x[i] == reduce(lambda a,b:a^b, (y[j] for j in range(n) if rows[i]>>j&1),0) for i in range(n)):
            count+=1
    return count

def checks():
    # F2, F4, F8 exhaustive all binary structure matrices through dimension 3.
    for n, f, poly in ((1,1,0b11),(2,1,0b11),(3,1,0b11),(2,2,0b111),(3,2,0b111),(2,3,0b1011),(3,3,0b1011)):
        for flat in range(1<<(n*n)):
            rows=tuple((flat>>(n*i))&((1<<n)-1) for i in range(n))
            got=brute(rows,n,f,poly)
            want=1<<nullity_af_minus_i(rows,n,f)
            assert got==want, (n,f,flat,got,want)
        print('ALL_BINARY_MATRICES_OK',n,f,1<<(n*n))
    # dimension-four selected mixed cycles, triangular, and singular matrices over F16.
    for rows in ((2,4,8,1),(2,4,8,0),(3,6,12,9),(0,0,0,0),(1,2,4,8),(15,7,3,1)):
        assert brute(rows,4,4,0b10011)==1<<nullity_af_minus_i(rows,4,4),rows
    print('DIMENSION_FOUR_F16_OK')
    assert brute((4,5,2),3,7,0b10000011)==8
    print('DEGREE_SEVEN_DELAYED_IDEMPOTENTS_OK')
    # Directed cycle: exactly 2^gcd(n,f) idempotents for n<=8, 1<=f<=20.
    from math import gcd
    for n in range(1,9):
        rows=tuple(1<<((i+1)%n) for i in range(n))
        for f in range(1,21):
            assert 1<<nullity_af_minus_i(rows,n,f)==1<<gcd(n,f)
    print('DIRECTED_CYCLES_OK')
    print('VERIFY_OK')
if __name__=='__main__':checks()
