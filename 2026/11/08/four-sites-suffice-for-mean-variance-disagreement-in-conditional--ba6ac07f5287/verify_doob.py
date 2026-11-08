"""Independent rational Doob-transform check for the four-site witness.
Only Python's standard library is required. Configurations are frozensets,
not bit masks. Time includes ineffective updates.
"""
from fractions import Fraction as F
from itertools import combinations


def solve(A, b):
    n=len(A)
    rows=[[F(x) for x in A[i]] + [F(b[i])] for i in range(n)]
    for k in range(n):
        j=next(j for j in range(k,n) if rows[j][k])
        rows[k],rows[j]=rows[j],rows[k]
        pivot=rows[k][k]
        rows[k]=[x/pivot for x in rows[k]]
        for i in range(n):
            if i!=k and rows[i][k]:
                c=rows[i][k]
                rows[i]=[rows[i][t]-c*rows[k][t] for t in range(n+1)]
    return [row[-1] for row in rows]


def build():
    v=range(4); whole=frozenset(v)
    edges={(0,1),(0,2),(0,3),(1,2),(2,3)}
    nb={i:set() for i in v}
    for x,y in edges: nb[x].add(y);nb[y].add(x)
    S=[frozenset(c) for k in range(1,4) for c in combinations(v,k)]
    ix={st:i for i,st in enumerate(S)}
    Q=[[F(0) for _ in S] for _ in S]
    b=[F(0) for _ in S]
    for i,st in enumerate(S):
        total=5*len(st)+(4-len(st))
        for x in v:
            prob=F(5 if x in st else 1,total*len(nb[x]))
            for y in nb[x]:
                if (x in st) == (y in st): new=st
                elif x in st: new=st|{y}
                else: new=st-{y}
                if new==whole: b[i]+=prob
                elif new: Q[i][ix[new]]+=prob
    return S,Q,b


def check():
    S,Q,b=build(); n=len(S)
    A=[[F(i==j)-Q[i][j] for j in range(n)] for i in range(n)]
    h=solve(A,b)
    assert all(0<v<1 for v in h)
    conditioned=[[Q[i][j]*h[j]/h[i] for j in range(n)] for i in range(n)]
    B=[[F(i==j)-conditioned[i][j] for j in range(n)] for i in range(n)]
    means=solve(B,[F(1) for _ in S])
    second=solve(B,[2*means[i]-1 for i in range(n)])
    variances=[second[i]-means[i]**2 for i in range(n)]
    for v in range(4):
        i=S.index(frozenset([v]))
        if v in (0,2):
            expected=(F(1122875,1488426),F(72659908801,8913687172),F(1954046189090893922205,79453819000277357584))
        else:
            expected=(F(422375,496142),F(6854218276,838231909),F(136482613376588448261,5621061866126274248))
        assert (h[i],means[i],variances[i]) == expected
    a=S.index(frozenset([0])); c=S.index(frozenset([1]))
    assert means[a]<means[c] and variances[a]>variances[c]
    print('PASS: exact conditional Doob chain, all four singleton seeds.')

if __name__=='__main__': check()
