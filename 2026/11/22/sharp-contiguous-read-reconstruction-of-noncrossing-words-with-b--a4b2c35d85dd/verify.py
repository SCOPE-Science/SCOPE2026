"""Independent small-size profile and enumeration checks for noninterlacing words.
Use the complete <=k contiguous-factor multiplicity readout."""
from collections import Counter,defaultdict
from itertools import product

def spectrum(word,k):
    return tuple(tuple(sorted(Counter(tuple(word[i:i+j]) for i in range(len(word)-j+1)).items())) for j in range(1,min(k,len(word))+1))

def is_noncrossing(word):
    pos=defaultdict(list)
    for i,a in enumerate(word):pos[a].append(i)
    for a,pa in pos.items():
        for b,pb in pos.items():
            if a>=b:continue
            for x,y in zip(pa,pa[1:]):
                for u,v in zip(pb,pb[1:]):
                    if x<u<y<v or u<x<v<y:return False
    return True

def verify(k,q,nmax):
    tested=0;unique=0
    for n in range(1,nmax+1):
        fibers=defaultdict(lambda:[0,False,None,None])
        for w in product(range(q),repeat=n):
            if max(Counter(w).values())>2*k-2:continue
            p=spectrum(w,k);entry=fibers[p];entry[0]+=1
            if entry[2] is None:entry[2]=w
            elif entry[3] is None:entry[3]=w
            if is_noncrossing(w):entry[1]=True
            tested+=1
        for p,(size,has_nc,a,b) in fibers.items():
            if has_nc:
                assert size==1,(k,q,n,size,a,b)
                unique+=1
    return (k,q,nmax,tested,unique)

if __name__=='__main__':
    for args in [(2,4,7),(3,3,11),(3,4,8),(4,3,10)]:
        print('PASS',verify(*args))
    for k in range(2,9):
        x=(0,)*k+(1,)+(0,)*(k-1)
        y=(0,)*(k-1)+(1,)+(0,)*k
        assert x!=y and spectrum(x,k)==spectrum(y,k)
        print('sharpness PASS',k,'length',2*k)

    # Noncrossing partitions with blocks at most m=2k-2:
    # F=1+sum_{j=1}^m z^j F^j, tested via recursive decomposition.
    from functools import lru_cache
    def count_gf(m,N):
        a=[0]*(N+1);a[0]=1
        for n in range(1,N+1):
            total=0
            for j in range(1,min(m,n)+1):
                dp=[1]+[0]*n
                for _ in range(j):
                    nex=[0]*(n+1)
                    for i in range(n+1):
                        if not dp[i]:continue
                        for b in range(n-i+1):nex[i+b]+=dp[i]*a[b]
                    dp=nex
                total+=dp[n-j]
            a[n]=total
        return a
    def rgfs(n):
        if n==0:yield ();return
        def extend(w,m):
            if len(w)==n:yield tuple(w);return
            for c in range(1,m+2):yield from extend(w+[c],max(c,m))
        yield from extend([1],1)
    for m in (2,4,6):
        N=9; counts=count_gf(m,N)
        for n in range(1,N+1):
            actual=sum(is_noncrossing(w) and max(Counter(w).values())<=m for w in rgfs(n))
            assert actual==counts[n],(m,n,actual,counts[n])
        print('capacity series PASS',m,counts)
