"""Standalone exact-rational checks for normalized symmetric Monge simplex metric extrema.

Runs only finite instances; the general theorem rests on the accompanying proof.
"""
from fractions import Fraction as Q
from itertools import combinations


def labels(n):
    return [('H', a, b) for a in range(1, n) for b in range(1, n-a+1)] + [('S', i) for i in range(1, n+1)]


def direct_matrix(n, v):
    x = [[Q(0) for _ in range(n)] for _ in range(n)]
    if v[0] == 'H':
        a, b = v[1:]
        for i in range(a):
            for j in range(n-b, n):
                x[i][j] = x[j][i] = Q(1, 2*a*b)
    else:
        i = v[1]-1
        for j in range(n):
            x[i][j] = x[j][i] = Q(1, 2*n)
        x[i][i] = Q(1, n)
    assert sum(map(sum,x)) == 1
    for i in range(n-1):
        for j in range(n-1):
            assert x[i][j]+x[i+1][j+1] <= x[i][j+1]+x[i+1][j]
    return x


def metric_formula(n, v, w):
    s=Q(n+1, 2*n*n)
    if v[0]=='S' and w[0]=='S':
        return Q(1,n)
    if v[0]=='H' and w[0]=='H':
        a,b=v[1:];c,d=w[1:]
        return Q(1,2*a*b)+Q(1,2*c*d)-Q(min(a,c)*min(b,d),a*b*c*d)
    if v[0]=='H':v,w=w,v
    i=v[1];a,b=w[1:]
    return s+Q(1,2*a*b)-Q(int(i<=a),n*a)-Q(int(i>n-b),n*b)


def full_min(n):
    if n<=4:return Q(2*n-1,2*n*n*(n-1))
    m=max((n-b-1)*b*(b+1) for b in range(1,n-1))
    return Q(1,2*m)


def min_pairs(n):
    if n<=4:
        return {frozenset((('H',1,n-1),('S',1))),frozenset((('H',n-1,1),('S',n)))}
    m=max((n-b-1)*b*(b+1) for b in range(1,n-1))
    aopts=[n-b-1 for b in range(1,n-1) if (n-b-1)*b*(b+1)==m]
    pairs=set()
    for a in aopts:
        pairs.add(frozenset((('H',a,n-a-1),('H',a,n-a))))
        pairs.add(frozenset((('H',n-a-1,a),('H',n-a,a))))
    return pairs


def max_pairs(n):
    if n==2:return {frozenset((('S',1),('S',2)))}
    return {frozenset((('H',1,1),('S',i))) for i in range(2,n)}


def run(nmax=12):
    for n in range(2,nmax+1):
        vv=labels(n)
        actual={v:direct_matrix(n,v) for v in vv}
        measured={}
        for v,w in combinations(vv,2):
            matv,matw=actual[v],actual[w]
            exact=sum((matv[i][j]-matw[i][j])**2 for i in range(n) for j in range(n))
            predicted=metric_formula(n,v,w)
            assert exact==predicted, ('metric',n,v,w,exact,predicted)
            measured[frozenset((v,w))]=exact
        minv=min(measured.values());maxv=max(measured.values())
        minset={p for p,d in measured.items() if d==minv}
        maxset={p for p,d in measured.items() if d==maxv}
        assert minv==full_min(n),(n,minv,full_min(n))
        assert minset==min_pairs(n),(n,'minimizers',minset^min_pairs(n))
        assert maxv==(Q(1,2) if n==2 else Q(1,2)+Q(n+1,2*n*n))
        assert maxset==max_pairs(n),(n,'maximizers',maxset^max_pairs(n))
        print(f'n={n}: vertices={len(vv)}, pairs={len(measured)}, min^2={minv} ({len(minset)}), max^2={maxv} ({len(maxset)}): PASS')
    print('SYMMETRIC_MONGE_EUCLIDEAN_EXTREMA_EXACT_PASS')

if __name__=='__main__':
    run()
