"""Direct multiplication and independent coefficient checks for cyclic quandle affine endomorphisms."""
from itertools import product
from collections import Counter

def formula(p,e,t):
    n=p**e
    c=[(p-1)*p**(e-r-1) for r in range(e)]+[1]
    h=(e-1)//2
    A=(p+1)*sum(p**(e-1-2*v) for v in range(h+1))+(e%2==0)
    T=A*n**t+(1-A)*(n//p)**t
    B=Counter()
    for rs in product(range(e+1),repeat=t):
        rank=tuple(p**(e-r) for r in rs)
        prod_rank=p**(e-min(e,sum(rs)))
        B[rank+(prod_rank,)]+=n*__import__('math').prod(c[r] for r in rs)
    B[(n,)*(t+1)]+=T-n**(t+1)
    return +B

def brute(n,t):
    els=list(product(range(n),repeat=2))
    C=Counter()
    for tup in product(els,repeat=t):
        if any(((a-1)*d-(c-1)*b)%n for i,(a,b) in enumerate(tup) for c,d in tup[i+1:]):
            continue
        ranks=tuple(len({(a*x+b)%n for x in range(n)}) for a,b in tup)
        aa=1;bb=0
        for a,b in tup:
            aa=a*aa%n;bb=(a*bb+b)%n
        pr=len({(aa*x+bb)%n for x in range(n)})
        C[ranks+(pr,)]+=1
    return C

def main():
    cases=[(2,1,3),(3,1,3),(5,1,2),(2,2,3),(3,2,2),(2,3,2),(3,2,3)]
    for p,e,t in cases:
        got=brute(p**e,t)
        expected=formula(p,e,t)
        assert got==expected,(p,e,t,(got-expected),(expected-got))
        print('PASS',p,e,t,'commuting',sum(got.values()),'rank_strata',len(got))
    print('ALL_RANK_CHECKS_PASSED')
if __name__=='__main__':main()
