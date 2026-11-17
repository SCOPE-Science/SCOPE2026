#!/usr/bin/env python3
"""Independent direct vertex-level check of the EGF basin formula.

Every labelled three-colouring on every complete split graph of
2 <= a+b <= 10 is visited, and its eventual least period computed.
"""
from itertools import product
from math import comb, factorial


def direct_step(states, a):
    counts = [0, 0, 0]
    clique = [0, 0, 0]
    for i, c in enumerate(states):
        counts[c] += 1
        if i < a:
            clique[c] += 1
    after = []
    for i, c in enumerate(states):
        successor = (c + 1) % 3
        target_count = counts[successor] if i < a else clique[successor]
        after.append((c + (target_count >= 2)) % 3)
    return tuple(after)


def U(n):
    return 0 if n < 2 else 1


def count_expected(a, b):
    # Literal coefficient extraction of the five EGF summands, using
    # exact rational factorial coefficients (no finite-state lookup).
    from fractions import Fraction
    def egf_e(n,k): return Fraction(k**n, factorial(n)) if n>=0 else Fraction(0)
    def egf_u(n): return Fraction(1,factorial(n)) if n>=2 else Fraction(0)
    def egf_v(n): return egf_u(n)
    def coefficient_product(fs, n):
        if not fs: return int(n==0)
        return sum(fs[0](j)*coefficient_product(fs[1:],n-j) for j in range(n+1))
    def ez(k): return lambda n: egf_e(n,k)
    one=lambda n: int(n==0)
    z=lambda n: int(n==1)
    z2=lambda n: int(n==2)
    z3=lambda n: int(n==3)
    # U(z)^3 exp(3w)
    total=coefficient_product([egf_u]*3,a)*egf_e(b,3)
    # 3 U(z)^2 exp(2w) V(w)
    total+=3*coefficient_product([egf_u]*2,a)*coefficient_product([ez(2),egf_v],b)
    # 3 z U(z)^2 exp(2w) (V(w)+w)
    total+=3*coefficient_product([egf_u]*2+[z],a)*coefficient_product([ez(2),lambda n: egf_v(n)+z(n)],b)
    # 3 V(w)^3 (z+z^2)
    total+=3*(z(a)+z2(a))*coefficient_product([egf_v]*3,b)
    # z^3 (V(w)+w)^3
    total+=z3(a)*coefficient_product([lambda n: egf_v(n)+z(n)]*3,b)
    ans=total*factorial(a)*factorial(b)
    assert ans.denominator==1
    return int(ans)


def main():
    total = 0
    max_time = 0
    checked = 0
    for s in range(2,11):
        for a in range(1,s):
            b=s-a
            observed=0
            for state in product(range(3), repeat=s):
                checked+=1
                x=state; seen={}
                while x not in seen:
                    seen[x]=len(seen)
                    x=direct_step(x,a)
                t=seen[x];p=len(seen)-t
                assert p in (1,3),(a,b,state,t,p)
                assert t <= 4,(a,b,state,t,p)
                max_time=max(max_time,t)
                if p==3:observed+=1
            expected=count_expected(a,b)
            assert observed==expected,(a,b,observed,expected)
            total+=1
    print('GRAPH_SIZES_CHECKED=%d'%total)
    print('LABELLED_INITIAL_STATES_CHECKED=%d'%checked)
    print('MAX_FIRST_PERIODIC_ENTRY=%d'%max_time)
    print('DIRECT_VS_EGF=PASS')
    print('ALL_ASSERTIONS=PASS')

if __name__=='__main__':
    main()
