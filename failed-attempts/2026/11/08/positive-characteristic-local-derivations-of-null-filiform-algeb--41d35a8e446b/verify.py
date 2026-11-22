"""Exhaustive small-case checks for local derivations of truncated nilpotent polynomials."""
from itertools import product
from collections import Counter

def rank(a,q):
    a=[list(row) for row in a]
    m=len(a); n=len(a[0]) if m else 0; r=0
    for j in range(n):
        piv=next((i for i in range(r,m) if a[i][j]%q),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][j],-1,q)
        a[r]=[(v*inv)%q for v in a[r]]
        for i in range(m):
            if i!=r:
                z=a[i][j]
                if z: a[i]=[(x-z*y)%q for x,y in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r

def rec(n,p,q):
    js=[j for j in range(n,0,-1) if j%p]
    counts={0:1}
    for j in js:
        d=n-j+1
        nxt={}
        for r,c in counts.items():
            nxt[r]=nxt.get(r,0)+c*q**r
            nxt[r+1]=nxt.get(r+1,0)+c*(q**d-q**r)
        counts=nxt
    return counts

def exhaustive(n,p,q):
    assert p==q and p in [2,3]
    cells=[(i,j) for j in range(1,n+1) if j%p for i in range(j,n+1)]
    hist=Counter()
    for digits in product(range(q),repeat=len(cells)):
        M=[[0]*n for _ in range(n)]
        for (i,j),a in zip(cells,digits): M[i-1][j-1]=a
        hist[rank(M,q)]+=1
    expected=rec(n,p,q)
    js=[j for j in range(n,0,-1) if j%p]
    max_count=1
    for i,j in enumerate(js):
        max_count*=q**(n-j+1)-q**i
    assert expected[len(js)]==max_count
    ell=n//p; r=n%p
    from fractions import Fraction
    prob=(Fraction(q-1,q)**r)
    for h in range(1,ell+1):
        prob*=Fraction(q**(h+1)-1,q**(h+1))**(p-1)
    assert Fraction(max_count,q**len(cells))==prob
    assert dict(hist)==expected,(n,p,q,hist,expected)
    # Independently check the defining local-derivation condition, not just the matrix pattern.
    if q**(n*n)<=10**6:
        domain=list(product(range(q),repeat=n))
        possible={x:set() for x in domain}
        for f in domain:
            for x in domain:
                out=tuple(sum((j+1)*x[j]*f[k-j] for j in range(k+1))%q for k in range(n))
                # t^j derivative * f; coordinate k index k+1, f index 0 corresponds t^1.
                possible[x].add(out)
        nlocal=0
        for digits in product(range(q),repeat=n*n):
            M=[digits[i*n:(i+1)*n] for i in range(n)]
            ok=True
            for x in domain:
                y=tuple(sum(M[i][j]*x[j] for j in range(n))%q for i in range(n))
                if y not in possible[x]:ok=False;break
            if ok:
                nlocal+=1
                for j in range(1,n+1):
                    for i in range(1,n+1):
                        a=M[i-1][j-1]
                        assert (j%p!=0 and i>=j) or a==0
        assert nlocal==q**len(cells),(n,p,nlocal,len(cells))
    print('n,p,q,dimension,counts,OK:',n,p,q,len(cells),dict(sorted(hist.items())))

for n,p,q in [(1,2,2),(2,2,2),(3,2,2),(4,2,2),(2,3,3),(3,3,3),(4,3,3),(5,2,2)]:
    exhaustive(n,p,q)
print('VERIFY_OK')
