"""Independent finite-field checks for a three-level incidence-algebra rank census.
Python 3 standard library only. Run: python verify.py
"""
from collections import Counter
from itertools import product
from math import comb


def expected(n,q):
    out=Counter()
    for a,b,c in product(range(n+1),repeat=3):
        r=sum(x*(n-y)+(n-x)*y for x,y in ((a,b),(a,c),(b,c)))
        # Count pairs of colorings before quotienting by complement.
        out[r]+=comb(n,a)*comb(n,b)*comb(n,c)*q**r
    return {r:v//2 for r,v in sorted(out.items())}


def intervals(n):
    m=3*n
    return [(i,j) for i in range(m) for j in range(m) if i==j or i//n<j//n]


def binary_case(n):
    pairs=intervals(n); dim=len(pairs); idx={p:i for i,p in enumerate(pairs)}
    terms=[(idx[(i,j)],idx[(j,k)],idx[(i,k)]) for i,j in pairs for a,k in pairs if a==j]
    def mult(x,y):
        z=0
        for a,b,c in terms:
            if ((x>>a)&1) and ((y>>b)&1): z^=1<<c
        return z
    units=[1<<j for j in range(dim)]
    def rank_binary(columns):
        pivots={}
        for col in columns:
            x=col
            while x:
                p=x.bit_length()-1
                if p in pivots: x^=pivots[p]
                else:
                    pivots[p]=x
                    break
        return len(pivots)
    hist=Counter()
    seen=set()
    for x in range(1<<dim):
        if mult(x,x)!=x:continue
        columns=[mult(x,e)^mult(e,x) for e in units]
        r=rank_binary(columns)
        # Two distinct idempotents x and x+1 have identical inner derivation.
        hist[r]+=1
        if n==1:
            diag=tuple((x>>idx[(i,i)])&1 for i in range(3))
            assert r==sum(diag[i]!=diag[j] for i in range(3) for j in range(i+1,3))
    assert all(v%2==0 for v in hist.values())
    hist={r:c//2 for r,c in sorted(hist.items())}
    assert hist==expected(n,2),(n,hist,expected(n,2))
    print('BINARY_EXHAUSTIVE_OK',n,dim,hist)


def gf4_mul(x,y):
    z=0
    for j in range(2):
        if y>>j&1: z^=x<<j
    # polynomial t^2+t+1
    if z&8:z^=0b1110
    if z&4:z^=0b111
    return z


def quartic_case():
    n=1; pairs=intervals(n);dim=len(pairs); idx={p:i for i,p in enumerate(pairs)}
    terms=[(idx[(i,j)],idx[(j,k)],idx[(i,k)]) for i,j in pairs for a,k in pairs if a==j]
    def mult(x,y):
        z=[0]*dim
        for a,b,c in terms:z[c]^=gf4_mul(x[a],y[b])
        return z
    def rref_rank(columns):
        a=[[columns[j][i] for j in range(dim)] for i in range(dim)]
        r=0
        for j in range(dim):
            k=next((k for k in range(r,dim) if a[k][j]!=0),None)
            if k is None:continue
            a[r],a[k]=a[k],a[r]
            # In GF4 the inverse of nonzero value is its square.
            inv=gf4_mul(a[r][j],a[r][j])
            a[r]=[gf4_mul(t,inv) for t in a[r]]
            for h in range(dim):
                if h!=r and a[h][j]:
                    fac=a[h][j]
                    a[h]=[u^gf4_mul(fac,v) for u,v in zip(a[h],a[r])]
            r+=1
            if r==dim:break
        return r
    hist=Counter()
    for xx in product(range(4),repeat=dim):
        x=list(xx)
        if mult(x,x)!=x:continue
        cols=[]
        for j in range(dim):
            e=[0]*dim;e[j]=1
            a=mult(x,e);b=mult(e,x)
            cols.append([aa^bb for aa,bb in zip(a,b)])
        hist[rref_rank(cols)]+=1
    assert all(v%2==0 for v in hist.values())
    hist={r:c//2 for r,c in sorted(hist.items())}
    assert hist==expected(1,4),(hist,expected(1,4))
    print('GF4_EXHAUSTIVE_OK',hist)


def max_stratum():
    for n in range(1,11):
        cc=0
        for a,b,c in product(range(n+1),repeat=3):
            r=sum(x*(n-y)+(n-x)*y for x,y in ((a,b),(a,c),(b,c)))
            if r==2*n*n:cc+=comb(n,a)*comb(n,b)*comb(n,c)
            assert r<=2*n*n
        assert cc==6*(2**n-1),(n,cc)
    print('MAX_CUT_ENUMERATION_OK through n=10')


if __name__=='__main__':
    binary_case(1)
    binary_case(2)
    quartic_case()
    max_stratum()
    print('VERIFY_OK')
