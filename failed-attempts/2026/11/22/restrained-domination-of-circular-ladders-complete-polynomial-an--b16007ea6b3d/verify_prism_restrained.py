#!/usr/bin/env python3
"""Exact finite checks of the restrained-domination prism formula.

Requires Python >= 3.9 and sympy. Graph and algebra definitions are included.
"""
from collections import defaultdict
from itertools import product
from sympy import symbols, zeros, eye, expand, factor, simplify, diff, nroots

x,z,u,t = symbols('x z u t')
SYMBOLS = range(4)

def permitted(left, middle, right, restrained=True):
    for layer in (0,1):
        if (middle >> layer) & 1:
            continue
        num = ((left >> layer)&1) + ((right >> layer)&1) + ((middle >> (1-layer))&1)
        if num == 0 or (restrained and num == 3):
            return False
    return True

def transfer(restrained):
    T=zeros(16,16)
    for a,b,c in product(SYMBOLS, repeat=3):
        if permitted(a,b,c,restrained):
            T[4*a+b,4*b+c] = z**b.bit_count()
    return T

F1=1-x*z+x*x*z+x*x*z*z-x**3*z*z
F2=1-x*z-x*z*z-x*x*z-2*x*x*z*z+x*x*z**3-2*x**3*z*z-2*x**3*z**3-x**3*z**4+x**5*z**3+x**6*z**4
DOM=(1+x*x*z)*(1-2*x*z-x*z*z-x*x*z-x*x*z*z-x**3*z*z-x**3*z**3+x**4*z**3+x**5*z**3)

def direct_counts(n, restrained):
    # Each 2-bit pair encodes one labelled rung; no circular-word assumptions.
    adj=[]
    for i in range(n):
        for layer in (0,1):
            adj.append((2*i+(1-layer), 2*((i-1)%n)+layer, 2*((i+1)%n)+layer))
    masks=[sum(1<<j for j in adj[i]) for i in range(2*n)]
    counts=[0]*(2*n+1)
    for s in range(1<<(2*n)):
        good=True
        for i, a in enumerate(masks):
            if not (s>>i)&1:
                p=(s&a).bit_count()
                if p==0 or (restrained and p==3):
                    good=False;break
        if good:counts[s.bit_count()]+=1
    return counts

def words_counts(n, restrained):
    # A separate direct transfer recurrence, not determinant extraction.
    out=[0]*(2*n+1)
    transitions={4*a+b:[4*b+c for c in SYMBOLS if permitted(a,b,c,restrained)] for a in SYMBOLS for b in SYMBOLS}
    for start in range(16):
        dp={(start,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for (st,k),v in dp.items():
                for to in transitions[st]:
                    nxt[(to,k+(st%4).bit_count())]+=v
            dp=nxt
        for k in range(2*n+1):out[k]+=dp.get((start,k),0)
    return out

def gcd_graph_check(restrained):
    E={4*a+b:[4*b+c for c in SYMBOLS if permitted(a,b,c,restrained)] for a in SYMBOLS for b in SYMBOLS}
    for source in range(16):
        seen={source};queue=[source]
        for q in queue:
            for v in E[q]:
                if v not in seen:seen.add(v);queue.append(v)
        assert len(seen)==16, (restrained,source,seen)
    assert 15 in E[15], 'nonaperiodic graph'
    return True

R=transfer(True); D=transfer(False)
assert expand((eye(16)-x*R).det(method='domain-ge') - F1*F2)==0
assert expand((eye(16)-x*D).det(method='domain-ge') - DOM)==0
print('DETERMINANT_IDENTITIES_OK')

# Formal low-weight expansion controls every n, not just checked finite orders.
R0=expand((F1*F2).subs({x:u/t,z:t*t}))
O0=expand(DOM.subs({x:u/t,z:t*t}))
rd=[expand(R0).coeff(t,k) for k in range(3)]
od=[expand(O0).coeff(t,k) for k in range(3)]
assert factor(rd[0]-(1-u**4))==0
assert factor(rd[1]-u*(u*u-2)*(u*u+1)**2)==0
assert factor(rd[2]-2*u**6)==0
assert factor(od[0]-rd[0])==0 and factor(od[1]-rd[1])==0

def H2(d):
    p0,p1,p2=d
    L2=p1*p1/(2*p0*p0)-p2/p0
    return factor(u*diff(L2,u))
hr=H2(rd);ho=H2(od)
assert factor(ho-hr-2*u*u*(1+4*u**4-u**8)/(1-u**4)**2)==0
q=u**4
expected_H2=(16*q*(1+q)/(1-q)**3+8*q/(1-q)**2) + u*u*(16*q*(1+q)/(1-q)**3+16*q/(1-q)**2+4/(1-q)) + 3*u**6
assert factor(hr-expected_H2)==0
print('ALL_ORDER_LOW_WEIGHT_IDENTITIES_OK')

for rest in (True,False):
    assert gcd_graph_check(rest)
    for n in range(3,10):
        assert words_counts(n,rest)==direct_counts(n,rest),('direct',rest,n)
print('DIRECT_SUBSET_VERSUS_TRANSFER_OK')

for n in range(4,31):
    data=words_counts(n,True)
    minimum=next(i for i,v in enumerate(data) if v)
    expected=(n+1)//2 + (n%4==2)
    expected_count= 4 if n%4==0 else 2*n if n%2 else n*n+(3 if n==6 else 0)
    assert (minimum,data[minimum])==(expected,expected_count),(n,minimum,data[minimum],expected,expected_count)
    assert data[-1]==1 and data[-2]==0 and data[-3]==3*n
print('MINIMUM_AND_BOUNDARY_COEFFICIENTS_OK')

xr=0.31911123526340224; xd=0.27262070249429576
assert abs(float((F1*F2).subs({x:xr,z:1})))<1e-8
assert abs(float(DOM.subs({x:xd,z:1})))<1e-8
assert xr>xd>0
print('PERRON_ROOTS_NUMERICALLY_CHECKED', 1/xr, 1/xd, xd/xr)
print('VERIFY_OK')
