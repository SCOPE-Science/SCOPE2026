"""Independent exhaustive checks of square-idempotence in increasing partial injections.
Only the Python standard library is required. Run: python verify.py
"""
from itertools import combinations
from math import comb, factorial
from collections import Counter


def compose(p, q):
    """Return p following q; maps represented by dictionaries."""
    return {x: p[q[x]] for x in q if q[x] in p}


def t(m):
    return sum(factorial(m)//(factorial(j)**2*factorial(m-2*j)) for j in range(m//2+1))


def root_count(n, fixed):
    s=(0,)+tuple(sorted(fixed))+(n+1,)
    out=1
    for i in range(len(s)-1):
        out*=t(s[i+1]-s[i]-1)
    return out


def gf_table(nmax):
    # Formal power series: T=1/sqrt((1-3z)(1+z)); F=sum_k u^k z^k T^(k+1)
    trin=[t(i) for i in range(nmax+1)]
    out=[Counter() for _ in range(nmax+1)]
    poly=[1]+[0]*nmax
    for k in range(nmax+1):
        nxt=[0]*(nmax+1)
        for i,a in enumerate(poly):
            if a:
                for j,b in enumerate(trin[:nmax+1-i]):
                    nxt[i+j]+=a*b
        poly=nxt
        for n in range(k,nmax+1):
            out[n][k]=poly[n-k]
    return out


def main():
    nmax=9
    coeff=gf_table(nmax)
    for n in range(nmax+1):
        counts=Counter()
        squares=Counter()
        elt=0
        idx=tuple(range(1,n+1))
        for r in range(n+1):
            for D in combinations(idx,r):
                for R in combinations(idx,r):
                    f=dict(zip(D,R))
                    elt+=1
                    ff=compose(f,f)
                    if compose(ff,ff)==ff:
                        # For increasing injective f, an idempotent square is partial identity.
                        assert all(x==y for x,y in ff.items())
                        S=frozenset(ff)
                        counts[len(S)]+=1
                        squares[S]+=1
                        assert S==frozenset(x for x,y in f.items() if x==y)
        assert elt==comb(2*n,n),(n,elt)
        for r in range(n+1):
            assert counts[r]==coeff[n][r],(n,r,counts[r],coeff[n][r])
        assert len(squares)==2**n
        for r in range(n+1):
            for S in combinations(idx,r):
                S=frozenset(S)
                assert squares[S]==root_count(n,S),(n,S,squares[S],root_count(n,S))
        print('n=%d elements=%d square_idempotent=%d fibers=%d rank_counts=%s PASS'%(
            n,elt,sum(counts.values()),len(squares),[counts[i] for i in range(n+1)]))
    print('VERIFY_OK')

if __name__=='__main__':
    main()

# Additional check of predicted logarithmic root-fiber cumulants for random idempotents.
# The direct exhaustive enumeration above is independent of this coefficient recursion.

def entropy_cumulants(N):
    from math import log
    b1=[log(t(m)) for m in range(N+1)]
    b2=[x*x for x in b1]
    f=[0.0]*(N+1);f1=f.copy();f2=f.copy()
    for n in range(N+1):
        f[n]=1.0+sum(f[n-1-j] for j in range(n))
        f1[n]=b1[n]+sum(b1[j]*f[n-1-j]+f1[n-1-j] for j in range(n))
        f2[n]=b2[n]+sum(b2[j]*f[n-1-j]+2*b1[j]*f1[n-1-j]+f2[n-1-j] for j in range(n))
    return f1[N]/f[N], f2[N]/f[N]-(f1[N]/f[N])**2

def entropy_constants(K=55):
    from math import log
    gamma=sum(log(t(m))*2**(-m-2) for m in range(K+1))
    var=sum((log(t(m))-gamma*(m+1))**2*2**(-m-2) for m in range(K+1))
    return gamma,var

if __name__=='__main__':
    g,v=entropy_constants()
    print('entropy_constants mean_per_n=%.12f variance_per_n=%.12f'%(g,v))
    for n in (30,60,100):
        a,b=entropy_cumulants(n)
        print('n=%d mean/n=%.12f var/n=%.12f'%(n,a/n,b/n))
    print('ENTROPY_RECURSION_OK')
