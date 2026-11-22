#!/usr/bin/env python3
"""Exact symbolic and finite tests for short cycles of T(a,b)=(a+b,ab)."""
import sympy as S
from itertools import product
x,y=S.symbols('x y')
def iterate(a,b,n):
    for _ in range(n):a,b=S.expand(a+b),S.expand(a*b)
    return a,b
A3,B3=iterate(x,y,3)
F3=S.cancel((A3-x)/y);G3=S.cancel((B3-y)/y)
assert S.factor(S.resultant(F3,G3,y))==x*(x*x+x+1)**2
assert S.rem(F3,x*x+x+1,x)==x*y
A4,B4=iterate(x,y,4)
F4=S.cancel((A4-x)/y);G4=S.cancel((B4-y)/y)
H4=S.cancel(F4/(x+1))
assert S.expand(H4)==x*x*y+x*x+x*y*y+x*y+1
assert S.factor(S.resultant(H4,G4,y))==x**3*(x*x+1)**4
assert S.factor(G4.subs(x,-1))==-y*(y*y-2*y+2)
assert S.rem(G4.subs(y,-1-x),x*x+1,x)==0

def graph_cycle_census(elements,add,mul):
    v=list(product(elements,repeat=2));f=lambda a:(add(a[0],a[1]),mul(a[0],a[1]))
    visited=set();cy={}
    for start in v:
        if start in visited:continue
        seq=[];inds={};now=start
        while now not in visited and now not in inds:
            inds[now]=len(seq);seq.append(now);now=f(now)
        if now in inds:
            period=len(seq)-inds[now]
            cy[period]=cy.get(period,0)+1
        visited.update(seq)
    return cy
for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]:
    got=graph_cycle_census(list(range(p)),lambda a,b:(a+b)%p,lambda a,b:a*b%p)
    expect4=int(p%4==1)
    assert got.get(1,0)==p and got.get(2,0)==0 and got.get(3,0)==0 and got.get(4,0)==expect4,(p,got)
# binary extension fields represented in polynomial bases (multiply via a monic irreducible polynomial)
def F2ext(m,polynomial):
    size=1<<m;mask=size-1
    def add(a,b):return a^b
    def mul(a,b):
        z=0
        while b:
            if b&1:z^=a
            b>>=1;a<<=1
            if a&(1<<m):a^=polynomial
        return z&mask
    return list(range(size)),add,mul
for m,polynomial in [(1,0b11),(2,0b111),(3,0b1011),(4,0b10011),(5,0b100101),(6,0b1000011)]:
    got=graph_cycle_census(*F2ext(m,polynomial))
    assert got.get(1,0)==2**m and all(got.get(k,0)==0 for k in (2,3,4)),(m,got)
# GF(9)=F3[u]/(u^2+1); u^2=-1
els=list(range(9))
def gf9_add(a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
def gf9_mul(a,b):
    a0,a1=a%3,a//3;b0,b1=b%3,b//3
    return (a0*b0-a1*b1)%3+3*((a0*b1+a1*b0)%3)
assert graph_cycle_census(els,gf9_add,gf9_mul).get(4)==1
# Products of fields: point count fixed by T^4 is product of fixed counts.
for ps in [(2,5),(5,5),(5,7),(3,13),(7,11),(5,13,17)]:
    actual=(S.prod(p+4*int(p%4==1) for p in ps)-S.prod(ps))//4
    assert actual>=0
for ps in [(2,5),(3,5),(5,5),(5,7),(5,13)]:
    states=list(product(*(range(p) for p in ps)))
    add=lambda a,b:tuple((a[j]+b[j])%ps[j] for j in range(len(ps)))
    mul=lambda a,b:tuple(a[j]*b[j]%ps[j] for j in range(len(ps)))
    got=graph_cycle_census(states,add,mul)
    expected=(S.prod(p+4*int(p%4==1) for p in ps)-S.prod(ps))//4
    assert got.get(1,0)==S.prod(ps) and got.get(4,0)==expected,(ps,got,expected)
    assert got.get(2,0)==got.get(3,0)==0,(ps,got)
print('SHORT_CYCLE_SPECTRUM_OK')
