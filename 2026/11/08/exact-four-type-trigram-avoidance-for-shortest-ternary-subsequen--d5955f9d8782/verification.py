#!/usr/bin/env python3
"""Exact ternary trigram-avoidance enumeration checks (stdlib only).

Run with: python verification.py
No external data or packages are required.
"""
from itertools import permutations, product
from collections import Counter

ALPH = '012'
ARCHES = [''.join(p) for p in permutations(ALPH)]
CANON = ('000', '001', '010', '012')
# Ascending powers in z, with the coefficient of z^0 first.
RATIONAL = {
    '000': ((0, 6), (1, -6)),
    '001': ((0, 6, -2), (1, -6, 2)),
    '010': ((0, 6, -4), (1, -6, 4)),
    '012': ((0, 5, 6, 2), (1, -3, -5, -2)),
}

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return tuple(a)

def add(a,b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return trim(out)

def minus(a,b):
    return add(a,tuple(-x for x in b))

def mult(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return trim(out)

def determinant_poly(mat):
    n=len(mat)
    total=(0,)
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        prod=(sign,)
        for i,j in enumerate(perm): prod=mult(prod,mat[i][j])
        total=add(total,prod)
    return total

def matrices(pat):
    v=[int(pat not in arch) for arch in ARCHES]
    T=[[int(pat not in (x+y) and v[j]) for j,y in enumerate(ARCHES)]
       for x in ARCHES]
    M=[[(int(i==j),-T[i][j]) for j in range(6)] for i in range(6)]
    # Matrix determinant lemma: det(M + 1*v^T)-det(M)=v^T adj(M) 1.
    Mplus=[[(int(i==j)+v[j],-T[i][j]) for j in range(6)] for i in range(6)]
    return v,T,M,Mplus

def canonical(p):
    # Canonical classes under alphabet relabeling and reversal.
    orbit=[]
    for pi in permutations(ALPH):
        u=''.join(pi[int(x)] for x in p)
        orbit.extend((u,u[::-1]))
    return min(orbit)

def is_subseq(u,w):
    i=0
    for c in w:
        if i<len(u) and c==u[i]: i+=1
    return i==len(u)

def is_univ(w,k):
    return all(is_subseq(''.join(x),w) for x in product(ALPH,repeat=k))

def transferred(pat,k):
    v,T,_,_=matrices(pat)
    for step in range(1,k):
        v=[sum(v[i]*T[i][j] for i in range(6)) for j in range(6)]
    return sum(v)

def coefficient(k,N,D):
    values=[0]*(k+1)
    for n in range(1,k+1):
        rhs=N[n] if n<len(N) else 0
        rhs-=sum(D[j]*values[n-j] for j in range(1,min(n,len(D)-1)+1))
        values[n]=rhs
    return values[k]


def run():
    for p in CANON:
        N,D=RATIONAL[p]
        v,T,M,MP=matrices(p)
        d=determinant_poly(M)
        a=minus(determinant_poly(MP),d)
        assert d==D,(p,'denominator',d,D)
        assert trim((0,)+a)==N,(p,'numerator',a,N)
        for k in range(1,31):
            assert transferred(p,k)==coefficient(k,N,D),(p,k)
    print('EXACT: four transfer determinants, adjugate numerators and 120 recurrence coefficients verified.')
    pats=[''.join(t) for t in product(ALPH,repeat=3)]
    assert set(map(canonical,pats))==set(CANON)
    checked=0
    for k in (1,2,3):
        counters=Counter()
        universal_count=0
        for tup in product(ALPH,repeat=3*k):
            w=''.join(tup)
            truth=is_univ(w,k)
            arch=all(set(w[3*i:3*i+3])==set(ALPH) for i in range(k))
            assert truth==arch,(k,w,truth,arch)
            checked+=1
            if truth:
                universal_count+=1
                factors={w[i:i+3] for i in range(len(w)-2)}
                for p in pats:
                    if p not in factors: counters[p]+=1
        assert universal_count==6**k
        for p in pats:
            assert counters[p]==transferred(p,k),(k,p,counters[p],transferred(p,k))
    print('EXHAUSTIVE:',checked,'ternary words of lengths 3, 6, 9 checked by literal subsequence membership; all 81 pattern-count comparisons passed.')
    for p in CANON:
        print('COEFFICIENTS',p, [transferred(p,k) for k in range(1,7)])
    print('PASS')

if __name__=='__main__': run()
