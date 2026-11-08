#!/usr/bin/env python3
"""Exact arithmetic checks for Haar-unitary sixth-moment inequalities.
Standard library only. All checks finite; the proof handles arbitrary dimensions.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial

S3=list(permutations(range(3)))
def inv(p): return tuple(p.index(i) for i in range(len(p)))
def comp(p,q): return tuple(p[q[i]] for i in range(len(p)))
def cycle_types(p):
    seen=set(); ls=[]
    for i in range(len(p)):
        if i not in seen:
            j=i; z=0
            while j not in seen:
                seen.add(j); z+=1;j=p[j]
            ls.append(z)
    return tuple(sorted(ls))
def inverse(A):
    n=len(A); a=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        k=next(k for k in range(i,n) if a[k][i]);a[i],a[k]=a[k],a[i]
        z=a[i][i];a[i]=[v/z for v in a[i]]
        for j in range(n):
            if j!=i:
                z=a[j][i];a[j]=[a[j][k]-z*a[i][k] for k in range(2*n)]
    return [row[n:] for row in a]
def weingarten_by_gram(n):
    mat=[[n**len(cycle_types(comp(inv(p),q))) for q in S3] for p in S3]
    return inverse(mat)
def formula(n,x):
    assert len(x)==n and sum(x)==1
    q2=sum(a*a for a in x);q3=sum(a*a*a for a in x)
    if n==2: return Q(1,4)+Q(3,2)*x[0]*x[1]
    return Q(6)*(n*n-2-3*n*q2+4*q3)/(n*(n*n-1)*(n*n-4))
def via_gram(n,x):
    G=weingarten_by_gram(n)
    wg={p:G[0][i] for i,p in enumerate(S3)}
    power={j:sum(z**j for z in x) for j in (1,2,3)}
    return 6*sum(wg[p]*__import__('math').prod(power[k] for k in cycle_types(p)) for p in S3)
def real_ratio(n,x): return Q(5,2)*n**3*formula(n,x)
checks=0
for n in range(3,10):
    G=weingarten_by_gram(n)
    # Inverse Gram matrix verifies all 36 entries, independently of the formula.
    G0=[[n**len(cycle_types(comp(inv(p),q))) for q in S3] for p in S3]
    assert all(sum(G0[i][k]*G[k][j] for k in range(6))==int(i==j) for i in range(6) for j in range(6))
    for k in range(1,6):
        for s in product(range(k+1),repeat=min(n-1,3)):
            if sum(s)>k:continue
            xx=[Q(a,k) for a in s]+[Q(0) for _ in range(n-len(s))]
            xx[-1]=1-sum(xx)
            if xx[-1]<0:continue
            assert via_gram(n,xx)==formula(n,xx), (n,xx)
            r=real_ratio(n,xx)
            assert Q(15*n*n,(n+1)*(n+2))<=r<=15,(n,xx,r)
            delta=[a-Q(1,n) for a in xx]
            defect=Q(15*n*n,(n*n-1)*(n*n-4))*sum(d*d*(3*n-4*(a+Q(2,n))) for d,a in zip(delta,xx))
            assert 15-r==defect,(n,xx,r,defect)
            checks+=1
for n in range(2,16):
    x=[Q(1,n)]*n; y=[Q(1)]+[Q(0)]*(n-1)
    assert real_ratio(n,y)==Q(15*n*n,(n+1)*(n+2))
    assert real_ratio(n,x)==(Q(25,2) if n==2 else Q(15))
    checks+=2
for k in range(0,101):
    x=[Q(k,100),Q(100-k,100)]
    assert real_ratio(2,x)==Q(5)+30*x[0]*x[1]
    assert 5<=real_ratio(2,x)<=Q(25,2)
    checks+=1
print('UNITARY_GRAM_WEINGARTEN_EXACT_CHECKS_PASSED',checks)
print('UNITARY_SHARP_RANK_ENDPOINTS_AND_STABILITY_PASSED')
