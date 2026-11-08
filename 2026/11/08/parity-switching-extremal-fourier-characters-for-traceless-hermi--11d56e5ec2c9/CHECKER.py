from itertools import product
from math import isclose

def makefield(p):
    # e^2=c+d*e; irreducible for p=2 or 3
    c,d=(1,1) if p==2 else (p-1,0)
    N=p*p
    def add(x,y):return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
    def neg(x):return ((-x%p)%p)+p*((-x//p)%p)
    def mul(x,y):
        a,b=x%p,x//p;u,v=y%p,y//p
        return ((a*u+c*b*v)%p)+p*((a*v+b*u+d*b*v)%p)
    def star(x):
        a,b=x%p,x//p
        return ((a+d*b)%p)+p*((-b)%p)
    T=[[mul(x,y) for y in range(N)] for x in range(N)]
    A=[[add(x,y) for y in range(N)] for x in range(N)]
    C=[star(x) for x in range(N)]
    def inv(x):
        assert x
        return next(y for y in range(1,N) if T[x][y]==1)
    invs=[0]+[inv(x) for x in range(1,N)]
    return N,T,A,C,invs

def rank(M,p,F):
    N,T,ADD,C,INV=F
    a=[list(row) for row in M]; n=len(a); r=0
    for j in range(n):
        pivot=next((i for i in range(r,n) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        factor=INV[a[r][j]]
        a[r]=[T[factor][v] for v in a[r]]
        for i in range(r+1,n):
            h=a[i][j]
            if h:
                a[i]=[ADD[a[i][k]][(-T[h][a[r][k]]%p)+p*((-(T[h][a[r][k]]//p))%p)] for k in range(n)]
        r+=1
        if r==n:break
    return r

def herm_matrices(p,n,F):
    N,T,ADD,C,INV=F
    diag=[(i,i) for i in range(n)]
    upper=[(i,j) for i in range(n) for j in range(i+1,n)]
    for vals in product(range(p),repeat=n):
        for up in product(range(N),repeat=len(upper)):
            mat=[[0]*n for _ in range(n)]
            for i,val in enumerate(vals):mat[i][i]=val
            for (i,j),val in zip(upper,up):mat[i][j]=val;mat[j][i]=C[val]
            yield mat

def nullities(M,p,F):
    n=len(M);N,T,ADD,C,INV=F
    return tuple(n-rank([[ADD[M[i][j]][t if i==j else 0] for j in range(n)] for i in range(n)],p,F) for t in range(p))

def formula_lambda(n,p,ds):
    B=sum((-p)**d for d in ds)
    num=(-p)**n *B//p-1
    assert num%(p+1)==0,(n,p,ds)
    return num//(p+1)

def direct_eigen(M,p,F):
    N,T,ADD,C,INV=F;n=len(M)
    # exact character count by trace values
    cnt=[0]*p;valid=0
    for v in product(range(N),repeat=n):
        if not any(v):continue
        norm=0
        for x in v:
            norm=(norm+T[C[x]][x])%p
        if norm:continue
        valid+=1
        form=0
        for i in range(n):
            for j in range(n):
                form=ADD[form][T[C[v[i]]][T[M[i][j]][v[j]]]]
        assert form<p
        cnt[form]+=1
    assert all(c%(p+1)==0 for c in cnt)
    cnt=[c//(p+1) for c in cnt]
    if p==2:return cnt[0]-cnt[1]
    if p==3:
        assert cnt[1]==cnt[2],cnt
        return cnt[0]-cnt[1]
    raise ValueError('p unsupported')

def test(p,n,full):
    F=makefield(p); d=((p**(2*n-1)+(p-1)*(-1)**n*p**(n-1)-1)//(p+1))
    L=(p**(n-1)*(p**(n-1)+(p-1 if n%2 else 2))+1)//(p+1)
    vals={};n_top=0; rows=0
    for i,M in enumerate(herm_matrices(p,n,F)):
        ds=nullities(M,p,F)
        lam=formula_lambda(n,p,ds)
        B=sum((-p)**dd for dd in ds)
        scalar=max(ds)==n
        if scalar:assert lam==d
        else:
            assert abs(lam)<=L,(p,n,ds,lam,L)
            if abs(lam)==L:
                assert lam==-L
                if n%2:assert sorted(ds)[-1]==n-1 and sum(x>0 for x in ds)==1
                else:assert sorted(ds)[-2:]==[1,n-1]
                n_top+=1
        vals[(ds,lam)]=vals.get((ds,lam),0)+1
        rows+=1
        if i in {0,1,17,42,100} or (p==2 and n==3):
            if (p==2 and n==3) or i in {0,17,100}:
                direct=direct_eigen(M,p,F)
                assert direct==lam,(p,n,ds,lam,direct)
    expected=(p*d if n%2 else p*((p-1)*p**(n-1)*(p**n-1)//(p+1)))
    assert n_top==expected,(p,n,n_top,expected)
    print('PASS p',p,'n',n,'num matrices',rows,'degree',d,'nontrivial radius',L,'top matrix count',n_top,'eigen classes',len(vals),'eigen values',sorted(set(l for _,l in vals)))

if __name__=='__main__':
    test(2,3,True)
    test(3,3,True)
    test(2,4,True)
