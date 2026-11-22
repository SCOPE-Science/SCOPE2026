"""Standalone exact checks for fixed-rank Henson type compatibility on cycle parameters."""
from itertools import combinations
from math import comb

def fibonacci(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def independent_cycle(mask,n):
    return not(mask & (((mask<<1)|(mask>>(n-1)))&((1<<n)-1)))

def gaps(mask,n):
    vs=[i for i in range(n) if mask>>i&1]
    return [(vs[(j+1)%len(vs)]-vs[j])%n or n for j in range(len(vs))]

def extrema(n,k):
    r=n-2*k
    hi=2**(k-1)*fibonacci(n-2*k+3)
    if r<=k:
        lo=2**(k-r)*3**r
        lo_mult=n*comb(k,r)//k
    else:
        lo=3**(k-1)*fibonacci(n-3*k+4)
        lo_mult=n
    hi_mult= (2 if n==2*k else n)
    return lo,hi,lo_mult,hi_mult

assert all(2*fibonacci(a+b-1)-fibonacci(a+1)*fibonacci(b+1)==fibonacci(a-2)*fibonacci(b-2) for a in range(2,40) for b in range(2,40))
assert all(fibonacci(a+1)*fibonacci(b+1)-3*fibonacci(a+b-2)==fibonacci(a-3)*fibonacci(b-3) for a in range(3,40) for b in range(3,40))
assert all(2*fibonacci(b+1)-3*fibonacci(b)==fibonacci(b-3) for b in range(3,40))
checks=0
for n in range(4,17):
    indep=[m for m in range(1<<n) if independent_cycle(m,n)]
    for k in range(1,n//2+1):
        per=[]
        for S in indep:
            if S.bit_count()!=k: continue
            partners=sum(1 for T in indep if not (S&T))
            via=1
            for d in gaps(S,n): via*=fibonacci(d+1)
            assert partners==via, (n,k,S,partners,via)
            per.append(partners)
            checks+=1
        lo,hi,lo_mult,hi_mult=extrema(n,k)
        assert min(per)==lo and max(per)==hi,(n,k,lo,hi,min(per),max(per))
        assert per.count(lo)==lo_mult,(n,k,'min multiplicity',per.count(lo),lo_mult)
        assert per.count(hi)==hi_mult,(n,k,'max multiplicity',per.count(hi),hi_mult)
    print('n',n,'one-types',len(indep),'nonempty-checks',sum(m!=0 for m in indep))
print('PASS identities=2850; direct partner counts=',checks,'n=4..16; extrema+counts all k')
