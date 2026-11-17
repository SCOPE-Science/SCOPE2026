"""Exhaustive finite checks of nilpotency indices in rectangular Jordan centralizers.

Run: python verify_power.py
Only prime fields are needed for these finite test cases; the mathematical theorem
covers all prime powers by an independent argument.
"""
from itertools import product
from math import prod


def mul(x, y, r, n, q):
    z = [0] * (r*r*n)
    # coefficients at t^d are row-major r-by-r matrices
    for d in range(n):
        for u in range(d+1):
            v=d-u
            for i in range(r):
                for k in range(r):
                    a=x[u*r*r+i*r+k]
                    if not a: continue
                    for j in range(r):
                        z[d*r*r+i*r+j] += a*y[v*r*r+k*r+j]
    return tuple(a%q for a in z)


def power_index(x,r,n,q):
    zero=(0,)*(n*r*r)
    t=x
    for j in range(1,r*n+1):
        if t==zero: return j
        t=mul(t,x,r,n,q)
    return None


def gl_order(q,r):
    return prod(q**r-q**i for i in range(r))


def verify(r,n,q):
    regular=nilpotent=0
    for x in product(range(q),repeat=n*r*r):
        k=power_index(x,r,n,q)
        if k is not None:
            nilpotent += 1
            if k ==r*n: regular += 1
    expect_n=q**(n*r*r-r)
    expect_reg=gl_order(q,r)*q**(r*r*(n-1)-r) if n>=2 else gl_order(q,r)//((q-1)*q**(r-1))
    assert (nilpotent,regular)==(expect_n,expect_reg), (r,n,q,nilpotent,regular,expect_n,expect_reg)
    print(f'CHECK q={q} r={r} n={n}: nilpotent={nilpotent} regular={regular} OK',flush=True)

if __name__=='__main__':
    for r,n,q in [(2,1,2),(2,2,2),(2,3,2),(2,2,3),(3,2,2)]:verify(r,n,q)
    print('VERIFY_OK')
