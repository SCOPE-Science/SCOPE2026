#!/usr/bin/env python3
"""Independent small-parameter verification of a graph-conditioned 3-nilpotent semigroup census.
Only standard-library modules are used.
"""
from itertools import permutations, product, combinations
from math import gcd, factorial

def all_pairs(n):
    return [(a,b) for a in range(n) for b in range(a,n)]

def is_star_free(n, edges):
    return all(any(frozenset((u,v)) not in edges for v in range(n) if v != u)
               for u in range(n))

def auts(n, edges):
    return [p for p in permutations(range(n)) if all(
        (frozenset((i,j)) in edges) == (frozenset((p[i],p[j])) in edges)
        for i in range(n) for j in range(i+1,n))]

def cycles(p):
    seen=set(); out=[]
    for i in range(len(p)):
        if i in seen: continue
        cur=[]; j=i
        while j not in seen:
            seen.add(j); cur.append(j); j=p[j]
        out.append(cur)
    return out

def admissible(p, edges):
    return all(frozenset((cyc[i],cyc[(i+len(cyc)//2)%len(cyc)])) in edges
               for cyc in cycles(p) if len(cyc)%2 == 0 for i in range(len(cyc)//2))

def pair_orbits(p):
    n=len(p); pairs={frozenset((i,j)) for i in range(n) for j in range(i+1,n)}
    num=0
    while pairs:
        e=pairs.pop(); orbit={e}; frontier=[e]
        while frontier:
            t=frontier.pop()
            q=frozenset(p[v] for v in t)
            if q not in orbit: orbit.add(q); frontier.append(q)
        pairs -= orbit
        num+=1
    return num

def p_orbit_formula(p):
    ls=[len(c) for c in cycles(p)]
    return sum(k//2 for k in ls)+sum(gcd(x,y) for i,x in enumerate(ls) for y in ls[i+1:])

def formula(n, edges):
    group=auts(n,edges)
    val=0
    for perm in group:
        assert pair_orbits(perm)==p_orbit_formula(perm)
        if admissible(perm,edges):
            val += 2**(len(cycles(perm))+p_orbit_formula(perm))
    assert val%len(group)==0
    return val//len(group)

def table_from_bits(n,edges,bits):
    # upper-triangle bits: diagonal and one binary choice per unordered pair.
    a=[[0]*n for _ in range(n)]
    for (i,j),t in zip(all_pairs(n),bits):
        a[i][j]=t
        if i==j:continue
        a[j][i]=t if frozenset((i,j)) in edges else 1-t
    return tuple(tuple(row) for row in a)

def transform(table,p):
    n=len(table)
    return tuple(tuple(table[p[i]][p[j]] for j in range(n)) for i in range(n))

def brute(n,edges):
    group=auts(n,edges)
    distinct=set()
    k=len(all_pairs(n))
    for bits in product((0,1),repeat=k):
        table=table_from_bits(n,edges,bits)
        assert any(table[i][j] for i in range(n) for j in range(n))
        for i in range(n):
            for j in range(i+1,n):
                assert (table[i][j]==table[j][i])==(frozenset((i,j)) in edges)
        distinct.add(min(transform(table,p) for p in group))
    return len(distinct)

def check():
    checks=0
    for n in (2,3,4):
        all_edges=[frozenset((i,j)) for i in range(n) for j in range(i+1,n)]
        for mask in range(1<<len(all_edges)):
            edges={x for i,x in enumerate(all_edges) if mask>>i&1}
            if not is_star_free(n,edges):continue
            f=formula(n,edges); b=brute(n,edges)
            assert f==b,(n,mask,f,b)
            checks += 1
    values=[]
    for n in range(2,7):
        assert formula(n,set())>0
        values.append((n,formula(n,set())))
    assert values==[(2,4),(3,12),(4,48),(5,296),(6,3040)]
    cycle4={frozenset((i,(i+1)%4)) for i in range(4)}
    matching4={frozenset((0,1)),frozenset((2,3))}
    cycle5={frozenset((i,(i+1)%5)) for i in range(5)}
    assert (formula(4,cycle4),formula(4,matching4),formula(5,cycle5))==(144,170,3280)
    assert brute(5,cycle5)==3280
    print('PASS: exhaustive labeled graph/orbit checks for n=2..4; graphs:',checks)
    print('PASS: edgeless graph isomorphism-class counts',values)
    print('GRAPH_CONDITIONED_NILPOTENT_SEMIGROUP_FIBERS_VERIFIED')

if __name__=='__main__':check()
