"""Direct finite checks for alternating cycles in compositions of retractions.
Only Python's standard library is used. Run: python verify_cycles.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial


def idempotents(n):
    vertices = tuple(range(n))
    for k in range(1, n+1):
        for root_tuple in combinations(vertices, k):
            roots = set(root_tuple)
            rest = [i for i in vertices if i not in roots]
            for choices in product(root_tuple, repeat=len(rest)):
                a = list(vertices)
                for x in root_tuple: a[x] = x
                for x,y in zip(rest, choices): a[x] = y
                yield (tuple(a), frozenset(roots))


def actual_cycles(f, g, roots_f, roots_g):
    n = len(f)
    composition = tuple(f[g[x]] for x in range(n))
    seen = set()
    cycles = defaultdict(int)
    periodic = set()
    for x in range(n):
        if x in seen: continue
        order = []
        loc = {}
        v = x
        while v not in seen and v not in loc:
            loc[v] = len(order)
            order.append(v)
            v = composition[v]
        if v in loc:
            cyc = order[loc[v]:]
            for y in cyc: periodic.add(y)
            if not (len(cyc) == 1 and cyc[0] in roots_f & roots_g):
                assert all(y in roots_f - roots_g for y in cyc)
                assert all(g[y] in roots_g - roots_f for y in cyc)
                cycles[len(cyc)] += 1
        seen.update(order)
    assert periodic & roots_f & roots_g == roots_f & roots_g
    return cycles


def fall(x,r):
    if r > x: return 0
    ans=1
    for j in range(r): ans*=x-j
    return ans


def moment(frequencies, exponents):
    out=1
    for r,t in exponents:
        out*=fall(frequencies.get(r,0),t)
    return out


def exact_moment(k,l,h,exponents):
    a,b=k-h,l-h
    R=sum(r*t for r,t in exponents)
    value=Fraction(fall(a,R)*fall(b,R),(k*l)**R)
    for r,t in exponents: value/=r**t
    return value


def test_exhaustive(max_n=5):
    checks=0
    specs = [((1,1),), ((1,2),), ((2,1),), ((3,1),),
             ((1,1),(2,1)), ((1,3),), ((2,2),)]
    for n in range(1,max_n+1):
        maps=list(idempotents(n))
        aggregates=defaultdict(lambda: [0]+[0]*len(specs))
        for f,F in maps:
            for g,G in maps:
                k,l,h=len(F),len(G),len(F&G)
                cycles=actual_cycles(f,g,F,G)
                row=aggregates[(k,l,h)]
                row[0]+=1
                for j,spec in enumerate(specs,1): row[j]+=moment(cycles,spec)
                checks+=1
        for (k,l,h),row in aggregates.items():
            for j,spec in enumerate(specs,1):
                calc=Fraction(row[j],row[0]); expect=exact_moment(k,l,h,spec)
                assert calc==expect,(n,(k,l,h),spec,calc,expect)
                checks+=1
        print('n',n,'idempotents',len(maps),'ordered pairs',len(maps)**2,
              'strata',len(aggregates))
    print('PASS:', checks,'exact comparisons')

if __name__=='__main__': test_exhaustive()
