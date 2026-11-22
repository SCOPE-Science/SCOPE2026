#!/usr/bin/env python3
"""Standalone exact recurrence and binomid-column checks for a cyclotomic family."""
from fractions import Fraction
from math import gcd


def recurrence(q, t, length):
    a, b = -(t + 1), q
    out = [a, b]
    for _ in range(length - 2):
        a, b = b, -q*b - q*q*a
        out.append(b)
    return out


def gnom(f, n, k):
    if not (0 <= k <= n):
        raise ValueError("invalid generalized coefficient")
    result = Fraction(1, 1)
    for j in range(1, k+1):
        result *= Fraction(f[n-j+1], f[j])
    return result


def er(r, c, k, m):
    return (sum((m+i+j)%3==r for i in range(1,k+1) for j in range(c))
        - sum((i+j)%3==r for i in range(1,k+1) for j in range(c)))


def table():
    for c in range(1,4):
        for k in range(1,4):
            for m in range(1,4):
                e0,e2 = er(0,c,k,m),er(2,c,k,m)
                assert e0>=0 and e2>=-1
                if e2<0:
                    assert c*k*m>=4
    for c in range(1,14):
        for k in range(1,14):
            for m in range(0,14):
                assert er(0,c,k,m)==er(0,c%3 or 3,k%3 or 3,m%3 or 3)
                assert er(2,c,k,m)==er(2,c%3 or 3,k%3 or 3,m%3 or 3)
    return 13**3*2


def main():
    checks=table()
    for q,t in [(2,8),(2,16),(3,27),(3,81),(6,18),(6,36),(2,1),(5,125)]:
        assert q**4%t==0
        f=recurrence(q,t,48)
        assert all(f[n] == q**n * [-(t+1),1,t][n%3] for n in range(48))
        for c in range(1,11):
            column=[None]
            for n in range(1,32):
                v=gnom(f,n+c-1,c)
                assert v.denominator==1, (q,t,c,n,v)
                column.append(v.numerator)
            for n in range(1,32):
                for k in range(n+1):
                    z=gnom(column,n,k)
                    assert z.denominator==1,(q,t,c,n,k,z)
                    checks+=1
    for q,t in [(2,5),(2,32),(3,10),(6,1297)]:
        assert q**4%t
        f=recurrence(q,t,7)
        z=gnom(f,4,2)
        assert z.denominator !=1
        checks+=1
    q,t=2,8
    f=recurrence(q,t,9)
    assert f[2] == 32 and f[4] == 16 and f[4]%f[2] !=0
    assert gcd(t,t+1)==1
    print('VERIFY_OK; exact independent recurrence and column coefficients:', checks)
    print('Counterexample: f2=32, f4=16, first order-two nondivisibility')

if __name__=='__main__':
    main()
