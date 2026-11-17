"""Exact finite corroboration of vertex-shell formulas for edge-diamond sums of bistars.
Run: python3 verify.py (standard Python 3, no third-party packages)."""
from collections import Counter
from itertools import product
from math import comb

checks = 0

def checked(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def edges(p, q):
    return [(0, i) for i in range(2, p + 2)] + [(1, j) for j in range(p + 2, p + q + 2)] + [(0, 1)]


def predicted(p, q):
    F = Counter()
    for t in range(p + 1):
        for s in range(q + 1):
            for bridge_left in (0, 1):
                a, b = t + bridge_left, s + 1 - bridge_left
                r2 = p + q - t - s + a*a + b*b
                occupied = p + q - t - s + (a > 0) + (b > 0)
                F[r2] += comb(p, t)*comb(q, s)*2**occupied
    return F


def independent_vertices(p, q):
    E = edges(p, q)
    n = p + q + 2
    V = set()
    for choices in product((0, 1), repeat=len(E)):
        indegree = [0]*n
        for (a,b),v in zip(E, choices):
            indegree[b if v else a] += 1
        occupied = [i for i in range(n) if indegree[i]]
        for signs in product((-1,1), repeat=len(occupied)):
            vec = [0]*n
            for i,sgn in zip(occupied,signs): vec[i] = sgn*indegree[i]
            V.add(tuple(vec))
    return V


def endpoint_sums(p, q):
    E = edges(p, q)
    n = p + q + 2
    S = set()
    for selection in product(range(4),repeat=len(E)):
        x=[0]*n
        for (a,b),w in zip(E,selection):
            x[a if w<2 else b] += 1 if w%2==0 else -1
        S.add(tuple(x))
    return S

for p in range(1,4):
    for q in range(1,4):
        V = independent_vertices(p,q)
        F = predicted(p,q)
        actual = Counter(sum(t*t for t in x) for x in V)
        checked(actual == F, 'radial spectrum disagrees for %s' % ((p,q),))
        checked(sum(F.values()) == 8*3**(p+q)-2**(q+1)*3**p-2**(p+1)*3**q, 'vertex count')
        R2=p*p+q*q+2*max(p,q)+1
        checked(max(actual)==R2,'outer radius')
        if p==q==1: C=16
        elif p==q or min(p,q)==1: C=8
        else: C=4
        checked(actual[R2]==C,'outer contacts')
        E = edges(p,q)
        # Check by a second construction: every signed endpoint selection is in the ball,
        # and its outer-sphere points are precisely the predicted contact vertices.
        S=endpoint_sums(p,q)
        maxsum=max(sum(v*v for v in x) for x in S)
        checked(maxsum==R2, 'endpoint-sum radius')
        shell={x for x in S if sum(v*v for v in x)==R2}
        checked(shell=={x for x in V if sum(v*v for v in x)==R2}, 'endpoint-sum contacts')
        checked(V.issubset(S), 'candidate not an endpoint sum')
        # Explicit generic integer gradient exposes each candidate signed-indegree vector.
        # Every orientation of a tree has a strict topological ranking.
        n=p+q+2
        for orient in product((0,1),repeat=len(E)):
            indeg=[0]*n
            directed=[]
            for (a,b),bit in zip(E,orient):
                tail,head=(a,b) if bit else (b,a)
                directed.append((tail,head));indeg[head]+=1
            rank=[0]*n
            remain=set(range(n))
            for k in range(n):
                available=sorted(v for v in remain if all(y!=v or x not in remain for x,y in directed))
                checked(bool(available),'directed tree cyclic?')
                z=available[0];rank[z]=k+1;remain.remove(z)
            checked(all(rank[a]<rank[b] for a,b in directed),'bad topological ranking')
            # One vertex for each independently signed nonzero-coordinate pattern.
            # Its dot product with its exposing gradient equals the full support sum.
            expected_support=sum(max(rank[a],rank[b]) for a,b in E)
            x=[0]*n
            for head in [b for a,b in directed]:x[head]+=1
            checked(sum(rank[i]*x[i] for i in range(n))==expected_support,'support mismatch')
        print('p=%d q=%d: vertices=%d, radius^2=%d, contacts=%d, endpoint_sums=%d' % (p,q,len(V),R2,C,len(S)))

print('OK: %d exact assertions over 9 bistar instances' % checks)
