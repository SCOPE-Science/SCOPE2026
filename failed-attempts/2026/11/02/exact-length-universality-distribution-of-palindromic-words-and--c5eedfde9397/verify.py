#!/usr/bin/env python3
"""Standalone finite checks for shortest palindromic subsequence-universal words."""
import itertools
import math

def palindromes(q, n):
    for half in itertools.product(range(q), repeat=(n+1)//2):
        yield half + (half[:-1] if n%2 else half)[::-1]

def contains_subsequence(w, v):
    it=iter(w)
    return all(any(x==a for x in it) for a in v)

def universal_literal(w,q,k):
    return all(contains_subsequence(w, v) for v in itertools.product(range(q),repeat=k))

def universal_arches(w,q,k):
    found=set(); t=0
    for a in w:
        found.add(a)
        if len(found)==q:
            t+=1;found.clear()
    return t>=k

def predicted_length(q,k):
    return q*k if k%2==0 else q*(k+1)-1

def predicted_forms(q,k):
    # Concatenation of k/2 arbitrary permutation blocks on the left,
    # reverse of those blocks on the right, and a shortest universal
    # palindromic center for odd k.
    perms=list(itertools.permutations(range(q)))
    for left_blocks in itertools.product(perms,repeat=k//2):
        left=tuple(x for b in left_blocks for x in b)
        centers=((),) if k%2==0 else tuple(p+p[:-1][::-1] for p in perms)
        for center in centers:
            yield left+center+left[::-1]

literal_words=0
arch_agreement=0
all_shorter=0
all_minimal=0
construct_cases=0
for q,k in [(2,j) for j in range(1,8)] + [(3,j) for j in range(1,6)] + [(4,j) for j in range(1,4)] + [(5,j) for j in range(1,3)] + [(6,j) for j in range(1,3)]:
    n=predicted_length(q,k)
    expect=set(predicted_forms(q,k))
    assert len(expect)==math.factorial(q)**((k+1)//2)
    actual=set()
    for w in palindromes(q,n):
        a=universal_arches(w,q,k)
        # Literal checks on all q<=3 and selected q=4 samples, and all predicted forms.
        if q<=3 or (q==4 and k<=2) or w in expect:
            b=universal_literal(w,q,k)
            assert a==b,(q,k,w)
            literal_words+=1
        arch_agreement+=1
        if a:actual.add(w)
    assert actual==expect,(q,k,len(actual),len(expect),list(actual-expect)[:1],list(expect-actual)[:1])
    all_minimal+=1
    construct_cases+=len(expect)
    for m in range(n):
        # All shorter palindromes when the total search is bounded.
        if q**((m+1)//2) <= 200000:
            for w in palindromes(q,m):
                assert not universal_arches(w,q,k)
                all_shorter+=1
print('VERIFY_OK length_optima=%d construction_words=%d palindrome_profiles=%d literal_subsequence_checks=%d shorter_palindromes=%d' % (all_minimal,construct_cases,arch_agreement,literal_words,all_shorter))

# Exact palindromic arch-doubling theorem and constructive absent witnesses.
def greedy_profile(w,q):
    ends=[]; seen=set(); start=0
    for i,a in enumerate(w):
        seen.add(a)
        if len(seen)==q:
            ends.append((i,a));seen.clear();start=i+1
    return len(ends), w[start:], tuple(a for _,a in ends)

indices=0
witness_checks=0
for q, max_half in [(2,11),(3,8),(4,7)]:
    for n in range(max_half+1):
        for h in itertools.product(range(q),repeat=n):
            t,r,m=greedy_profile(h,q)
            even=h+h[::-1]
            assert greedy_profile(even,q)[0]==2*t,(q,h)
            missing=set(range(q))-set(r)
            assert missing
            a=min(missing)
            missing_even=m+(a,)+m[::-1]
            assert not contains_subsequence(even,missing_even),(q,h,missing_even)
            witness_checks+=1
            indices+=1
            for c in range(q):
                odd=h+(c,)+h[::-1]
                predicted=2*t+(int(set(r)|{c}==set(range(q))))
                assert greedy_profile(odd,q)[0]==predicted,(q,h,c,predicted)
                if predicted==2*t:
                    a=min(set(range(q))-(set(r)|{c}))
                    witness=m+(a,)+m[::-1]
                else:
                    assert c not in r
                    witness=m+(c,c)+m[::-1]
                assert not contains_subsequence(odd,witness),(q,h,c,witness)
                witness_checks+=1
                indices+=1
print('ARCH_DOUBLING_OK profiles=%d absent_witnesses=%d' % (indices,witness_checks))

# Rational two-variable generating function via integer convolutions.
def onto(n,r):
    return sum((-1)**(r-j)*math.comb(r,j)*j**n for j in range(r+1))

def profiles_from_GF(q, N):
    # Coefficient of y^h u^t in A(y)^t R(y): half-length h, t greedy arches.
    arch=[0]*(N+1);rem=[0]*(N+1);single=[0]*(N+1)
    for h in range(N+1):
        rem[h]=q**h-onto(h,q)
        single[h]=q*onto(h,q-1)
        if h>=1: arch[h]=q*onto(h-1,q-1)
    dp={(0,0):1}; counts={}
    # Each h arch profile: t times convolution, then arbitrary remainder.
    arches=[[0]*(N+1) for _ in range(N+1)]
    arches[0][0]=1
    for t in range(1,N+1):
        for h in range(N+1):
            arches[t][h]=sum(arches[t-1][h-j]*arch[j] for j in range(1,h+1))
    for h in range(N+1):
        for t in range(N+1):
            rh=sum(arches[t][j]*rem[h-j] for j in range(h+1))
            sh=sum(arches[t][j]*single[h-j] for j in range(h+1))
            if rh:
                counts[(2*h,2*t)]=rh
                counts[(2*h+1,2*t)]=q*rh-sh
            if sh:
                counts[(2*h+1,2*t+1)]=sh
    return counts

checked_GF=0
for q,N in [(2,11),(3,7),(4,5)]:
    expected=profiles_from_GF(q,N)
    for length in range(2*N+2):
        histogram={}
        for w in palindromes(q,length):
            idx=greedy_profile(w,q)[0]
            histogram[idx]=histogram.get(idx,0)+1
        for idx in set(histogram)|{a for n,a in expected if n==length}:
            assert histogram.get(idx,0)==expected.get((length,idx),0),(q,length,idx,histogram.get(idx,0),expected.get((length,idx),0))
        checked_GF+=1
print('GENERATING_FUNCTION_OK lengths=%d' % checked_GF)
