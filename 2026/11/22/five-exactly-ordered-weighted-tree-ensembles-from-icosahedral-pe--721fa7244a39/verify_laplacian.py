#!/usr/bin/env python3
"""Exact weighted spanning-tree enumeration for the icosahedral network.

All arithmetic uses Python integers and rational numbers. No nonstandard packages.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

N=12

def edges():
    e=set()
    for i in range(5):
        u=1+i; v=6+i
        for a,b in ((0,u),(11,v),(u,1+(i+1)%5),
                    (v,6+(i+1)%5),(u,v),(u,6+(i+1)%5)):
            e.add(tuple(sorted((a,b))))
    assert len(e)==30
    return tuple(sorted(e))
E=edges()
ADJ={i:set() for i in range(N)}
for a,b in E: ADJ[a].add(b);ADJ[b].add(a)
assert sorted(map(len,ADJ.values()))==[5]*12

def matching_completion(avail):
    if not avail:
        yield frozenset()
        return
    a=min(avail)
    for b in sorted(ADJ[a]&avail):
        for tail in matching_completion(avail-{a,b}):
            yield tail|{(min(a,b),max(a,b))}

MATCHINGS=tuple(matching_completion(set(range(N))))
assert len(MATCHINGS)==125 and len(set(MATCHINGS))==125

def bareiss_det(a):
    a=[list(map(int,row)) for row in a]
    n=len(a); prev=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            q=next((i for i in range(k+1,n) if a[i][k]),None)
            if q is None: return 0
            a[k],a[q]=a[q],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                tmp=a[i][j]*pivot-a[i][k]*a[k][j]
                assert tmp%prev==0
                a[i][j]=tmp//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def tree_number(marked,t):
    L=[[0]*11 for _ in range(11)]
    for a,b in E:
        w=t if (a,b) in marked else 1
        if a<11:L[a][a]+=w
        if b<11:L[b][b]+=w
        if a<11 and b<11:L[a][b]-=w;L[b][a]-=w
    return bareiss_det(L)

def polynomial_from_values(values):
    # The Newton forward formula: f(t)=sum Delta^k f(0)*binomial(t,k).
    differences=list(values);out=[Fraction(0)]*len(values)
    product=[Fraction(1)]
    for k in range(len(values)):
        factor=Fraction(differences[0],1)
        for j in range(1,k+1):factor/=j
        for j,z in enumerate(product):out[j]+=factor*z
        differences=[differences[i+1]-differences[i] for i in range(len(differences)-1)]
        new=[Fraction(0)]*(len(product)+1)
        for j,c in enumerate(product):new[j]-=k*c;new[j+1]+=c
        product=new
    assert all(v.denominator==1 for v in out)
    return tuple(int(v) for v in out)

def div_tminus1_squared(c):
    # Divide by t^2-2t+1 in descending degree.
    a=list(c); q=[0]*(len(a)-2)
    for d in range(len(a)-1,1,-1):
        v=a[d];q[d-2]=v;a[d]-=v;a[d-1]+=2*v;a[d-2]-=v
    assert a[:2]==[0,0],a
    return tuple(q)

def flips_four(m):
    count=0
    for other in MATCHINGS:
        dif=m^other
        if len(dif)!=4:continue
        deg=Counter(x for e in dif for x in e)
        if len(deg)==4 and all(n==2 for n in deg.values()):count+=1
    return count

by_poly=defaultdict(list)
for m in MATCHINGS:
    samples=tuple(tree_number(m,t) for t in range(7))
    poly=polynomial_from_values(samples)
    assert len(poly)==7
    assert tree_number(m,7)==sum(c*7**k for k,c in enumerate(poly))
    by_poly[poly].append(m)
assert len(by_poly)==5
classes=sorted(by_poly.items(),key=lambda q:-len(q[1]))
assert sorted(len(mm) for pp,mm in classes)==[5,10,20,30,60]
assert all(sum(pp)==5184000 for pp,mm in classes)
assert all(sum(k*pp[k] for k in range(7))==11404800 for pp,mm in classes)
# Strict order by the first matching in class: 5 > 20 > 60 > 30 > 10,
# for every positive t different from 1. Positivity is certified coefficientwise.
ordered=sorted(classes,key=lambda x:len(x[1]))
ordered=[next((p for p,m in classes if len(m)==c)) for c in (5,20,60,30,10)]
for hi,lo in zip(ordered,ordered[1:]):
    q=div_tminus1_squared(tuple(a-b for a,b in zip(hi,lo)))
    assert all(z>=0 for z in q) and q[0]>0
winners=next(mm for pp,mm in classes if len(mm)==5)
losers=next(mm for pp,mm in classes if len(mm)==10)
assert len([m for m in MATCHINGS if flips_four(m)==0])==5
assert all(flips_four(m)==0 for m in winners)
assert all(flips_four(m)>0 for m in losers)
for poly,mm in classes:
    print('CLASS',len(mm),'poly-ascending',','.join(map(str,poly)),'sample',sorted(next(iter(mm))), 'flip4',flips_four(mm[0]))
print('ORDER 5>20>60>30>10 FOR t>0, t!=1; PASS')
