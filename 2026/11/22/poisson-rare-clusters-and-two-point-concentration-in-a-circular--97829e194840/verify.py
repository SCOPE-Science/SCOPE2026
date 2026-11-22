#!/usr/bin/env python3
"""Independent finite enumerations and symbolic identities for circular nearest-neighbor component extremes.
No finite enumeration is used as a substitute for the asymptotic probabilistic proof.
"""
import itertools
from fractions import Fraction
from math import factorial

checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def p(k):
    return Fraction((k - 1) * (k + 2) * (2 ** k), factorial(k + 3))

def q(k):
    return Fraction(k * (2 ** k), factorial(k + 2))

def peak_indices(gaps):
    n = len(gaps)
    return [i for i in range(n) if gaps[i] > gaps[(i-1)%n] and gaps[i] > gaps[(i+1)%n]]

def component_sizes(gaps):
    n = len(gaps)
    peaks = peak_indices(gaps)
    check(len(peaks) >= 1, 'a cyclic sequence must have a local maximum')
    return [(peaks[(j+1)%len(peaks)]-peaks[j])%n or n for j in range(len(peaks))]

def direct_nearest_edges(gaps):
    n = len(gaps)
    s = sum(gaps)
    positions = [Fraction(0,1)]
    for gap in gaps[:-1]:
        positions.append(positions[-1] + Fraction(gap,s))
    edges=set()
    for i in range(n):
        dst=[]
        for j in range(n):
            if i!=j:
                d=abs(positions[i]-positions[j]); dst.append((min(d,1-d),j))
        best=min(dst)[1]
        edges.add(frozenset((i,best)))
    return edges

# Historical one-gap distribution, used as an input rather than credited as new.
for k in range(2,27):
    check(p(k) == q(k)-q(k+1), 'finite difference identity')
    check(q(k+1)/q(k) == Fraction(2*(k+1), k*(k+3)), 'tail ratio')
    check(Fraction(2**(k-2),factorial(k-1))/q(k) == Fraction((k+1)*(k+2),4), 'overlap-bound ratio')
    integral = sum((Fraction(1,k+1) - (Fraction(1,j+1)+Fraction(1,k-j+1))/Fraction(k+2,1) + Fraction(1,(j+1)*(k-j+1)*(k+3))) / factorial(j) / factorial(k-j) for j in range(1,k))
    check(integral == p(k), 'valley integral enumeration')

# Count no-local-maximum permutations, an input to the two-block bound.
for L in range(2,9):
    no_peak_count=sum(all(not(a[i-1]<a[i]>a[i+1]) for i in range(1,L-1)) for a in itertools.permutations(range(L)))
    check(no_peak_count == 2**(L-1), 'valley permutation count')

# Exhaust all cyclic gap rankings, which are equiprobable under Dirichlet spacings.
for n in range(5,9):
    count_large={k:0 for k in range(2,n-1)}
    count_equal={k:0 for k in range(2,n-2)}
    total=0
    for g in itertools.permutations(range(1,n+1)):
        sizes=component_sizes(g)
        total += 1
        check(sum(sizes)==n and all(x>=2 for x in sizes), 'component partition')
        peaks=peak_indices(g)
        check(len(peaks)==len(sizes), 'one cut per component')
        if n<=7:
            edges = direct_nearest_edges(g)
            predicted={frozenset((i,(i+1)%n)) for i in range(n) if i not in peaks}
            check(edges == predicted,'metric nearest-neighbor graph equals local-max cuts')
        for k in count_large:
            w=sum(x>=k for x in sizes)
            a=sum(g[i]>g[(i-1)%n] and g[i]>g[(i+1)%n] and all(not(g[(i+j)%n]>g[(i+j-1)%n] and g[(i+j)%n]>g[(i+j+1)%n]) for j in range(1,k)) for i in range(n))
            check(w==a,'locally defined rare-event count equals component count')
            count_large[k] += w
        for k in count_equal:
            count_equal[k] += sizes.count(k)
    for k,v in count_large.items():
        check(Fraction(v,total) == n*q(k), 'exact rare-event first moment')
    for k,v in count_equal.items():
        check(Fraction(v,total) == n*p(k), 'exact fixed-size first moment')
    print(f'n={n}; enumerated={total}; exact moment identities passed')

# Upper- and lower-tail estimates for the two-point concentration theorem
for n in [1000,10000,100000,1000000,10**9]:
    b=2
    while n*q(b+1)>=Fraction.from_float((b+1)**0.5):
        b+=1
    check(n*q(b)>=Fraction.from_float(b**0.5), 'lower b inequality')
    check(n*q(b+1)<Fraction.from_float((b+1)**0.5),'upper b inequality')
    check(n*q(b+2)<Fraction(3,1)*Fraction.from_float(1/(b**0.5)), 'two-point upper Markov bound')
    print(f'n={n}; two-point base={b}; n q(b)={float(n*q(b)):.6g}; n q(b+1)={float(n*q(b+1)):.6g}')

print(f'PASS: {checks} exact or controlled assertions')
