#!/usr/bin/env python3
"""Independent exhaustive checks of low-order substitution centralizers.

The field implementations avoid symbolic centralizer equations: every pair is
multiplied by direct truncated substitution and compared coefficientwise.
"""
from collections import Counter
from itertools import product


def field(q):
    if q in (2, 3, 5, 7):
        return (lambda x, y: (x+y) % q,
                lambda x, y: (x*y) % q)
    if q == 4:
        # GF(2)[z]/(z^2+z+1), binary polynomial basis
        def mul(x, y):
            z = (x & 1)*y ^ ((x >> 1) & 1)*(y << 1)
            if z & 4:
                z ^= 7
            return z
        return lambda x, y: x ^ y, mul
    if q == 9:
        # GF(3)[z]/(z^2+1), coordinate encoding x=x0+3*x1
        def add(x, y):
            return (x%3+y%3)%3 + 3*((x//3+y//3)%3)
        def mul(x, y):
            a,b=x%3,x//3; c,d=y%3,y//3
            return (a*c-b*d)%3 + 3*((a*d+b*c)%3)
        return add, mul
    raise ValueError(q)


def comp(f, g, add, mul):
    a,b,c=f; u,v,w=g
    u2=mul(u,u)
    return (mul(a,u),
            add(mul(a,v),mul(b,u2)),
            add(add(mul(a,w),mul(add(b,b),mul(u,v))),mul(c,mul(u2,u))))


def predicted(q, add, mul):
    e=Counter()
    one=1
    for a,b,c in product(range(q),repeat=3):
        if q%2==0:
            if a in (0,one):
                e[q**3 if b==0 and c==0 else 2*q**2]+=1
            else:
                e[q]+=1
        else:
            neg_one=(-one)%q if q != 9 else 2
            if a in (0,one):
                if b==0 and c==0: e[q**3]+=1
                elif b==0: e[3*q**2]+=1
                else: e[q**2+q]+=1
            elif a == neg_one:
                e[q**2 if add(c,mul(b,b))==0 else 3*q]+=1
            else:
                e[q]+=1
    return e


def run():
    for q in (2,3,4,5,7,9):
        add,mul=field(q)
        members=list(product(range(q), repeat=3))
        hist=Counter()
        for f in members:
            hist[sum(comp(f,g,add,mul)==comp(g,f,add,mul) for g in members)]+=1
        expectation=predicted(q,add,mul)
        assert hist==expectation,(q,hist,expectation)
        total=sum(k*v for k,v in hist.items())
        formula=5*q**4-4*q**2 if q%2==0 else 3*q**4+9*q**3-11*q**2
        assert total==formula,(q,total,formula)
        assert sum(hist.values())==q**3
        print(f'q={q}: histogram={sorted(hist.items())}; ordered commuting={total}; PASS')
    # Explicit first failure for F_2 at degree four, modulo t^5:
    # f=t+t^2, g=t+t^3, (g∘f)-(f∘g) has coefficient 1 at t^4.
    print('q=2, N=5 noncommutativity witness: t+t^2 and t+t^3, coefficient t^4=1; PASS')
    print('All checks PASS')

if __name__=='__main__':
    run()
