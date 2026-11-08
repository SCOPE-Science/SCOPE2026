#!/usr/bin/env python3
"""Checks a q-letter adjacent-distinct word's greedy-arch distribution.
Compares the collapsed-state recurrence against an independent polynomial
rational identity, exhaustive proper words, and direct subsequence testing.
"""
from fractions import Fraction
from collections import defaultdict
from itertools import product
from math import factorial


def add(A, B):
    d=A.copy()
    for k,v in B.items(): d[k]+=v
    return d


def coeffs(q, maxn):
    # collapsed state s=0..q-1, number of completed arches k
    states={(0,0):1}
    out=[{0:1}]
    for n in range(1,maxn+1):
        ns=defaultdict(int)
        if n==1:
            ns[(1,0)]=q
        else:
            for (s,k),v in states.items():
                if s==0:
                    ns[(1,k)]+=(q-1)*v
                else:
                    ns[(s,k)]+=(s-1)*v
                    if s==q-1: ns[(0,k+1)]+=v
                    else: ns[(s+1,k)]+=(q-s)*v
        states=ns
        a=defaultdict(int)
        for (s,k),v in states.items():a[k]+=v
        out.append({k:v for k,v in a.items() if v})
    return out


def polys(q):
    # D(z)=product_{j=1}^{q-2}(1-jz)
    D=[1]
    for j in range(1,q-1):
        e=[0]*(len(D)+1)
        for i,v in enumerate(D):e[i]+=v; e[i+1]-=j*v
        D=e
    # H numerator: sum (q-1)!/(q-j)! z^(j-1) * D/prod_{h=1}^{j-1}(1-hz)
    # D quotient via product over h=j,...,q-2 (excluding h=0).
    H=[0]*(q-1)
    for j in range(1,q):
        v=[1]
        for h in range(j,q-1):
            v2=[0]*(len(v)+1)
            for i,x in enumerate(v):v2[i]+=x;v2[i+1]-=h*x
            v=v2
        factor=factorial(q-1)//factorial(q-j)
        for i,x in enumerate(v):H[i+j-1]+=factor*x
    C=[0]*(q)
    C[q-1]=factorial(q-1)
    # F = (D + q z H + u z C)/(D - u (q-1) z C)
    P=defaultdict(int);Q=defaultdict(int)
    for i,x in enumerate(D):P[(i,0)]+=x;Q[(i,0)]+=x
    for i,x in enumerate(H):P[(i+1,0)]+=q*x
    for i,x in enumerate(C):P[(i+1,1)]+=x;Q[(i+1,1)]-=(q-1)*x
    return {k:v for k,v in P.items() if v}, {k:v for k,v in Q.items() if v}


def check_rational(q,arr):
    P,Q=polys(q)
    for n in range(len(arr)):
        for k in range(n//q+2):
            lhs=0
            for (d,j),a in Q.items():
                if d<=n and j<=k:lhs+=a*arr[n-d].get(k-j,0)
            if lhs!=P.get((n,k),0):
                raise AssertionError(('rational mismatch',q,n,k,lhs,P.get((n,k),0)))


def arch(word,q):
    seen=set();k=0
    for ch in word:
        seen.add(ch)
        if len(seen)==q: k+=1;seen.clear()
    return k


def direct_univ(word,q,k):
    def is_subseq(t):
        it=iter(word)
        return all(any(c==x for c in it) for x in t)
    return all(is_subseq(t) for t in product(range(q),repeat=k))


def main():
    cells=0;exhaustive=0;direct=0;maxn=54
    for q in range(2,9):
        arr=coeffs(q,maxn)
        check_rational(q,arr)
        cells+=sum(len(v) for v in arr)
        for n in range(1,min(9,12-q)+1):
            cnt=defaultdict(int)
            for w in product(range(q), repeat=n):
                if any(w[i]==w[i+1] for i in range(n-1)):continue
                k=arch(w,q);cnt[k]+=1;exhaustive+=1
                if q<=4 and n<=7:
                    for j in range(1,n//q+2):
                        assert direct_univ(w,q,j)==(j<=k), (q,w,j,k)
                        direct+=1
            assert dict(cnt)==arr[n], ('exhaustive mismatch',q,n,cnt,arr[n])
        assert arr[q][1]==factorial(q)
        for k in range(1,maxn//q+1):
            assert arr[q*k].get(k,0)==factorial(q)*((q-1)*factorial(q-1))**(k-1)
            if q>=3:
                for n in range(q*k+1,min(q*k+7,maxn+1)):
                    assert arr[n].get(k,0)>0
            if q==2:
                for n in range(q*k+2,min(q*k+7,maxn+1)):
                    assert arr[n].get(k,0)==0
        for n,v in enumerate(arr):
            if n:
                assert sum(v.values())==q*(q-1)**(n-1)
    # Independent exact log-derivative check for the probability PGF
    # g(t) = (q-1)(q-1)! (t/(q-1))^q / product(1-h*t/(q-1)).
    for q in range(2,9):
        mean=q+sum(Fraction(h,q-1-h) for h in range(1,q-1))
        logsecond=-q+sum(Fraction(h*h,(q-1-h)**2) for h in range(1,q-1))
        variance=mean+logsecond
        h1=sum(Fraction(1,j) for j in range(1,q))
        h2=sum(Fraction(1,j*j) for j in range(1,q))
        assert mean==1+(q-1)*h1
        assert variance==(q-1)**2*h2-(q-1)*h1
    print('VERIFY_OK q=2..8 recurrence_n=0..54 coefficient_cells=',cells,'exhaustive_proper_words=',exhaustive,'direct_subsequence_tests=',direct)

if __name__=='__main__': main()
