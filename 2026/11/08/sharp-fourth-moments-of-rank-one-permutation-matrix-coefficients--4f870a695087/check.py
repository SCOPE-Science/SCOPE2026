#!/usr/bin/env python3
"""Exact finite checks for the rank-one permutation coefficient fourth-moment theorem."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

def E_formula(n,a,b):
    sa=sum(x*x for x in a);sb=sum(y*y for y in b)
    assert sum(a)==sum(b)==0 and sa and sb
    u=F(sum(x**4 for x in a),sa*sa)
    v=F(sum(y**4 for y in b),sb*sb)
    if n==2: return F(1)
    if n==3: return F(3,2)
    return F(n-1,n*(n-2)*(n-3))*(n*n*(n+1)*u*v-3*n*(n-1)*(u+v)+3*(n*n-3*n+3))

def E_direct(n,a,b):
    arr=[sum(a[i]*b[p[i]] for i in range(n)) for p in permutations(range(n))]
    m2=F(sum(x*x for x in arr),factorial(n))
    m4=F(sum(x**4 for x in arr),factorial(n))
    assert m2==F(sum(x*x for x in a)*sum(y*y for y in b),n-1)
    return m4/(m2*m2)

def upper(n):return F(n*n-3*n+3,n*(n-1))
def lower(n):return F(n,(n//2)*((n+1)//2))-F(3,n)
def R(n,u,v):
    return F(n-1,n*(n-2)*(n-3))*(n*n*(n+1)*u*v-3*n*(n-1)*(u+v)+3*(n*n-3*n+3))
def target(n):
    if n==2:return F(1)
    if n==3:return F(3,2)
    if n==4:return F(3)
    return F(n*n-3*n+3,n-1)

def centered_patterns(n):
    profiles=[]
    for k in range(1,n):
        profiles.append(tuple([n-k]*k+[-k]*(n-k)))
    for q in range(1,n):
        v=tuple([i%3-1 for i in range(n)])
        w=tuple([i%4-2 for i in range(n)])
        for z in (v,w):
            avg=F(sum(z),n)
            a=tuple(F(x)-avg for x in z)
            if sum(t*t for t in a)>0: profiles.append(a)
    profiles.append(tuple([n-1]+[-1]*(n-1)))
    return sorted(set(profiles),key=str)

checks=0
for n in range(2,8):
    ps=centered_patterns(n)
    for ia,a in enumerate(ps):
        for ib,b in enumerate(ps):
            if n==7 and ((ia+3*ib)%5):continue
            e=E_formula(n,a,b)
            d=E_direct(n,a,b)
            assert e==d,(n,a,b,e,d)
            assert d<=target(n),(n,a,b,d,target(n))
            checks+=1
print('EXACT_PERMUTATION_FOURTH_MOMENT_IDENTITIES_OK',checks)

corners=0
for n in range(4,201):
    l=F(1,n);h=upper(n)
    assert upper(n)==F(n,(n-1))-F(3,n)
    vals=[R(n,l,l),R(n,l,h),R(n,h,l),R(n,h,h)]
    assert max(vals)==target(n)
    assert vals[1]==vals[2]==1
    if n==4:
        assert vals[0]==3 and vals[3]==F(7,3)
    else:
        assert vals[3]>vals[0] and vals[3]>1
    corners+=1
print('EXACT_BILINEAR_RECTANGLE_DOMINANCE_OK',corners)

profiles=0
for n in range(4,81):
    p={}
    for k in range(1,n):
        a=[n-k]*k+[-k]*(n-k)
        u=F(sum(x**4 for x in a),sum(x*x for x in a)**2)
        assert u==F(n,k*(n-k))-F(3,n)
        p[k]=u
        profiles+=1
    assert max(p.values())==upper(n)
    assert min(p.values())==lower(n)
    assert [k for k,u in p.items() if u==upper(n)]==[1,n-1]
print('EXACT_TWO_LEVEL_POWER_SUM_EXTREMA_OK',profiles)

for n in [2,3,4,5,6,7]:
    spike=[n-1]+[-1]*(n-1)
    k=n//2
    balanced=[n-k]*k+[-k]*(n-k)
    a=balanced if n==4 else spike
    assert E_direct(n,a,a)==target(n)
print('EXACT_ATTAINMENT_AND_FOUR_STATE_TRANSITION_OK')
print('ALL_PERMUTATION_RANK_ONE_MOMENT_CHECKS_OK')
