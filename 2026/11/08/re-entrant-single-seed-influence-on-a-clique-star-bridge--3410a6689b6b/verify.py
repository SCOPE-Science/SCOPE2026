#!/usr/bin/env python3
"""Exact reproducible checks for re-entrant one-seed reach on a star--clique bridge.

Requires Python 3 standard library only. All polynomial coefficients and sampled
values are computed exactly; finite checks corroborate the separate general proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def powpoly(a, k):
    x = [1]
    for _ in range(k):
        x = mul(x, a)
    return x


def evaluate(a, p):
    v = 0
    for x in a[::-1]:
        v = v * p + x
    return v


def reachable_size(n, edges, mask, s):
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if mask & (1 << i):
            adj[u].append(v)
            adj[v].append(u)
    seen = {s}
    queue = [s]
    for u in queue:
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen)


def enumerate_influence(n, edges):
    """Exact coefficient vector of E(component size) for every possible seed."""
    e = len(edges)
    basis = [mul([0] * k + [1], powpoly([1, -1], e-k))
             for k in range(e+1)]
    counts = [[0] * (e+1) for _ in range(n)]
    for mask in range(1 << e):
        k = mask.bit_count()
        for s in range(n):
            counts[s][k] += reachable_size(n, edges, mask, s)
    output = []
    for s in range(n):
        ans = [0]
        for k in range(e+1):
            ans = add(ans, [counts[s][k]*x for x in basis[k]])
        output.append(ans)
    return output


def clique_reliability_polynomial(q):
    """Exact terminal-to-terminal connection probability on K_q, by edge subsets."""
    edges = list(combinations(range(q), 2))
    e = len(edges)
    by_edges = [0]*(e+1)
    for mask in range(1 << e):
        adj = [[] for _ in range(q)]
        for i,(u,v) in enumerate(edges):
            if mask & (1 << i):
                adj[u].append(v);adj[v].append(u)
        seen={0}; queue=[0]
        for u in queue:
            for v in adj[u]:
                if v not in seen:
                    seen.add(v);queue.append(v)
        if 1 in seen:
            by_edges[mask.bit_count()] += 1
    out=[0]
    for k,count in enumerate(by_edges):
        out=add(out,[count*x for x in mul([0]*k+[1],powpoly([1,-1],e-k))])
    return out


def expect_clique(q,p):
    """Independent recurrence for component size in G(q,p)."""
    connected=[F(0)]*(q+1)
    connected[1]=F(1)
    for m in range(2,q+1):
        connected[m]=1-sum(comb(m-1,j-1)*connected[j]
                            *(1-p)**(j*(m-j)) for j in range(1,m))
    return sum(s*comb(q-1,s-1)*connected[s]
               *(1-p)**(s*(q-s)) for s in range(1,q+1))


def main():
    checks=0
    r4=clique_reliability_polynomial(4)
    assert r4 == [0,1,2,0,-7,7,-2]
    checks += 1
    f4=[1,-6,0,21,-21,6]
    assert add([4],[-3*x for x in r4[1:]]) == f4
    checks += 1
    # Transform f(p) to (1+t)^5 f(t/(1+t)); Descartes gives <=2 roots.
    transform=[0]*6
    for j,a in enumerate(f4):
        for k in range(6-j):
            transform[j+k]+=a*comb(5-j,k)
    assert transform == [1,-1,-14,-5,2,1]
    assert [1 if evaluate(f4,F(i,2))>0 else -1 for i in (0,1,2)] == [1,-1,1]
    checks += 2
    for low,high in [(F(184,1000),F(185,1000)),(F(709,1000),F(710,1000))]:
        assert evaluate(f4,low)*evaluate(f4,high)<0
        checks += 1
    # A star with 4 leaves has center 0, clique vertices 5,...,8, bridge (0,5).
    q=4
    n=2*q+1
    star=[(0,j) for j in range(1,q+1)]
    clique=list(combinations(range(q+1,2*q+1),2))
    edges=star+[(0,q+1)]+clique
    assert len(edges)==11
    influences=enumerate_influence(n,edges)
    hub=[1,q,0,0,0,0,0,0,0,0,0,0]
    clique_expected=add([1],[(q-1)*x for x in r4])
    # E_0=1+4p+p*C_4; E_5=C_4+p(1+4p).
    expected_hub=add([1,4],mul([0,1],clique_expected))
    expected_bridge=add(clique_expected,[0,1,4])
    assert influences[0] == expected_hub
    assert influences[q+1] == expected_bridge
    checks += 2
    assert add(expected_hub,[-x for x in expected_bridge])==mul([0,1,-1],f4)
    checks += 1
    # Independent full-graph enumeration confirms global seed optimality in three regimes.
    for p,winning in [(F(1,10),0),(F(1,2),q+1),(F(9,10),0)]:
        vals=[evaluate(c,p) for c in influences]
        assert vals[winning]>max(v for i,v in enumerate(vals) if i!=winning)
        checks += n
    for p in [F(1,11),F(1,4),F(1,2),F(3,4),F(9,10)]:
        assert expect_clique(4,p)==evaluate(clique_expected,p)
        checks += 1
    # All-size proof uses the independent two-hop lower bound at p=1/2.
    for q in range(4,25):
        lower=F(2,1)-F(3,4)**(q-2)
        assert lower>F(q,q-1)
        checks += 1
    for q in (4,5,6,7,8,9):
        C=expect_clique(q,F(1,2))
        assert C>1+F(q,2)
        checks += 1
    # This independent recurrence is not finite proof of the general claim.
    print(f"PASS: {checks} exact identities and global-seed checks; q=4 edge-subset enumeration uses 2^11 configurations.")
    print("R4(p) = p + 2p^2 - 7p^4 + 7p^5 - 2p^6")
    print("f4(p) = 1 - 6p + 21p^3 - 21p^4 + 6p^5")
    print("q4 thresholds bracketed by (0.184,0.185) and (0.709,0.710).")

if __name__ == '__main__':
    main()
