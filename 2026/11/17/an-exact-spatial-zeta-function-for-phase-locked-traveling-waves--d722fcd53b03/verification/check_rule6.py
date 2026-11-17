#!/usr/bin/env python3
"""Independent integer checks for Rule 6 phase-locked traveling waves.

Requires Python 3 and sympy (for exact characteristic polynomial).
All finite-word checks are independent of the transfer-matrix trace.
"""
import sympy as sp


def f(a, b, c):
    return (1-a) * (b ^ c)


def allowed(v):
    a, b, c, d, e = v
    return f(f(a, b, c), f(b, c, d), f(c, d, e)) == e


def matrix():
    M = sp.zeros(16)
    for s in range(16):
        a,b,c,d = ((s >> j) & 1 for j in (3,2,1,0))
        for e in (0, 1):
            if allowed((a,b,c,d,e)):
                M[s, ((s << 1) & 15) | e] = 1
    return M


def update(x,n):
    y = 0
    for i in range(n):
        l=(x>>((i-1)%n))&1
        c=(x>>i)&1
        r=(x>>((i+1)%n))&1
        y |= ((1-l)*(c^r)) << i
    return y


def shifted_two(x,n):
    # (R^2 x)_i=x_{i+2}, with R sending cell i to cell i-1.
    return ((x >> 2) | (x << (n-2))) & ((1<<n)-1) if n>=2 else x


def main():
    M=matrix()
    t=sp.Symbol('t')
    z=sp.Symbol('z')
    expected=t**10*(t-1)*(t+1)**2*(t**3-2*t**2+2*t-2)
    computed=M.charpoly(t).as_expr()
    assert sp.expand(computed-expected)==0
    determinant=(1-z)*(1+z)**2*(1-2*z+2*z*z-2*z**3)
    assert sp.expand(sp.det(sp.eye(16)-z*M)-determinant)==0
    print('EXACT_MATRIX_CHARPOLY_PASS:',sp.factor(computed))
    print('EXACT_ZETA_DENOMINATOR_PASS:',sp.factor(determinant))
    total=0
    for n in range(3,16):
        trace=int(sp.trace(M**n))
        direct=0
        for x in range(1<<n):
            if update(update(x,n),n)==shifted_two(x,n):
                direct+=1
                # Periodicity follows algebraically from commutation.
                y=x
                for _ in range(2*n):
                    y=update(y,n)
                assert y==x
        assert trace==direct,(n,trace,direct)
        total+=1<<n
        print('RING',n,'PHASE_LOCKED',direct,'TRACE',trace,'PASS')
    print('DIRECT_BINARY_WORD_CHECKS',total)
    print('CHECKS_PASS')

if __name__=='__main__':main()
