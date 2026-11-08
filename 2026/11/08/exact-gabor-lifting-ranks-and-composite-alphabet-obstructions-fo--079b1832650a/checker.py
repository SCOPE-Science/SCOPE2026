"""Exact tests for cyclotomic-alphabet Gabor rank and overlap obstructions.

Uses exact Z[omega] arithmetic for every zero-frequency ambiguity sum.
Nonzero modulation nonvanishing follows from the proof's cyclotomic field
argument; floating-point checks are only independent spot corroboration.
"""
from itertools import product
from math import gcd
import cmath

Z6 = ((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))


def semigroup(n,m):
    primes=[]; t=m
    for d in range(2,t+1):
        if t%d==0:
            primes.append(d)
            while t%d==0: t//=d
        if d*d>t: break
    if t>1: primes.append(t)
    a={0}
    for i in range(n+1):
        for prime in primes:
            if i+prime<=n and i in a: a.add(i+prime)
    return a


def overlap(p,S,u):
    return sorted(t for t in S if (t+u)%p in S)


def expsum6(e,m):
    x,y=0,0
    for exp in e:
        a,b=Z6[(6//m*exp)%6]
        x+=a;y+=b
    return (x,y)


def ambigu_zero_frequency(p,S,m,phase,u):
    edge=[(phase[(t+u)%p]-phase[t])%m for t in overlap(p,S,u)]
    return expsum6(edge,m)==(0,0)


def rank_formula(p,S,m,phase):
    D={u for u in range(p) if overlap(p,S,u)}
    Z=sum(ambigu_zero_frequency(p,S,m,phase,u) for u in D if u)
    return p*len(D)-Z


def brute_sample(p,S,m):
    S=set(S)
    fails=0
    count=0
    predicted=all(len(overlap(p,S,u)) not in semigroup(p,m) for u in range(1,p))
    for labels in product(range(m),repeat=len(S)):
        phase=dict(zip(sorted(S),labels))
        rank=rank_formula(p,S,m,phase)
        fails+=(rank<p*p)
        count+=1
        assert rank<=p*p
        if count%23==0:
            for u in range(p):
                for v in range(p):
                    terms=[cmath.exp(2j*cmath.pi*((phase[(t+u)%p]-phase[t])/m+v*t/p))
                           for t in overlap(p,S,u)]
                    numerical_zero=abs(sum(terms))<1e-7
                    if v==0:
                        assert numerical_zero==ambigu_zero_frequency(p,S,m,phase,u)
                    elif terms:
                        assert not numerical_zero, (p,m,S,u,v,labels)
        if predicted:
            assert rank==p*p,(p,m,S,labels,rank)
    assert (fails==0)==predicted,(p,m,S,fails,predicted)
    return count,fails


def explicit_r31():
    p=31;S={t*t%p for t in range(1,p)}
    assert len(S)==15
    assert {len(overlap(p,S,u)) for u in range(1,p)}=={7}
    assert 7 not in semigroup(7,2) and 7 not in semigroup(7,3)
    assert 7 in semigroup(7,6)
    u=1;edges=overlap(p,S,u)
    edge_label=dict(zip(edges,[0,3,0,3,0,2,4]))
    indeg={t:0 for t in S}
    for t in edges: indeg[(t+u)%p]+=1
    phase={}
    for root in sorted(t for t in S if indeg[t]==0):
        t=root;phase[t]=0
        while t in edge_label:
            dest=(t+u)%p
            assert dest not in phase
            phase[dest]=(phase[t]+edge_label[t])%6
            t=dest
    assert set(phase)==S
    assert ambigu_zero_frequency(p,S,6,phase,u)
    assert ambigu_zero_frequency(p,S,6,phase,p-u)
    return len(S),rank_formula(p,S,6,phase),sorted(phase.items())


def main():
    checks=[]
    tests=[(5,{0,1,2},m) for m in (1,2,3,6)]
    tests += [(7,{1,2,4},m) for m in (1,2,3,6)]
    tests += [(7,{0,1,2,3},m) for m in (1,2,3,6)]
    for p,S,m in tests:
        assert gcd(p,m)==1
        n,fails=brute_sample(p,S,m)
        checks.append((p,len(S),m,n,fails))
    size,rnk,pattern=explicit_r31()
    assert rnk<=31*31-2
    print('EXACT_CYCLOTOMIC_ALPHABET_GABOR_PASS')
    print('cases (p, support_size, alphabet_order, total_assignments, defective):')
    for c in checks:print(c)
    print('total_signings',sum(x[3] for x in checks))
    print('p31 composite failure support_size',size,'lifting_rank',rnk)
    print('p31 sabotage phase exponents (t,exp)',pattern)

if __name__=='__main__': main()
