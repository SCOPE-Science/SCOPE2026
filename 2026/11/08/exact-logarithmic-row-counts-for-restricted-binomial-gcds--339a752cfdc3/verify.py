#!/usr/bin/env python3
"""Exact finite checks for the restricted-binomial-GCD row-count asymptotic."""
from math import gcd, factorial, comb

def lucas_nonzero(n,k,p):
    while n or k:
        if k%p>n%p: return False
        k//=p;n//=p
    return True

def token_weights(n,m,p):
    w=[]; power=1
    while n:
        d=n%p
        w.extend([power%m]*d)
        power=power*p%m
        n//=p
    return w

def min_zero_sum(w,m):
    # Tests whether the only zero-sum subsequences are empty and whole.
    total=sum(w)%m
    if total: return False
    # Use a prefix bitmask including nonempty subsequences; whole excluded by last item.
    nonempty=set()
    for a in w[:-1]:
        nonempty |= {(r+a)%m for r in nonempty} | {a%m}
        if 0 in nonempty: return False
    return True

def gcd_positive_by_lucas(m,q,p):
    N=m*q
    return all(not lucas_nonzero(N,m*j,p) for j in range(1,q))

def ord_mod(p,m):
    h=1;x=p%m
    while x!=1:
        x=x*p%m;h+=1
    return h

checks=0
for m in range(2,11):
    for p in (2,3,5,7,11):
        if gcd(m,p)!=1: continue
        for q in range(2,351):
            n=m*q
            a=min_zero_sum(token_weights(n,m,p),m)
            b=gcd_positive_by_lucas(m,q,p)
            assert a==b, (m,p,q,a,b)
            checks+=1
print('DIRECT_LUCAS_VS_MINIMAL_ZERO_SUM',checks)

# A separate exhaustive word test of the maximal-length cyclic zero-sum lemma.
word_checks=0
from itertools import product
for m in range(2,9):
    for t in product(range(1,m),repeat=m):
        if sum(t)%m!=0: continue
        good=min_zero_sum(list(t),m)
        if good:
            assert len(set(t))==1 and gcd(t[0],m)==1
        if len(set(t))==1 and gcd(t[0],m)==1:
            assert good
        word_checks+=1
print('MAXIMAL_LENGTH_CYCLIC_WORDS',word_checks)

# Count large cutoffs by enumerating only integers with few base-p digits.
def count_sparse(m,p,L):
    bound=m*(p**L)
    # Enumerate base-p integers N<=bound with digit-sum at most m.
    # Distinct representations as digit vectors, no p carries permitted.
    K=0
    max_exp=L+2
    def walk(e,rem,N,weights):
        nonlocal K
        if e==max_exp:
            if N>m and N<=bound and N%m==0 and min_zero_sum(weights,m):
                K+=1
            return
        base=p**e
        for d in range(min(p-1,rem)+1):
            walk(e+1, rem-d, N+d*base, weights+[(base%m)]*d)
    walk(0,m,0,[])
    return K
for m,p,exps in [(3,2,[8,10,12,14,16]),(4,3,[6,8,10,12]),(5,2,[8,12,16,20])]:
    h=ord_mod(p,m)
    for L in exps:
        c=count_sparse(m,p,L)
        pred=L**m/(factorial(m)*h**(m-1))
        print('COUNT',m,p,L,c,'leading',round(pred,5))
print('VERIFY_OK finite_checks_only=True')

def finite_profile_formula(m,p,L):
    h=ord_mod(p,m)
    n=[len(range(r,L,h)) for r in range(h)]
    cells=[(r,d) for r in range(h) for d in range(1,p)]
    out=0
    def go(i,rem,e,weights):
        nonlocal out
        if i==len(cells):
            if not weights or not min_zero_sum(weights,m):return
            factor=1
            for r in range(h):
                E=sum(e[j] for j,(rr,d) in enumerate(cells) if rr==r)
                if E>n[r]: return
                numer=factorial(n[r])//factorial(n[r]-E)
                denom=1
                for j,(rr,d) in enumerate(cells):
                    if rr==r:denom*=factorial(e[j])
                factor*=numer//denom
            out+=factor
            return
        r,d=cells[i]
        for t in range(rem//d+1):
            e.append(t)
            go(i+1,rem-t*d,e,weights+[pow(p,r,m)]*(d*t))
            e.pop()
    go(0,m,[],[])
    return out-(1 if p**L>m else 0)

for m,p in [(3,2),(4,3),(5,2),(5,3),(7,2)]:
    for L in range(2,11):
        lhs=finite_profile_formula(m,p,L)
        rhs=sum(min_zero_sum(token_weights(m*q,m,p),m) for q in range(2,(p**L-1)//m+1))
        assert lhs==rhs,(m,p,L,lhs,rhs)
    print('EXACT_PROFILE_REPLAY',m,p,ord_mod(p,m),'L=2..10')
print('ALL_EXACT_PROFILE_TESTS_OK')

# Exact degree-at-most-five interpolation certificates for the m=5, p=2 case.
# The proof already bounds each congruence branch degree by five.
def branch0(L):
    return (L**5+40*L**4+560*L**3-640*L**2+6144*L-30720)//30720

def branch2(L):
    return (L**5+40*L**4+600*L**3-640*L**2+12944*L-59520)//30720

for L in range(4,25,4):
    assert finite_profile_formula(5,2,L)==branch0(L)
for L in range(6,27,4):
    assert finite_profile_formula(5,2,L)==branch2(L)
assert branch0(16)!=branch2(16)
print('ORDER_FOUR_BRANCH_POLYNOMIAL_CERTIFICATE_OK six_points_per_branch=True')
