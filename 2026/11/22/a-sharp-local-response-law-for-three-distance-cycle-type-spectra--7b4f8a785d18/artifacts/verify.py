"""Independent finite checks for the 3-distance cycle type-spectrum identities.

Usage: python3 artifacts/verify.py
Uses only Python's standard library.
"""
from collections import Counter
from itertools import product
from math import comb


def truncated_cycle(n):
    return [[min(abs(i-j), n-abs(i-j), 3) for j in range(n)] for i in range(n)]


def admissible(a, d):
    n = len(a)
    return all(abs(a[i]-a[j]) <= d[i][j] <= a[i]+a[j]
               for i in range(n) for j in range(i+1,n))


def direct_poly(d):
    n = len(d)
    out = Counter()
    for a in product((1,2,3), repeat=n):
        if admissible(a, d):
            out[(a.count(1),a.count(2),a.count(3))] += 1
    return +out


def polypow_linear(p, q, k):
    # (p + q)^k, variables p,q in {0,1,2}.
    out = Counter()
    for j in range(k+1):
        e=[0,0,0]
        e[p]+=j
        e[q]+=k-j
        out[tuple(e)] += comb(k,j)
    return out


def mul_monom(poly, exp, factor=1):
    return Counter({tuple(u+v for u,v in zip(k,exp)): val*factor
                    for k,val in poly.items()})


def add(*ps):
    z=Counter()
    for p in ps:z.update(p)
    return +z


def closed_formula(n):
    assert n>=7
    return add(polypow_linear(1,2,n),
               mul_monom(polypow_linear(1,2,n-3),(1,2,0),n),
               mul_monom(polypow_linear(1,2,n-4),(2,2,0),n),
               mul_monom(polypow_linear(1,2,n-5),(2,3,0),n),
               mul_monom(polypow_linear(1,2,n-5),(3,2,0),n))


def clique_formula(d):
    # Here d is a truncated unit-edge graph metric; its one-edges
    # define neighborhoods. Uses an independently constructed clique sum.
    n=len(d)
    out=Counter()
    for b in range(1<<n):
        S=[i for i in range(n) if b>>i&1]
        if any(d[i][j]==3 for i in S for j in S if i<j):
            continue
        N={j for i in S for j in range(n) if d[i][j]==1 and j not in S}
        out.update(mul_monom(polypow_linear(1,2,n-len(S)-len(N)),
                              (len(S),len(N),0)))
    return +out


def decrement_formula(n):
    assert n>=7
    # x^2 y^2 (x+y)^2 (y+z)^(n-6)
    out=Counter()
    for k in range(3):
        out.update(mul_monom(polypow_linear(1,2,n-6),
                              (2+k,4-k,0),comb(2,k)))
    if n==7:out[(3,4,0)]+=1
    return +out


def check_metric(d):
    n=len(d)
    return all(d[i][j] <= d[i][k]+d[k][j]
               for i in range(n) for j in range(n) for k in range(n))


def run():
    for n in range(4,12):
        d=truncated_cycle(n)
        assert check_metric(d)
        direct=direct_poly(d)
        assert direct==clique_formula(d), ('clique', n)
        if n>=7:
            assert direct==closed_formula(n), ('formula', n)
            assert sum(direct.values())==(n+4)*2**(n-2)
            e=[row[:] for row in d]
            e[0][3]=e[3][0]=2
            assert check_metric(e)
            after=direct_poly(e)
            delta=Counter(after)
            delta.subtract(direct)
            assert min(delta.values())>=0
            assert +delta==decrement_formula(n), ('decrement', n)
            assert sum(delta.values())==2**(n-4)+(1 if n==7 else 0)
            print(f'n={n}: types={sum(direct.values())}; decrease(0,3): +{sum(delta.values())} types')
        else:
            print(f'n={n}: types={sum(direct.values())}; boundary case')
    # Separate, exhaustive graph-family test against the general clique formula.
    cases=0
    for n in range(1,6):
        edges=[(i,j) for i in range(n) for j in range(i+1,n)]
        for b in range(1<<len(edges)):
            adj=[[] for _ in range(n)]
            for k,(i,j) in enumerate(edges):
                if b>>k&1:
                    adj[i].append(j);adj[j].append(i)
            dist=[[0 if i==j else 100 for j in range(n)] for i in range(n)]
            for i in range(n):
                dist[i][i]=0
                todo=[i]
                for v in todo:
                    for u in adj[v]:
                        if dist[i][u]>dist[i][v]+1:
                            dist[i][u]=dist[i][v]+1; todo.append(u)
            if any(dist[i][j]==100 for i in range(n) for j in range(n)):
                continue
            d=[[min(3,dist[i][j]) for j in range(n)] for i in range(n)]
            assert direct_poly(d)==clique_formula(d), ('general graph', n, b)
            cases+=1
    print('Exhaustive connected labelled graphs through 5 vertices:', cases)
    print('VERIFY_OK')

if __name__=='__main__':run()
