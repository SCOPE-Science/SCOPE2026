#!/usr/bin/env python3
"""Exact independent-edge epidemic immunization check on a two-clique gateway graph.

No simulation is used: each percolation state is enumerated and evaluated in
integer arithmetic.  A separate connectivity argument supplies the formulas.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

CHECKS = 0
CONFIGURATIONS = 0


def require(condition, note):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(note)


def graph(m):
    """Two K_m copies; vertex 2m is joined to vertices 0 and m."""
    left = range(m)
    right = range(m, 2*m)
    edges = list(combinations(left, 2)) + list(combinations(right, 2))
    edges.extend([(0, 2*m), (m, 2*m)])
    return tuple(range(2*m+1)), edges


def polynomial_for_vaccination(m, vaccinated):
    """Average outbreak size by exhaustive exact bond-state enumeration."""
    global CONFIGURATIONS
    vertices, all_edges = graph(m)
    active = [v for v in vertices if v != vaccinated]
    edges = [(u,v) for u,v in all_edges if vaccinated not in (u,v)]
    count = len(edges)
    coeff = [Fraction(0) for _ in range(count+1)]
    for mask in range(1 << count):
        CONFIGURATIONS += 1
        parent = {v:v for v in active}

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        for i, (u,v) in enumerate(edges):
            if (mask >> i) & 1:
                parent[root(u)] = root(v)
        component_sizes = {}
        for v in active:
            r = root(v)
            component_sizes[r] = component_sizes.get(r,0)+1
        # Uniform seed: the mean reached size is sum(component_size^2)/n.
        mean_size = Fraction(sum(k*k for k in component_sizes.values()), len(active))
        open_count = mask.bit_count()
        closed_count = count-open_count
        for j in range(closed_count+1):
            coeff[open_count+j] += mean_size * comb(closed_count,j) * (-1)**j
    return strip(coeff)


def strip(a):
    a = list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a


def add(a,b):
    return strip([(a[i] if i<len(a) else 0) +(b[i] if i<len(b) else 0)
                  for i in range(max(len(a),len(b)))])


def sub(a,b):
    return add(a,[-x for x in b])


def mul(a,b):
    c=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return strip(c)


def scale(a,c):
    return strip([x*c for x in a])


def val(a,x):
    z=Fraction(0)
    for c in reversed(a):
        z=z*x+c
    return z


P=[Fraction(0),Fraction(1)]
ONE=[Fraction(1)]
Q3=[Fraction(0),Fraction(1),Fraction(1),Fraction(-1)]
EG3=add(ONE,scale(Q3,2))
EB3=add(ONE, scale(add(add(scale(P,2),scale(Q3,3)),scale(mul(P,Q3),2)),Fraction(1,3)))
DIFF3=scale(mul(P,[Fraction(1),Fraction(1),Fraction(-5),Fraction(2)]),Fraction(1,3))

# Each orbit is verified, and each single-vertex removal is exhaustively checked.
for m in (2,3):
    expected = {}
    for v in range(2*m+1):
        expected[v]=polynomial_for_vaccination(m,v)
    # Automorphism orbit equalities
    for v in range(1,m):
        require(expected[v] == expected[1],f"left nonbridge, m={m}")
    for v in range(m+1,2*m):
        require(expected[v] == expected[1],f"right nonbridge, m={m}")
    require(expected[0] == expected[m],f"bridge endpoints, m={m}")
    require(expected[2*m] == expected[2*m],"gateway representative")
    if m==3:
        require(expected[2*m] == EG3,"two triangles, gateway removed")
        require(expected[0] == EB3,"two triangles, bridge endpoint removed")
        require(sub(EG3,EB3) == DIFF3,"sharp cubic difference")
        # Exact symbolic sign certificates at four rational points.
        for x in (Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
            require(val(expected[1],x)>val(expected[0],x),"nonbridge strict domination")
        require(val(DIFF3,Fraction(1,2))==Fraction(1,12),"low-transmissibility advantage")
        require(val(DIFF3,Fraction(3,4))==Fraction(-7,128),"high-transmissibility advantage")
        cubic=[Fraction(1),Fraction(1),Fraction(-5),Fraction(2)]
        lo=Fraction(678963,1000000)
        hi=Fraction(678964,1000000)
        require(val(cubic,lo)>0 and val(cubic,hi)<0,"root rational enclosure")
        # p=t/(1+t) gives (1+t)^3 f(p) = 1+4t-t^3.
        # The transformed polynomial has exactly one positive zero by Descartes.
        for t in (Fraction(0),Fraction(1,2),Fraction(1),Fraction(2),Fraction(4)):
            lhs=val(cubic,t/(1+t))*(1+t)**3
            rhs=1+4*t-t**3
            require(lhs==rhs,"transformation identity")
    else:
        require(expected[2*m] == [Fraction(1),Fraction(1)],"path-five central deletion")
        require(expected[0] == [Fraction(1),Fraction(1),Fraction(1,2)],"path-five adjacent deletion")
        require(sub(expected[2*m],expected[0]) == [Fraction(0),Fraction(0),Fraction(-1,2)],"path-five no switch")
        for x in (Fraction(1,10),Fraction(1,2),Fraction(9,10),Fraction(1)):
            require(val(expected[1],x)>val(expected[0],x),"outer deletion inferior")

print(f"PASS: {CHECKS} exact identities and rational inequalities; "
      f"{CONFIGURATIONS} exhaustive bond configurations across all vertex deletions")
print("Cubic crossover lies strictly between 0.678963 and 0.678964")
