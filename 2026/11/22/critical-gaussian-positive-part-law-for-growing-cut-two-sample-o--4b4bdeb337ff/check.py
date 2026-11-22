"""Reproducible exact checks for near-saturation overlap distances.
Uses only Python 3 standard library. All identities are proved separately in RESULT.md.
"""
from math import comb, sqrt
from itertools import combinations


def runs(word):
    return 1 + sum(word[i]!=word[i-1] for i in range(1,len(word)))


def rho_numerator(word,q):
    """Exact minimum of sum min(N_0,N_1) over <=q cuts, balanced samples."""
    N=len(word)
    c=[0]
    for b in word: c.append(c[-1]+b)
    prev=[N+1]*(N+1)
    prev[0]=0
    for _ in range(q+1):
        cur=[N+1]*(N+1)
        for j in range(N+1):
            cur[j]=min(prev[i]+min(c[j]-c[i],j-i-(c[j]-c[i])) for i in range(j+1))
        prev=cur
    return prev[N]


def full_iso_pattern_count(word):
    return sum(tuple(word[j:j+7])==(1,0,0,1,0,0,1) for j in range(0,len(word)-6,7))


def run_numbers(m,n):
    def C(a,b):return comb(a,b) if 0<=b<=a else 0
    out={}
    for r in range(2,m+n+1):
        if r%2==0:
            k=r//2
            z=2*C(m-1,k-1)*C(n-1,k-1)
        else:
            k=(r-1)//2
            z=C(m-1,k)*C(n-1,k-1)+C(m-1,k-1)*C(n-1,k)
        out[r]=z
    assert sum(out.values())==comb(m+n,m)
    return out


def main():
    checked=0
    for n in range(1,7):
        dist={}
        for positions in combinations(range(2*n),n):
            word=tuple(int(i in positions) for i in range(2*n))
            r=runs(word)
            dist[r]=dist.get(r,0)+1
            for q in range(1,2*n+1):
                a=rho_numerator(word,q)
                assert (a==0)==(q>=r-1),(n,word,q,a,r)
                d=max(r-1-q,0)
                assert a>= (d+1)//2,(n,word,q,a,d)
                checked+=2
        assert dist=={r:v for r,v in run_numbers(n,n).items() if v}
        checked+=1
    print('Exact word/DP/run-count assertions passed:',checked)
    # Check the constructive upper bound for words with actual isolated blocks.
    from random import Random
    rng=Random(20261116)
    checked2=0
    for n in (8,10,15,20,30,40):
        base=[0]*n+[1]*n
        for _ in range(75):
            rng.shuffle(base)
            word=tuple(base)
            R=runs(word)
            L=full_iso_pattern_count(word)
            for d in range(0,min(2*L,R-2)+1):
                q=R-1-d
                assert q>=1
                assert rho_numerator(word,q)==(d+1)//2,(n,d,L,word)
                checked2+=1
    print('Constructive isolated-pattern assertions passed:',checked2)
    for n in (3,6,10,25,50):
        dist=run_numbers(n,n)
        den=comb(2*n,n)
        mean=sum(r*v for r,v in dist.items())/den
        var=sum((r-mean)**2*v for r,v in dist.items())/den
        assert abs(mean-(n+1))<1e-9
        assert abs(var-n*(n-1)/(2*n-1))<1e-8
        for q in (1,n,2*n-1):
            p=sum(v for r,v in dist.items() if r-1<=q)/den
            assert 0<=p<=1
        print('n, mean R, sd R, P(rho_n=0):',n,mean,round(sqrt(var),6),round(sum(v for r,v in dist.items() if r-1<=n)/den,6))
    print('ALL CHECKS PASS')

if __name__=='__main__':main()
