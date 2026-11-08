#!/usr/bin/env python3
"""Exact finite validation of two-seat approval-welfare/JR boundaries.
No external packages; Python 3.9+. Theorems are proved in RESULT.md.
"""
from itertools import product, combinations
from math import comb, factorial
from fractions import Fraction


def bad_av_pairs(votes, n):
    """votes[j] is n-bit approval-support mask for candidate j."""
    m = len(votes)
    pairs = list(combinations(range(m), 2))
    scores = [s.bit_count() for s in votes]
    max_total = max(scores[i] + scores[j] for i,j in pairs)
    best = [w for w in pairs if scores[w[0]]+scores[w[1]]==max_total]
    mask_all = (1 << n)-1
    def jr(w):
        uncovered = mask_all ^ (votes[w[0]] | votes[w[1]])
        return all((uncovered & votes[c]).bit_count() * 2 < n for c in range(m))
    return best, [w for w in best if not jr(w)]


def poly_mul(a,b,deg):
    o=[Fraction(0) for _ in range(deg+1)]
    for i,u in enumerate(a):
        for j,v in enumerate(b[:deg+1-i]):
            o[i+j]+=u*v
    return o


def model_prob(n,m,p=Fraction(1,2)):
    if n%2:return Fraction(0)
    M=comb(n,n//2)
    a=sum(Fraction(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n//2))
    b=Fraction(M)*p**(n//2)*(1-p)**(n//2)
    f=[Fraction(1)] + [Fraction(2,factorial(j))+(int(j==2)) for j in range(1,m+1)]
    pol=[Fraction(1)]+[Fraction(0) for _ in range(m)]
    for _ in range(M//2):pol=poly_mul(pol,f,m)
    total=Fraction(0)
    for r in range(m+1):
        safe=Fraction(factorial(r),M**r)*pol[r]
        assert 0<=safe<=1
        total+=Fraction(comb(m,r))*a**(m-r)*b**r*(1-safe)
    return total


def verify():
    tests=0
    for n,m in [(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(4,3),(4,4),(5,3),(6,3)]:
        bad=0
        for v in product(range(1<<n),repeat=m):
            best,bad_w=bad_av_pairs(v,n)
            assert any(w not in bad_w for w in best), (n,m,v)
            if n%2:assert not bad_w,(n,m,v)
            if bad_w:
                bad+=1
                assert n%2==0
                for i,j in bad_w:
                    assert v[i]==v[j] and v[i].bit_count()==n//2
                    assert any(c not in (i,j) and v[c]==(((1<<n)-1)^v[i]) for c in range(m))
                    assert max(s.bit_count() for s in v)==n//2
            tests+=1
        prob=Fraction(bad,(1<<n)**m)
        expected=model_prob(n,m)
        assert prob==expected, (n,m,prob,expected)
        if m==3:
            simple=(3*comb(n,n//2)*Fraction(1,8)**n) if n%2==0 else Fraction(0)
            assert prob==simple,(n,m,prob,simple)
        print(f'n={n}, m={m}: {bad} bad profiles of {(1<<n)**m}, P={prob}, OK')
    print('PASS: complete',tests,'labeled candidate-support profiles; independent occupancy coefficient identities.')

if __name__=='__main__': verify()


def weighted_check():
    """Independent exact weighted check, not relying on occupancy recurrence."""
    for n,m,p in [(2,3,Fraction(1,3)),(2,4,Fraction(2,5)),(4,3,Fraction(1,4))]:
        total=Fraction(0)
        for votes in product(range(1<<n),repeat=m):
            _,bad=bad_av_pairs(votes,n)
            if bad:
                ones=sum(v.bit_count() for v in votes)
                total+=p**ones*(1-p)**(n*m-ones)
        assert total==model_prob(n,m,p),(n,m,p,total,model_prob(n,m,p))
        print(f'exact weighted n={n},m={m},p={p}: {total}, OK')
    print('PASS: exact independent nonuniform Bernoulli probability checks.')

if __name__=='__main__': weighted_check()
