#!/usr/bin/env python3
"""Exact reproducibility checks for the characteristic-three Humbert rank strata.

Requires Python >= 3.9 and sympy. The all-extension theorem is proved in RESULT.md;
these computations verify polynomial identities, geometric disjointness and sample fields.
"""
from itertools import combinations
from sympy import symbols, groebner, Poly

u, v, w = symbols('u v w')
F = [u+1,v+1,u+v,u+v+1,u*v+u+v]
Delta = u*v*(u-1)*(v-1)*(u-v)
# All pairwise intersections are excluded by the smooth-locus equation Delta != 0.
for i,j in combinations(range(5),2):
    ideal = groebner([F[i],F[j],w*Delta-1], w,u,v, modulus=3)
    assert len(ideal.polys)==1 and ideal.polys[0].as_expr()==1,(i,j,list(ideal))
print('PAIRWISE_DISJOINT_ON_M05=10_PAIRS')

# Characteristic-three Hasse invariant for each of the five Legendre parameters.
Lams = [(v-1,u-1),(v,u),(v*(1-u),v-u),(v,1),(u,1)]
for k,((n,d),f) in enumerate(zip(Lams,[F[3],F[2],F[4],F[1],F[0]]),1):
    # Hasse coefficient of x^2 is -(1+lambda). Thus n+d=0.
    assert Poly(n+d, u,v, modulus=3).rem(Poly(f,u,v,modulus=3)).is_zero,(k,n,d,f)
    # Both polys have same zero locus on smooth parameter space via unit coefficients.
    assert Poly(n+d,u,v,modulus=3).total_degree()==Poly(f,u,v,modulus=3).total_degree()
print('FIVE_LEGENDRE_HASSE_EQUATIONS=PASS')

class Field:
    # polynomial x^m + sum coef[i] x^i, low-degree first, mod 3.
    def __init__(self, coeff):
        self.mod = tuple(int(x)%3 for x in coeff)
        self.m = len(coeff)
        self.q = 3**self.m
        self.zero=tuple([0]*self.m)
        self.one=tuple([1]+[0]*(self.m-1))
        self.elements=list(self._ints())
    def _ints(self):
        for x in range(self.q):
            y=x
            a=[]
            for _ in range(self.m):
                a.append(y%3);y//=3
            yield tuple(a)
    def add(self,a,b):return tuple((a[i]+b[i])%3 for i in range(self.m))
    def neg(self,a):return tuple((-a[i])%3 for i in range(self.m))
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        v=[0]*(2*self.m-1)
        for i in range(self.m):
            for j in range(self.m):v[i+j]=(v[i+j]+a[i]*b[j])%3
        for i in range(2*self.m-2,self.m-1,-1):
            t=v[i]
            for j in range(self.m):v[i-self.m+j]=(v[i-self.m+j]-t*self.mod[j])%3
        return tuple(v[:self.m])
    def pow(self,a,n):
        r=self.one
        while n:
            if n%2:r=self.mul(r,a)
            a=self.mul(a,a);n//=2
        return r
    def div(self,a,b):
        assert b!=self.zero
        return self.mul(a,self.pow(b,self.q-2))
    def eq3(self,x):return x==self.zero

def enumerate_rank(qpoly):
    K=Field(qpoly)
    q=K.q
    z,o=K.zero,K.one
    negone=K.neg(o)
    if q>3:
        for a in K.elements:
            if a==z:continue
            assert K.pow(a,q-1)==o
    counter=[0,0,0,0,0,0]
    for u0 in K.elements:
        if u0 in (z,o):continue
        for v0 in K.elements:
            if v0 in (z,o,u0):continue
            fs=[K.add(u0,o), K.add(v0,o), K.add(u0,v0),K.add(K.add(u0,v0),o),K.add(K.add(K.mul(u0,v0),u0),v0)]
            r=sum(t==z for t in fs)
            assert r<=1,('multiple supersingular factors',u0,v0,fs)
            ls=[K.div(K.sub(v0,o),K.sub(u0,o)), K.div(v0,u0), K.div(K.mul(v0,K.sub(o,u0)),K.sub(v0,u0)),v0,u0]
            assert r==sum(x==negone for x in ls)
            counter[r]+=1
    assert counter[0] == (q-3)*(q-7), (q,counter)
    assert counter[1] == 5*(q-3), (q,counter)
    assert sum(counter)==(q-2)*(q-3)
    print(f'FIELD_Q={q};ORDINARY={counter[0]};P_RANK_4={counter[1]};TOTAL={sum(counter)}')

for poly in ((0,),(1,0),(1,2,0)):
    # degree 1: x; degree 2: x^2+1; degree 3: x^3-x+1
    enumerate_rank(poly)
print('VERIFY_OK')
