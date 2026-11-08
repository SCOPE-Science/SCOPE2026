#!/usr/bin/env python3
"""Independent, exact coefficient audit for a Gaussian fourth-order chaos identity.
Run with Python 3 standard library, no data downloads.
"""
from collections import defaultdict
from math import factorial
from itertools import product
from fractions import Fraction

def add(*polys):
    ans=defaultdict(int)
    for p in polys:
        for key, val in p.items(): ans[key]+=val
    return {k:v for k,v in ans.items() if v}

def mul(p,q):
    ans=defaultdict(int)
    for (i,j),v in p.items():
        for (k,l),w in q.items(): ans[(i+k,j+l)]+=v*w
    return {k:v for k,v in ans.items() if v}

def expectation(poly):
    def gauss(n): return 0 if n&1 else factorial(n)//(2**(n//2)*factorial(n//2))
    return sum(v*gauss(i)*gauss(j) for (i,j),v in poly.items())

one={(0,0):1}; x2={(2,0):1}; y2={(0,2):1}; xy={(1,1):1}
r=add(x2,y2);r2=mul(r,r)
A=add(r2,{(2,0):-8,(0,2):-8,(0,0):8})
B1=mul(add(x2,{(0,2):-1}),add(r,{(0,0):-6}))
B2=mul({(1,1):2},add(r,{(0,0):-6}))
C1={(4,0):1,(2,2):-6,(0,4):1}
C2={(3,1):4,(1,3):-4}
forms=[A,B1,B2,C1,C2]

def power(p,k):
    ans=one
    for _ in range(k):ans=mul(ans,p)
    return ans

def quadruple_compositions(total,number):
    if number==1:
        yield (total,);return
    for v in range(total+1):
        for rest in quadruple_compositions(total-v,number-1):yield (v,)+rest

def canonical_moment(exps):
    poly=one
    for f,k in zip(forms,exps):poly=mul(poly,power(f,k))
    coeff=factorial(4)
    for k in exps: coeff=Fraction(coeff,factorial(k))
    return expectation(poly)*int(coeff)

# Coefficient polynomial utilities in five variables.
unit=(0,0,0,0,0)
def mon(index):
    e=list(unit);e[index]=1
    return {tuple(e):1}
def cadd(*polys):
    d=defaultdict(int)
    for p in polys:
        for key,v in p.items():d[key]+=v
    return {k:v for k,v in d.items() if v}
def cmul(p,q):
    d=defaultdict(int)
    for i,v in p.items():
        for j,w in q.items():d[tuple(x+y for x,y in zip(i,j))]+=v*w
    return {k:v for k,v in d.items() if v}
def cscale(p,c):return {k:v*c for k,v in p.items() if v*c}
def cpow(p,n):
    o={unit:1}
    for _ in range(n):o=cmul(o,p)
    return o

a,b1,b2,c1,c2=[mon(k) for k in range(5)]
u=cadd(cpow(b1,2),cpow(b2,2));v=cadd(cpow(c1,2),cpow(c2,2))
sign=cadd(cmul(cadd(cpow(b1,2),cscale(cpow(b2,2),-1)),c1),cscale(cmul(cmul(b1,b2),c2),2))
E2=cadd(cscale(cpow(a,2),64),cscale(u,48),cscale(v,192))
E4=cadd(cscale(cpow(a,4),1216512),cscale(cpow(u,2),739584),cscale(cpow(v,2),3870720),cscale(cmul(cpow(a,2),u),4626432),cscale(cmul(cpow(a,2),v),9658368),cscale(cmul(u,v),6359040),cscale(cmul(a,sign),7520256))

def identity_check():
    for i in range(5):
        for j in range(5):
            t=expectation(mul(forms[i],forms[j]));expected=[64,48,48,192,192][i] if i==j else 0
            assert t==expected,(i,j,t,expected)
    print('EXACT_FIVE_ORTHOGONAL_CHAOS_BASIS_VECTORS_OK')
    cnt=0
    for e in quadruple_compositions(4,5):
        actual=canonical_moment(e);expected=E4.get(e,0)
        assert actual==expected,(e,actual,expected)
        cnt+=1
    assert cnt==70
    print('EXACT_ALL_70_FOURTH_MOMENT_COEFFICIENTS_OK',cnt)
    # The square |a b + conjugate(b)c|^2 is expanded polynomially.
    mod_sq=cadd(cmul(cpow(a,2),u),cmul(u,v),cscale(cmul(a,sign),2))
    rhs=cadd(cscale(cpow(a,4),786432),cscale(cpow(u,2),497664),cscale(cmul(cpow(a,2),v),7077888),cscale(cmul(u,cadd(cpow(a,2),cscale(v,3))),221184),cscale(mod_sq,3760128))
    left=cadd(E4,cscale(cpow(E2,2),-105))
    assert left==rhs
    print('EXACT_POSITIVE_SUM_OF_SQUARES_REMAINDER_OK')
    # Exact endpoint of rank-one Hermite: H4(x)=x^4-6x^2+3.
    H4={(4,0):1,(2,0):-6,(0,0):3}
    assert expectation(power(H4,2))==24
    assert expectation(power(H4,4))==368064
    assert expectation(power(H4,4))==639*24*24
    # Upper bound from product formula of fourth-order multiple Wiener integrals.
    from math import comb
    terms=[(factorial(r)*comb(4,r)**2)**2*factorial(8-2*r) for r in range(5)]
    assert sum(terms)==368064
    assert [t//576 for t in terms]==[70,320,216,32,1]
    print('EXACT_RANK_ONE_639_AND_CONTRACTION_COEFFICIENTS_OK')
    print('ALL_BINARY_FOURTH_WIENER_CHAOS_CHECKS_OK')

if __name__=='__main__':identity_check()
