#!/usr/bin/env python3
"""Reproducible finite checks for recent-window recursive-tree ancestry depth.

Standard-library only.  These computations check finite instances; the asymptotic
central limit theorem is proved analytically in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import isqrt, log

TESTS = 0


def check(condition, message='assertion failed'):
    global TESTS
    TESTS += 1
    if not condition:
        raise AssertionError(message)


def cube_root_floor(x):
    lo, hi = 0, x + 1
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if m**3 <= x: lo = m
        else: hi = m
    return lo


def window(l, kind):
    """Exact width for beta=1/3, 1/2, or 2/3, at child label l."""
    if l == 1: return 0
    z = l - 1
    if kind == 'third': w = cube_root_floor(z)
    elif kind == 'half': w = isqrt(z)
    elif kind == 'two_thirds': w = cube_root_floor(z*z)
    else: raise ValueError(kind)
    return min(l - 1, 1 + w)


def exact_depth_distribution(n, kind):
    # Dynamic backward-ancestry recurrence.
    laws = [{0: Fraction(1)} for _ in range(n+1)]
    for l in range(2,n+1):
        b = window(l, kind)
        out = defaultdict(Fraction)
        for j in range(1,b+1):
            for t,p in laws[l-j].items(): out[t+1] += p/b
        laws[l] = dict(out)
    return laws[n]


def independent_full_tree_enumeration(n, kind):
    # Enumerate independent attachment choices of ALL vertices, not a backward walk.
    widths = [window(l,kind) for l in range(2,n+1)]
    denom = 1
    for w in widths: denom *= w
    counts = defaultdict(int)
    for jumps in product(*[range(1,w+1) for w in widths]):
        parent = {l:l-jumps[l-2] for l in range(2,n+1)}
        pos,t = n,0
        while pos != 1:
            pos=parent[pos]; t += 1
        counts[t] += 1
    return {t:Fraction(c,denom) for t,c in counts.items()}


def potential(n,kind):
    return sum((Fraction(2,window(l,kind)+1) for l in range(2,n+1)), Fraction(0))


def exact_paths(n,kind):
    """All possible sequences of ancestor jumps from the newest node to the root."""
    stack=[(n,[])]
    while stack:
        l,path=stack.pop()
        if l==1:
            yield path
        else:
            for j in range(1,window(l,kind)+1):
                stack.append((l-j,path+[(l,j)]))


def mean_variance(n,kind):
    means=[0.]*(n+1)
    vars_=[0.]*(n+1)
    for l in range(2,n+1):
        b=window(l,kind)
        means[l]=1+sum(means[l-j] for j in range(1,b+1))/b
        vars_[l]=sum(vars_[l-j]+(1+means[l-j]-means[l])**2 for j in range(1,b+1))/b
    return means[n],vars_[n]


def main():
    for kind in ('third','half','two_thirds'):
        for n in range(2,10):
            p=exact_depth_distribution(n,kind)
            q=independent_full_tree_enumeration(n,kind)
            check(p==q,f'finite distribution disagreement: {kind}, {n}')
            check(sum(p.values())==1,'probability normalization')
            mu=sum((t*x for t,x in p.items()),Fraction(0))
            check(mu <= potential(n,kind),'potential mean bound')
            a={l:Fraction(2,window(l,kind)+1) for l in range(2,n+1)}
            for path in exact_paths(n,kind):
                M=sum((a[l]*j-1 for l,j in path),Fraction(0))
                R=sum((sum((a[u]-a[l] for u in range(l-j+1,l+1)),Fraction(0)) for l,j in path),Fraction(0))
                check(R>=0,'correction positivity')
                check(potential(n,kind)==len(path)+M+R,'pathwise martingale identity')
        # Independent moment recursion at significantly larger sizes.
        n=3000
        m,v=mean_variance(n,kind)
        f=float(potential(n,kind))
        check(m<=f+1e-8,'mean bounded above by deterministic potential')
        check(f-m < 20*(1+log(n)),'logarithmic correction sanity check')
        check(0<v<f,'nondegenerate spread')
        print(f'{kind}: n={n}, F={f:.6f}, E(depth)={m:.6f}, Var(depth)={v:.6f}')
    print(f'PASS: {TESTS} exact finite checks / deterministic diagnostics')

if __name__=='__main__': main()
