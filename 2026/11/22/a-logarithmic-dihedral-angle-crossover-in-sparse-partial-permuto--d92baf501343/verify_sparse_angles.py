"""Reproduce exact facet-incidence and dihedral-angle counts for sparse partial permutohedra.

Python 3 standard library only. It verifies finite cases; all-order statements
require the symbolic arguments in RESULT.md.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial, isclose, pi, acos, sqrt, log2


def facelist(m, n):
    facets = [("L", (i,)) for i in range(m)]
    facets += [("U", ss) for k in range(1, n) for ss in combinations(range(m), k)]
    facets += [("G", tuple(range(m)))]
    return facets


def vertices(m, n):
    yield (0,) * m
    for k in range(1, n + 1):
        values = tuple(range(n, n-k, -1))
        for places in permutations(range(m), k):
            x = [0] * m
            for i, v in zip(places, values):
                x[i] = v
            yield tuple(x)


def active_facets(x, facets, n):
    ans = []
    for i, (kind, idx) in enumerate(facets):
        if kind == 'L' and x[idx[0]] == 0:
            ans.append(i)
        elif kind == 'U':
            k = len(idx)
            if sum(x[j] for j in idx) == k*n-k*(k-1)//2:
                ans.append(i)
        elif kind == 'G' and sum(x) == n*(n+1)//2:
            ans.append(i)
    return ans


def predicted_pairs(facets, m, n):
    result = {}
    for i, (typ1, s) in enumerate(facets):
        for j in range(i+1, len(facets)):
            typ2, t = facets[j]
            if typ1 == typ2 == 'L':
                result[(i,j)] = ('right',0,1)
            elif typ1 == 'L' and typ2 == 'U' and s[0] not in t:
                result[(i,j)] = ('right',0,1)
            elif typ1 == 'L' and typ2 == 'G':
                result[(i,j)] = ('acute',1,m)
            elif typ1 == 'U' and typ2 == 'U' and set(s)<set(t):
                result[(i,j)] = ('obtuse',len(s),len(t))
            elif typ1 == 'U' and typ2 == 'G':
                result[(i,j)] = ('obtuse',len(s),m)
    return result


def theoretical_counts(m, n):
    right = comb(m,2)+sum((m-k)*comb(m,k) for k in range(1,n))
    obtuse = sum(comb(m,t)*(2**t-2) for t in range(2,n)) \
          + sum(comb(m,s) for s in range(1,n))
    acute = m
    return {'right':right,'obtuse':obtuse,'acute':acute}


def exact_normal_dot_angle(facets, i, j, m):
    """Derive cos(outward angle) by integer dot and norm squared."""
    def normal(f):
        typ,ss=f
        if typ == 'L':
            a=[0]*m; a[ss[0]]=-1; return a
        a=[0]*m
        for t in ss: a[t]=1
        return a
    a=normal(facets[i]); b=normal(facets[j])
    dot=sum(u*v for u,v in zip(a,b))
    aa=sum(u*u for u in a); bb=sum(v*v for v in b)
    if dot==0: return ('right',0,1)
    if dot<0: return ('acute',dot*dot,aa*bb)
    return ('obtuse',dot*dot,aa*bb)


def check(m,n):
    facets = facelist(m,n)
    predicted = predicted_pairs(facets,m,n)
    hits = set()
    total_vertices=0
    for vertex in vertices(m,n):
        active=active_facets(vertex,facets,n)
        assert len(active)==m, (m,n,vertex,active)
        total_vertices+=1
        for pair in combinations(active,2): hits.add(pair)
    assert total_vertices == sum(comb(m,k)*factorial(k) for k in range(n+1))
    assert hits==set(predicted), (m,n,'missing',len(set(predicted)-hits),'extras',len(hits-set(predicted)))
    for (i,j), (typ,a,b) in predicted.items():
        typ2,a2,b2=exact_normal_dot_angle(facets,i,j,m)
        assert typ==typ2 and a*b2==a2*b,(m,n,i,j,typ,a,b,typ2,a2,b2)
    counts=dict(Counter(t for t,_,_ in predicted.values()))
    assert counts==theoretical_counts(m,n), (m,n,counts,theoretical_counts(m,n))
    return total_vertices,len(facets),len(hits),counts


def exact_ratio(m,n):
    c=theoretical_counts(m,n)
    return c['obtuse']/c['right'], 2**(n-1)/m

if __name__=='__main__':
    total_v=total_r=cases=0
    for m in range(4,9):
        for n in range(2,min(m-2,5)+1):
            v,f,r,c=check(m,n)
            total_v+=v; total_r+=r; cases+=1
            print(f'case m={m} n={n} vertices={v} facets={f} ridges={r} acute={c["acute"]} right={c["right"]} obtuse={c["obtuse"]}')
    print('RATIO checks (exact enumeration-free formulas):')
    for m in [256,1024,4096]:
        for delta in [-2,0,2]:
            n=int(log2(m))+delta
            ratio,heur=exact_ratio(m,n)
            print(f'm={m} n={n} observed_O_over_R={ratio:.9g} predicted_2pow_over_m={heur:.9g}')
    print(f'SPARSE_RIDGE_ANGLE_PASS cases={cases} vertices_tested={total_v} ridges_tested={total_r}')
