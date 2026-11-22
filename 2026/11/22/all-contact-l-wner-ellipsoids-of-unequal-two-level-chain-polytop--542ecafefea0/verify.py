"""Exact arithmetic corroboration of outer ellipsoid and contact design."""
from fractions import Fraction as F
from itertools import product

def zero_distribution(m):
    if m % 2:
        return {0:F(1,m+1),(m+1)//2:F(m,m+1)}
    r=m//2
    return {0:F(1,m+2),r:F(1,2),r+1:F(r,2*(r+1))}

def check(p,q):
    n=p+q; a=F(p+1,2*(n+1)); b=F(q+1,2*(n+1))
    w=F(4*(n+1),n*(p+1)*(q+1))
    H=[[w*(q+1) if i==j and i<p else w*(p+1) if i==j else w if (i<p)!=(j<p) else F(0) for j in range(n)] for i in range(n)]
    c=[a]*p+[b]*q
    def quad(x):
        y=[v-t for v,t in zip(x,c)]
        return sum(y[i]*H[i][j]*y[j] for i in range(n) for j in range(n))
    assert quad([0]*n)==1
    # Because every binary point in one block has quadratic value 1, vertex contact is exact.
    if n<=12:
        for mask in product((0,1),repeat=p): assert quad(list(mask)+[0]*q)==1
        for mask in product((0,1),repeat=q): assert quad([0]*p+list(mask))==1
    for m in (p,q):
        D=zero_distribution(m)
        assert sum(D.values())==1
        assert sum(F(k)*v for k,v in D.items())==F(m,2)
        assert sum(F(k*(k-1))*v for k,v in D.items())==F(m*(m-1),4)
    wa=F(p+1,n+1); wb=F(q+1,n+1)
    mass0=wa*zero_distribution(p)[0]+wb*zero_distribution(q)[0]-F(1,n+1)
    assert mass0>0
    # Exact covariance of the constructed contact design.
    S=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i<p and j<p: raw=a if i==j else a/2
            elif i>=p and j>=p: raw=b if i==j else b/2
            else: raw=F(0)
            S[i][j]=raw-c[i]*c[j]
    for i in range(n):
        for j in range(n):
            v=sum(H[i][k]*S[k][j] for k in range(n))
            assert v==(F(1,n) if i==j else 0),(p,q,i,j,v)
    assert (p+1)*(q+1)-p*q==n+1
    return n

if __name__=='__main__':
    t=0
    for p in range(1,20):
        for q in range(1,20):
            t+=check(p,q)
    print('UNBALANCED_TWO_BLOCK_LOEWNER_EXACT_PASS',361,'pairs',t,'coordinates')
