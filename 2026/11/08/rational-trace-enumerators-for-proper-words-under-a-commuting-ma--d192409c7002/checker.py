#!/usr/bin/env python3
"""Check exact trace enumerators for adjacent-distinct words by independent enumeration."""
from itertools import product
from collections import defaultdict


def from_gap_conditions(h, N):
    """Directly enumerate projected non-marker strings, tracking permissible marker counts."""
    linear = [0]*(N+1)
    circular = [0]*(N+1)
    linear[0] = circular[0] = 1
    linear[1] = 1  # single marker
    for m in range(1, N+1):
        for u in product(range(h), repeat=m):
            t = sum(u[i] == u[i+1] for i in range(m-1))
            for r in range(t, min(m+1, N-m)+1):
                linear[m+r] += 1
            tc = t + (u[-1] == u[0])
            for r in range(tc, min(m, N-m)+1):
                circular[m+r] += 1
    return linear, circular


def ratios(h, N):
    """Expand the two predicted rational functions using integer polynomial recurrences."""
    def inverse_one_minus(a, b):
        # 1/(1-a*z-b*z*z)
        vals = [0]*(N+1)
        vals[0]=1
        for n in range(1, N+1):
            vals[n] = a*vals[n-1] + (b*vals[n-2] if n>=2 else 0)
        return vals
    def power_linear(v):
        # divide by 1-z; cumulative coefficients
        total=0; out=[]
        for x in v:
            total += x
            out.append(total)
        return out
    def add_shift(v, shift, scale=1):
        return [scale*v[n-shift] if n>=shift else 0 for n in range(N+1)]
    def combine(*args):
        return [sum(v[n] for v in args) for n in range(N+1)]
    A = inverse_one_minus(h-1,1)
    B = inverse_one_minus(0,h)
    D = inverse_one_minus(-1,1)  # 1/(1+z-z*z), 1/(1-z*(z-1))
    lin_terms = combine(add_shift(A,1,h), add_shift(B,4,-h))
    lin = power_linear(lin_terms)
    lin[0] += 1; lin[1] += 1
    # cyclic: z*(h-1+z)/(1-z*(h-1+z)), and
    # (h-1) z*(z-1)/(1-z*(z-1)), and -h*z^3/(1-h*z²).
    E = inverse_one_minus(h-1,1)
    cyc_terms = combine(add_shift(E,1,h-1), add_shift(E,2),
                        add_shift(D,2,h-1),add_shift(D,1,-(h-1)),
                        add_shift(B,3,-h))
    cyc = power_linear(cyc_terms)
    cyc[0] += 1
    return lin, cyc


def from_actual_words(h, N):
    """Count trace classes from complete word listings, not from gap conditions."""
    L=[]; C=[]
    for n in range(N+1):
        lin=set(); cyc=set()
        for w in product(range(h+1), repeat=n):
            if any(w[i]==w[i+1] for i in range(n-1)):
                continue
            signature = (tuple(v for v in w if v != h), sum(v==h for v in w))
            lin.add(signature)
            if n==0 or (n>=2 and w[0]!=w[-1]):
                cyc.add(signature)
        L.append(len(lin)); C.append(len(cyc))
    return L,C


def main():
    total=0
    for h in (2,3,4):
        N=9 if h==2 else 8 if h==3 else 7
        got=from_actual_words(h,N)
        gap=from_gap_conditions(h,N)
        exact=ratios(h,N)
        assert got==gap==exact, (h, got, gap, exact)
        total += 2*(N+1)
        print('h=',h, 'linear=',exact[0], 'circular=',exact[1])
    for h in (1,2,3,4,5,6,7):
        N = 8 if h>4 else 9
        gap=from_gap_conditions(h,N)
        exact=ratios(h,N)
        assert gap==exact, (h,gap,exact)
        total += 2*(N+1)
    print('PASS', total, 'coefficient comparisons, independent word and gap enumerations')


if __name__=='__main__':
    main()
