"""Independent exact finite checks for growing-uniform-sampling missing counts.

Run: python3 checker.py. Python standard library only.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import product

checks = 0

def check(a, b, label):
    global checks
    assert a == b, (label, a, b)
    checks += 1


def dynamic(n, q):
    # Number of unobserved labels after each stage; stage i has q iid draws.
    law = {0: Fraction(1)}
    for i in range(1, n+1):
        nxt = {}
        for u, prob in law.items():
            r = u + 1
            for b in range(min(q, r)+1):
                ways = comb(r, b) * sum(
                    (-1)**h * comb(b,h) * (i-r+b-h)**q
                    for h in range(b+1)
                )
                assert ways >= 0
                v = r-b
                nxt[v] = nxt.get(v,Fraction(0)) + prob*Fraction(ways,i**q)
        law = nxt
        check(sum(law.values()), Fraction(1), f'normalization n={i} q={q}')
    return law


def mean_by_marginals(n,q):
    return sum((Fraction(j-1,n)**q for j in range(1,n+1)),Fraction(0))


def variance_by_pairs(n,q):
    p=[Fraction(j-1,n)**q for j in range(1,n+1)]
    ans=sum((x*(1-x) for x in p),Fraction(0))
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            joint=Fraction((i-1)*(j-2), n*(n-1))**q
            ans += 2*(joint - p[i-1]*p[j-1])
    return ans


def brute(n,q):
    # Independent exact enumerator without recurrence/inclusion-exclusion.
    d = {}
    stages=[list(product(range(i),repeat=q)) for i in range(1,n+1)]
    total=1
    for stage in stages: total*=len(stage)
    for trajectory in product(*stages):
        seen={x+1 for stage in trajectory for x in stage}
        unvisited=n-len(seen)
        d[unvisited]=d.get(unvisited,0)+1
    return {k:Fraction(v,total) for k,v in d.items()}

for q in range(1,5):
    for n in range(1,15):
        law=dynamic(n,q)
        mean=sum((k*p for k,p in law.items()),Fraction(0))
        var=sum(((k-mean)**2*p for k,p in law.items()),Fraction(0))
        check(mean,mean_by_marginals(n,q),f'mean {n} {q}')
        check(var,variance_by_pairs(n,q),f'variance {n} {q}')
        if q==2 and n>=2:
            closed=Fraction((n+1)*(2*n-1)*(2*n+1)*(4*n-5),180*n*n*(n-1))
            check(var,closed,f'q=2 closed variance {n}')

def conditional_mean(m, n, q, initial_unseen):
    law={initial_unseen: Fraction(1)}
    for stage in range(m+1,n+1):
        nxt={}
        for u, prob in law.items():
            r=u+1
            for b in range(min(q,r)+1):
                ways=comb(r,b)*sum((-1)**h*comb(b,h)*(stage-r+b-h)**q
                                    for h in range(b+1))
                nxt[r-b]=nxt.get(r-b,Fraction(0))+prob*Fraction(ways,stage**q)
        law=nxt
    return sum((u*prob for u,prob in law.items()),Fraction(0))

for q in range(1,5):
    for n in range(2,9):
        for m in range(1,n):
            for u in range(m):
                predicted=mean_by_marginals(n,q)+Fraction(m,n)**q*(u-mean_by_marginals(m,q))
                check(conditional_mean(m,n,q,u),predicted,
                      f'time regression q={q} m={m} n={n} u={u}')

for (n,q) in [(2,1),(3,1),(4,1),(5,1),(2,2),(3,2),(4,2),(5,2),(3,3),(4,3)]:
    lhs=dynamic(n,q)
    rhs=brute(n,q)
    for key in range(n+1):
        check(lhs.get(key,0),rhs.get(key,0),f'brute {n} {q} {key}')

print(f'CHECKS_PASS={checks}')
