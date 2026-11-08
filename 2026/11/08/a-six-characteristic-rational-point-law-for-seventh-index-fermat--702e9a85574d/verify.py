"""Exact certificate for four-summand seventh-root Fermat surface counts.

Pure Python 3, no external dependencies; run as `python verify.py`.
"""
from itertools import combinations_with_replacement, product
from collections import Counter

K = 7
PHI = [1] * 7


def bareiss_determinant(rows):
    n = len(rows)
    a = [list(row) for row in rows]
    sign = 1
    denom = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            i = next((j for j in range(k+1,n) if a[j][k]),None)
            if i is None:
                return 0
            a[k],a[i]=a[i],a[k]
            sign=-sign
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*piv-a[i][k]*a[k][j]
                assert z % denom == 0
                a[i][j] = z//denom
            a[i][k]=0
        denom=piv
    return sign*a[-1][-1]


def reduce_z7(poly):
    a=list(poly)
    if len(a)<7:
        a.extend([0]*(7-len(a)))
    for i in range(len(a)-1,5,-1):
        v=a[i]
        if v:
            for j in range(7):
                a[i-6+j]-=v
        a[i]=0
    return a[:6]


def norm_of_sum(indices):
    coeff=[indices.count(j) for j in range(7)]
    cols=[]
    for j in range(6):
        cols.append(reduce_z7([0]*j+coeff))
    rows=[[cols[j][i] for j in range(6)] for i in range(6)]
    return abs(bareiss_determinant(rows))


def poly_remainder_mod(poly, divisor, p):
    f=[v%p for v in poly]
    while len(f)>len(divisor)-1:
        coeff=f[-1]*pow(divisor[-1],-1,p)%p
        for j in range(len(divisor)):
            f[len(f)-len(divisor)+j]=(f[len(f)-len(divisor)+j]-coeff*divisor[j])%p
        while f and f[-1]==0:
            f.pop()
    return tuple(f+[0]*(len(divisor)-1-len(f)))


def zero_at_root(indices,p):
    if p==2:
        return all(x==0 for x in poly_remainder_mod([indices.count(i) for i in range(7)], [1,1,0,1],2))
    if p==3:
        return all(x==0 for x in poly_remainder_mod([indices.count(i) for i in range(7)],[1]*7,3))
    roots={29:7,43:4,71:20,547:9}
    return sum(pow(roots[p],i,p) for i in indices)%p==0


def run():
    norm_counts=Counter(norm_of_sum(idx) for n in range(1,5)
                        for idx in combinations_with_replacement(range(7),n))
    assert norm_counts=={1:91,8:28,29:42,43:42,64:28,71:42,547:42,729:7,4096:7},norm_counts
    expected={2:[0,7,42,301],3:[0,0,7,0],29:[0,0,0,84],43:[0,0,21,0],71:[0,0,0,84],547:[0,0,0,28]}
    for p, want in expected.items():
        got=[sum(zero_at_root(z,p) for z in product(range(7),repeat=n)) for n in range(1,5)]
        assert got==want,(p,got,want)
    for p, want in [(29,768),(43,432),(71,12000)]:
        d=(p-1)//7
        v=[pow(x,d,p) for x in range(p)]
        num=sum((v[x]+v[y]+v[z]+1)%p==0 for x in range(p) for y in range(p) for z in range(p))
        num+=sum((v[y]+v[z]+1)%p==0 for y in range(p) for z in range(p))
        num+=sum((v[z]+1)%p==0 for z in range(p))
        assert num==want,(p,num,want)
    print('VERIFY_SEVENTH_ROOT_OK')

if __name__=='__main__':run()
