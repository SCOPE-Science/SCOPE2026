#!/usr/bin/env python3
"""Exact finite certificate for type-F4 Schubert Weil/Cartier quotients.
Run with Python 3 standard library: python3 f4_cartier_check.py
Coxeter generators s1,...,s4 use the stated Cartan convention.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from math import gcd

A = ((2,-1,0,0), (-1,2,-2,0), (0,-1,2,-1), (0,0,-1,2))
N=4
E = tuple(int(i==j) for i in range(N) for j in range(N))
def mul(a,b):
    return tuple(sum(a[N*i+k]*b[N*k+j] for k in range(N))
                 for i in range(N) for j in range(N))
def apply(m, v):
    return tuple(sum(m[N*i+j]*v[j] for j in range(N)) for i in range(N))
S=[]; H=[]
for i in range(N):
    r=list(E); c=list(E)
    for j in range(N):
        r[N*i+j]-=A[i][j]
        c[N*i+j]-=A[j][i]
    S.append(tuple(r));H.append(tuple(c))
# Root reflection built from corresponding root/coroot vectors.
def refl(alpha, beta):
    v=tuple(sum(beta[i]*A[i][j] for i in range(N)) for j in range(N))
    return tuple(int(i==j)-alpha[i]*v[j] for i in range(N) for j in range(N))
assert all(refl(tuple(int(k==i) for k in range(N)),tuple(int(k==i) for k in range(N)))==S[i] for i in range(N))
# BFS computes the unique 1,152 group elements, a shortest reduced word for each,
# and the Coxeter length. Enumerated matrices are intrinsic, not group names.
W=[E]; where={E:0}; length=[0]; word=[()]; todo=deque([0])
while todo:
    v=todo.popleft()
    for s in range(N):
        M=mul(W[v],S[s])
        if M not in where:
            where[M]=len(W); W.append(M); length.append(length[v]+1)
            word.append(word[v]+(s,));todo.append(where[M])
assert len(W)==1152 and max(length)==24
assert tuple(Counter(length)[i] for i in range(25)) == (
 1,4,9,16,25,36,48,60,71,80,87,92,94,92,87,80,71,60,48,36,25,16,9,4,1)
# Independent reflection/inversion test. There are precisely 24 positive F4 roots.
paired=set()
for w in W:
    # dual Weyl actions on simple coroot vectors from the SAME reduced word
    # are recomputed from words, not inferred from root matrices.
    cv=E
    for s in word[where[w]]:cv=mul(cv,H[s])
    for s in range(N):
        e=tuple(int(k==s) for k in range(N))
        alpha=apply(w,e); beta=apply(cv,e)
        if all(x<=0 for x in alpha):
            alpha=tuple(-x for x in alpha);beta=tuple(-x for x in beta)
        assert all(x>=0 for x in alpha)
        assert all(x>=0 for x in beta)
        paired.add((alpha,beta))
assert len(paired)==24
assert len({a for a,b in paired})==24
reflectors={refl(alpha,beta):beta for alpha,beta in paired}
assert len(reflectors)==24
positive=[a for a,b in paired]
for w,L in zip(W,length):
    assert sum(all(t<=0 for t in apply(w,a)) for a in positive)==L

def det(m):
    n=len(m)
    if n==0:return 1
    return sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
               * __import__('math').prod(m[i][p[i]] for i in range(n))
               for p in permutations(range(n)))

def invariant_factors(M):
    n=len(M); assert all(len(row)==n for row in M)
    prev=1; factors=[]
    for k in range(1,n+1):
        d=0
        for I in combinations(range(n),k):
            for J in combinations(range(n),k):
                d=gcd(d,abs(det([[M[i][j] for j in J] for i in I])))
        assert d>0 and d%prev==0
        factors.append(d//prev);prev=d
    assert all(factors[i+1]%factors[i]==0 for i in range(len(factors)-1))
    return tuple(x for x in factors if x>1)

counts=Counter(); lengths_by_type=Counter(); maximal=[]; covers_total=0
for wi,w in enumerate(W):
    support=tuple(sorted(set(word[wi])))
    covers={}
    # Strong-exchange check by deleting all positions in a reduced expression.
    for j,s in enumerate(word[wi]):
        drop=E
        for t in word[wi][:j]+word[wi][j+1:]:drop=mul(drop,S[t])
        x=where[drop]
        if length[x]!=length[wi]-1:continue
        suffix=word[wi][j+1:]
        invU=E; cU=E
        for t in reversed(suffix):
            invU=mul(invU,S[t]);cU=mul(cU,H[t])
        e=tuple(int(k==s) for k in range(N))
        alpha=apply(invU,e); beta=apply(cU,e)
        if all(t<=0 for t in beta):
            alpha=tuple(-t for t in alpha);beta=tuple(-t for t in beta)
        assert all(t>=0 for t in beta)
        assert mul(w,refl(alpha,beta))==drop
        if x in covers:assert covers[x]==beta
        covers[x]=beta
    # Independent cover generation from all 24 positive root reflections.
    alternate={}
    for ref,beta in reflectors.items():
        x=where[mul(w,ref)]
        if length[x]==length[wi]-1:
            alternate[x]=beta
    assert covers==alternate,(wi,word[wi],covers,alternate)
    covers_total+=len(covers)
    M=tuple(tuple(beta[s] for s in support) for _,beta in sorted(covers.items()))
    n=len(support)
    assert len(M)>=n
    if len(M)!=n:continue   # Non-Q-factorial; positive-rank defect.
    factors=invariant_factors(M)
    ty='trivial' if not factors else 'x'.join(str(k) for k in factors)
    counts[ty]+=1
    lengths_by_type[(length[wi],ty)]+=1
    if ty=='2x2':maximal.append((tuple(x+1 for x in word[wi]), M))
assert counts==Counter({'trivial':171,'2':49,'2x2':13}), counts
assert len(maximal)==13
assert sum(counts.values())==233
assert covers_total>0
assert any(ww==(2,3,2,4,3,2) and MM==((1,0,0),(1,2,0),(1,2,2)) for ww,MM in maximal)
print('Type F4: |W|=',len(W),', positive roots=',len(paired),', total covers=',covers_total,sep='')
print('Q-factorial:',sum(counts.values()), 'non-Q-factorial:',len(W)-sum(counts.values()))
print('Cl/Pic=0:',counts['trivial'], '; Z/2:',counts['2'],'; (Z/2)^2:',counts['2x2'])
print('WITNESS (Z/2)^2:',maximal[0][0],maximal[0][1])
print('LENGTH TABLE: length, factorial, order2, order4')
for L in range(25):
    print(L, lengths_by_type[(L,'trivial')],lengths_by_type[(L,'2')],lengths_by_type[(L,'2x2')])
print('CHECKS PASS: enumeration, inversion lengths, reflection covers, determinants, minors.')
